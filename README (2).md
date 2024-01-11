
## MLFLOW_Tutorial

PLease refer below sections and follow the step to run and learn.

<details><summary> <h3> Mlflow Installation Steps </h3> </summary>
<p>

#### Step1: Run a below command to install a mlflow(You can run this command in jupyter notebook cell as well)
```ruby
pip install mlflow
```
#### Step2: Check version of mlflow
```ruby
# for command line
mlflow --version

# For jupyter notebook
mlflow.__version__
```  
#### (Optional)Step3: It is recommend to create an new environment before installting mlflow
```ruby
conda create -n mlflow_env
conda activate mlflow_env
pip install mlflow
```    
</p>
</details>





There are 4 components of MLflow and they can be used independently.
* <strong> MLflow Tracking:</strong> It is used for logging metrics, parameters, code versions and output files
* <strong> MLflow Projects:</strong> It can package the code in a way in order to reproduce it on any plotform.
* <strong> MLflow Models:</strong> It is a standard format for packaging machine learning models that can be used in a variety of downstream tools—for example, real-time serving through a REST API or batch inference on Apache Spark. 
* <strong> MLflow Model Registry:</strong> It is a centralized model store, set of APIs, and web interface to manage the full ML lifecycle.



<details><summary> <h3> MLflow Tracking </h3> </summary> 
<p>
<br> MLflow Tracking is probably the most used tool in industry by ML engineers and data scientists. Lets quickly see how to use mlflow tracking to track the metrics and parameters.

You can copy and paste below code in jupyter notebook named [train.ipynb]("https://github.com/ShubhPatil95/MLFlow-Tutorial/blob/main/train.ipynb")

```ruby
import mlflow

if __name__ == "__main__":
    mlflow.log_param("Param-1", "Apple")
    mlflow.log_param("Param-2", 11)
    mlflow.log_metric("Metrics-1",12)
    mlflow.log_metric("Metrics-2",20.5)

    with open("test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifact("test.txt")
```
Now run below line in next cell of train.ipynb and you will get URL UI like http://127.0.0.1:5000.
```ruby
mlflow ui
```
 Go to URL http://127.0.0.1:5000 and you will see output as below.<br>
<img src="https://github.com/ShubhPatil95/MLFlow-Tutorial/blob/main/images/UI-outputs-1.jpg" alt="UI output-1">

You can click on run and you will see below page showing all detail with test.txt file.

<img src="https://github.com/ShubhPatil95/MLFlow-Tutorial/blob/main/images/UI-outputs-1-Inside.png" alt="UI-outputs-1-Inside">
</p>
</details>



<details><summary> <h3> MLFlow-Simple-ML-Project </h3> </summary>
<p>
<br> Here in this section will see how to create a entire project using MLFlow.

#### Step1: Create a folder Mlflow_Project_Package and move inside the folder
```ruby
mkdir Mlflow_Simple_ML_Project
cd Mlflow_Simple_ML_Project
```
#### Step2: Create a train.py by copying code from here [train.py](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Simple_ML_Project/train.py)
```ruby
nano train.py
```  
#### Step3: Lets try to understand train.py/
```ruby
with mlflow.start_run():   # The parameters,metrics and artifacts under indentation of this line will be recorded.

    mlflow.log_param("param_name",param_value)  # It will log the paramters

    mlflow.log_metric("metric_name", metric_value)  # IT will log the metrics
  
    mlflow.sklearn.log_model(model, "model_name")    # It will record model created by sklearn
```

#### Step4: Lets run train.py and wait till successful execution.
  
```ruby
python3 train.py
```   
    
#### Step5: You will notice that new folder under mlruns will be created.
  
```ruby
ls  # this command will show mlruns folder is created
```
  
#### Step6: Now its time to go to mlflow UI to see systematically presented parameters, metrics and artificats. Then it will generated URL for UI: http://127.0.0.1:5000.
```ruby
mlflow ui
```
  
#### Step7: On UI you will see all the metrics and logs we have recorded through our code. Explore this UI and enjoy it.
  
</p>
</details>




<details><summary> <h3> MLFlow_Project_Package </h3> </summary>
<p>
<br> Till now we have seen, how to create a project using MLFlow. Further moving ahead in this section we will learn how to package a project in a MLFlow way.

#### Step1: Create a folder Mlflow_Project_Package and move inside of it
```ruby
mkdir Mlflow_Project_Package
cd Mlflow_Project_Package
```
#### Step2: Create a new conda env
```ruby
conda create -n mlflow_env python=3.7 -y

conda activate mlflow_env
```
#### Step3: Create a python file train.py and copy paste code from [train.py](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/train.py) or You can create train.ipynb file from [train.ipynb](https://github.com/ShubhPatil95/MLFlow-Tutorial/blob/main/train.ipynb)
```ruby
nano train.py
```
#### Step4: Create requirements.txt and paste code from [requirements.txt](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/requirements.txt) and then run second command
```ruby
nano requirements.txt
pip install -r requirements.txt
```
#### Step5: Check if train.py is running
```ruby
python3 train.py  
```
#### Step6: run below command and check if results are logged into mlflow ui. If you have train.ipynb file in step3 then you can run this command in next cell of jupyter notebook as well.
```ruby
mlflow ui
```
#### Step7: Create [conda.yaml](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/conda.yaml) exporting depencies into it or you can go to mlflow ui and copy paste same conda.yaml file.
```ruby
conda env export > conda.yaml
```
#### Step8: Create file under name MLproject and copy paste from [MLproject](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/MLproject)
```ruby
nano MLproject
```
#### Step9: Run below command to check if package is running(second command will run it in local existing conda)
```ruby
mlflow run . -P intercept=False
mlflow run . -P intercept=False --no-conda
```
#### Step10: How to share your project??<br>
just share below four file and ask to run command <strong>mlflow run .</strong>
```ruby
  1. requirements.txt
  2. train.py
  3. conda.yaml 
  4. MLproject 
````
#### Step11: How to run project from github? <br> (make sure code on github is directly inside repo not under any folder of repo) Run below command.
```ruby
 # mlflow run git@github.com:Username/Repo_Name --version branch_name
   mlflow run git@github.com:ShubhPatil95/Mlflow_Project_Package --version main -P intercept=True
```
 #### Step12: mlflow run using python API, just create file [MLFlow_Project_API.py](https://github.com/ShubhPatil95/Mlflow_Project_Package/blob/main/MLFlow_Project_API.py)
```ruby
 python3 MLFlow_Project_API.py
```
  
</p>
</details>



