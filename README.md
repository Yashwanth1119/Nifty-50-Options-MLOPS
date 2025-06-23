# Nifty 50 Options Trading MLOps Project

## Overview
This project predicts Nifty 50 option price movements using an MLOps pipeline with MongoDB, Streamlit, MLflow, Prefect, and GitHub Actions.

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
