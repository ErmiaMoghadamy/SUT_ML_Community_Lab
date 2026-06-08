FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if your ML libraries or pipeline need them
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files and your saved weights
COPY main.py lib.py model.pkl pipeline.pkl .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]