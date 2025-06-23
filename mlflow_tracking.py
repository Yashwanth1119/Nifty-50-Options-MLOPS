import mlflow

def log_experiment(model, X_test, y_test, params):
    mlflow.set_experiment("Nifty Options IV Prediction")
    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.sklearn.log_model(model, "model")
        score = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", score)
