# Nifty 50 Options Trading MLOps Project

## Overview
This project predicts Nifty 50 option price movements using an MLOps pipeline with MongoDB, Streamlit, MLflow, Prefect, and GitHub Actions.

## Project Directory Structure
```bash
nifty50-options-mlops/
│
├── .github/workflows/
│   └── ci-cd.yml                  # GitHub Actions CI/CD pipeline
├── artifacts/                     # Store intermediate data/models
├── data/                          # Raw and processed data
├── notebooks/
│   └── eda_visualization.ipynb    # EDA & Data Viz
├── pipeline/
│   ├── data_ingestion.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── prediction.py
├── prefect_flows/
│   └── option_pipeline.py         # Prefect Flow Orchestration
├── streamlit_app/
│   └── app.py                     # Streamlit Interface
├── docker/
│   └── Dockerfile
├── requirements.txt
├── .env
├── mlflow_tracking.py
├── README.md
└── main.py

```
## Features
- 📥 Data Ingestion via Prefect
- 🧪 Feature Engineering & Model Training
- 🧠 Model Logging via MLflow
- 📊 Visualization using Streamlit
- 🔁 CI/CD using GitHub Actions

## Run the Pipeline
```bash
prefect run -p prefect_flows/option_pipeline.py
```

## Run Streamlit App
```bash
streamlit run streamlit_app/app.py
```
