# Meeting Minutes: Session 3 - California Housing Price Prediction (End-to-End ML Project)

## Meeting Metadata
- Session Number: 03
- Date: June 4, 2026 (14 Khordad 1405)
- Special Guest: Mr. FakhrAlRami (Data Scientist at Hamrah-e-Aval)
- Attendance Statistics: Average: 10 participants | Peak: 13 participants
- Project Lead: Ermia Moghadami
- Core Presenters: Taha Mohammadi, Hamed Mirzaei, Matin Hayati

---

## 1. Project Mission & Objectives
The primary objective of this project is to build a Machine Learning model to predict the median house price in California based on census data. The team followed the standard 8-step Machine Learning pipeline to move from raw data to a production-ready model.

---

## 2. Workflow & Task Allocation
The project was executed following the industry-standard ML roadmap. The contributions were distributed as follows:

| Step | Phase | Responsible / Contributors |
| :--- | :--- | :--- |
| 1 | Look at the Big Picture | Presented by Taha Mohammadi & Ermia Moghadami |
| 2 | Get the Data | Presented by Ermia Moghadami |
| 3 | Discover & Visualize the Data | Presented by Taha Mohammadi |
| 4 | Prepare the Data for ML | Presented by Ermia Moghadami |
| 5 | Select and Train a Model | Presented by Ermia Moghadami, Taha Mohammadi, & Hamed Mirzaei |
| 6 | Fine-tune the Model | Presented by Ermia Moghadami |
| 7 | Present the Solution | Presented by Ermia Moghadami |
| 8 | Launch, Monitor, and Maintain | Presented by Ermia Moghadami |

---

## 3. Technical Highlights & Session Outcomes

### A) Exploratory Data Analysis (EDA)
Led by the core presentation team, specifically Taha Mohammadi, this phase yielded critical insights:
- Identified a strong positive correlation between Median Income and House Price.
- Detected a "Capping" anomaly where house prices were limited to $500,000.
- Utilized scatter matrices and histograms to understand non-linear relationships.

### B) Feature Engineering
The team developed strategic attributes to improve model accuracy, including:
- rooms_per_household (Measuring house size).
- bedrooms_per_room (Determining luxury vs. standard utility).
- population_per_household (Measuring density).

### C) Modeling Strategy (Decision Trees)
In a collaborative session involving Ermia Moghadami, Taha Mohammadi, and Hamed Mirzaei, the team analyzed the Decision Tree algorithm:
- Implementation of Decision Trees for Regression beyond standard Classification.
- Evaluation of feature space partitioning to predict cluster averages.
- Analysis of Overfitting risks and the implementation of pruning/ensemble methods.

---

## 4. System Deployment & Observability (Infrastructure)
A key highlight of the session was the advanced infrastructure work led by the Project Lead, Ermia Moghadami. The focus was on ensuring the model’s sustainability through professional monitoring tools:

- Deployment Workflow: Orchestrating the project lifecycle to ensure a seamless transition from a local environment to a production-ready state.
- Monitoring & Observability Stack:
    - InfluxDB:* Implemented as a high-performance time-series database to log model predictions and performance metrics.

    - *Grafana: Integrated to build professional, real-time dashboards for tracking model health, data drift, and system latency.
- Outcome: This infrastructure allows the team to monitor the model's behavior in real-world scenarios, marking a significant milestone in the project's technical maturity.

---

## 5. General Notes
- Team Expansion: Matin Hayati officially joined as a Core Presenter during this session and was fully onboarded into the project's end-to-end roadmap.
- Conclusion: The project has successfully moved from theoretical analysis to a fully monitored and deployable architecture.

---

Project Status: ✅ Completed

Written and Prepared by:
Taha Mohammadi*  
Official Project Core Presenter
