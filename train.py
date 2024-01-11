import mlflow

if __name__ == "__main__":
    mlflow.log_param("Param-1", "Apple")
    mlflow.log_param("Param-2", 11)
    mlflow.log_metric("Metrics-1",12)
    mlflow.log_metric("Metrics-2",20.5)
    
    with open("test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifacts("test.txt")


    

