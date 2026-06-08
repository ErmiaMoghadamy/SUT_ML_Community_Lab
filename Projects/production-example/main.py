import joblib
import sys
import time
import pandas as pd
from fastapi import FastAPI, HTTPException, BackgroundTasks
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from pydantic_settings import BaseSettings, SettingsConfigDict

import lib

sys.modules['__main__'].CombinedAttributesAdder = lib.CombinedAttributesAdder

# --- Environment Configuration Schema ---
class Settings(BaseSettings):
    influxdb_url: str
    influxdb_token: str
    influxdb_org: str
    influxdb_bucket: str

    # This tells Pydantic to read directly from your .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

try:
    settings = Settings()
except Exception as e:
    raise RuntimeError(f"Initialization failed: Missing or invalid environment variables. {e}")

app = FastAPI(title="California Housing Production API (Monitored)")

try:
    influx_client = InfluxDBClient(
        url=settings.influxdb_url, 
        token=settings.influxdb_token, 
        org=settings.influxdb_org
    )
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)
except Exception as e:
    print(f"Warning: Could not connect to InfluxDB: {e}")
    write_api = None


# --- Load ML Artifacts ---
try:
    model = joblib.load("./model.pkl")
    pipeline = joblib.load("./pipeline.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load serialization artifacts: {e}")


def log_metrics_to_influx(latency_ms: float, prediction: float, ocean_prox: str):
    if write_api:
        try:
            point = (
                Point("inference_performance")
                .tag("ocean_proximity", ocean_prox)
                .field("latency_ms", latency_ms)
                .field("predicted_value", float(prediction))
            )
            write_api.write(bucket=settings.influxdb_bucket, org=settings.influxdb_org, record=point)
        except Exception as err:
            print(f"Failed to write telemetry to InfluxDB: {err}")


@app.post("/predict")
async def predict_housing_value(data: lib.HousingDistrictData, background_tasks: BackgroundTasks):
    start_time = time.time()
    
    try:
        input_df = pd.DataFrame([data.model_dump()])
        
        # ML Inference Pipeline
        prepared_data = pipeline.transform(input_df)
        prediction = model.predict(prepared_data)[0]
        
        latency_ms = (time.time() - start_time) * 1000
        
        # Offload metrics logging to the background thread pool
        background_tasks.add_task(
            log_metrics_to_influx, 
            latency_ms, 
            prediction, 
            data.ocean_proximity
        )
                
        return {
            "predicted_median_house_value": round(prediction, 2),
            "inference_latency_ms": round(latency_ms, 2)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))