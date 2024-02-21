from mlflow import log_metric, log_param, log_artifacts 
import mlflow



if __name__ == "__main__":
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    # Log a parameter (key-value pair)
    log_param("threshold", 3)
    log_param("verborisy", "DEBUG")


    # Log a metric; metrics can be updated throughout the run
    log_metric("timestamp", 10000)
    log_metric("TTC", 33)
    
    log_artifacts("produced-dataset.csv")