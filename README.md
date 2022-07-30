

# Project Title - Operationalizing Banks loan Recommendation Model

Before getting into project overview I would like to in short describe  **WHY**  Machine learning.

We all know there's something  powerfull with Machine Learning 'So what's that?'

*Its the iterative nature of machine learning that's key, unlike traditional computing with machine learning as models are exposed to new data, they are able to independently evolve without any human intervention.* WOW! (understandable it isn't new, just thought of highlighting)

In this project we will demonstrate ML pipeline automation using both Azure ML Studio and Python SDK. We'll also showcase ML components and how they work together in the process of 

    1. Authentication
    2. Ingest Data
    2. TrainAuto ML model
    3. Deploy Best model 
    4. Enable logging 
    5. Consume model endpoints
    6. Create and Publish pipeline
    7. Documentation

We'll elaborate on above items from architecture, Auto ML and Python SDK project tasks perspective. It  gives  a high-level understanding of the components and how they work together to assist in the process of building, deploying, and maintaining machine learning models.

## Architectural Diagram


![Project Architural Diagram](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/project/UdacityAzureMLProjArch.png)


### Architectural Foundational components

**Azure Storage Account** An Azure storage account contains all of your Azure Storage data objects, including blobs, file shares, queues, tables, and disks. The storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in your storage account is durable and highly available, secure, and massively scalable.
    
**Datastores** are attached to workspaces and are used to store connection information to Azure storage services so you can refer to them by name and don't need to remember the connection information and secret used to connect to the storage services.
    
**Azure Machine Learning compute cluster** is a managed-compute infrastructure that allows you to easily create a single or multi-node compute. The compute cluster is a resource that can be shared with other users in your workspace. The compute scales up automatically when a job is submitted, and can be put in an Azure Virtual Network. The compute executes in a containerized environment and packages your model dependencies in a Docker container. *It's available as environments with Azure ML workspace.*
    
**Azure compute instance** is a fully managed cloud-based workstation optimized for your machine learning development environment. Its used to run Jupyter notebooks.

### Azure Machine Learning Workspace

Workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. The workspace keeps a history of all training runs, including logs, metrics, output, and a snapshot of your scripts. You use this information to determine which training run produces the best model.

Once you have a model you like, you register it with the workspace. You then use the registered model and scoring scripts to deploy to Azure Container Instances, Azure Kubernetes Service, as a REST-based HTTP endpoint.

### Azure Machine Learning Assets
    
**Datasets** aid in management of the data you use for model training and pipeline creation.
    
**Experiments or Jobs** are training runs you use to build your models.
    
**Models** are at the heart of Azure Machine learning. A model is the result of a Azure Machine learning training Run via Auto ML or SDK using notebooks.
    
**Endpoints:** After you train a machine learning model, you need to deploy the model so that others can use it to do inferencing. In Azure Machine Learning, you can use **endpoints** and **deployments** to do so.

An **endpoint** is an HTTPS endpoint that clients can call to receive the inferencing (scoring) output of a trained model. 

A **deployment** is a set of resources required for hosting the model that does the actual inferencing.

A single endpoint can contain multiple deployments. Endpoints and deployments are independent Azure Resource Manager resources that appear in the Azure porta

**Pipelines** are reusable workflows for training and retraining your model.
    
**Azure Machine Learning environment** is where your machine learning training happens. They specify the Python packages, environment variables, and software settings around your training and scoring scripts. They also specify run times (Python, Spark, or Docker)
    
    
    
    
## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

### Step 1:  Authentication

**Successfully created service principal for given workspace**

![Create Service Principal](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/ServicePrincipalCreated1.png)


**Deprecated workspace command using az role assignment**

![Deprecated workspace command](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/azmlworkspacedepricated.png)

### Step 2: Automated ML Experimant 

**Data Ingest** 

**Create Bank Marketing Dataset**

![Create dataset](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/CreateDataset1.png)


![Bank Marketing Dataset](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/bankmarketingdatasetautoml1.png)

**Registered Data Assets**

![Register Data asset](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/registereddataset1.png)


### Create new Automated ML Job and configure job

**Bank loan recommendation experiment is using Classification technique for yes/no prediction**

![Created Auto ML Job](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/experiment1.png)


**Automated ML run completed** 

![Experiment 1](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/ExperimentCompleted1.png)


### Step 3: Deploy Best Model anf create endpoint

**Deploy the Model**

**Select Best Model**

![Select Best Model](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/bestmodel1.png)

**Selected Best Model**

![Best Model Selected](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/bestmodel2.png)


### Step 4: Enable Logging - Application Insights

**Enable App Insight using Python SDK Webservice logs.py**

![Logs.py](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/logspyenableappinsight.png)


**Enabled Application Insight - Model showing application insight link**

![Enabled App Insight](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/modelendpoint_appinsight.png)

### Step 5: Swagger Documentaion - Consume deployed model using Swagger

**Swagger Instance for Model HTTP API**

![Swagger for HTTP API](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/swagger_prjlocal1.png)

**Swagger runs HTTP API Methods and response for the model**

![Swagger HTTP Response](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/swaggerhubmodelresponse.png)

### Step 6: Consume model Endpoints

**Model endpoint**

![Model Endpoint](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/projmodelendpoint.png)


**Python SDK consume model endpoint**

![Consume Model endpoint](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/endpointconsumemodelpy.png)


**Run Model using Python SDK - Output**

![Run Model Python](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/endpoint_run_prjassign2_jsonoutput.png)

### Step 7: Create, Publish and Consume Pipeline

**Jupyter notebook uploaded**

https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/project/aml-pipelines-with-automated-machine-learning-step.ipynb

**Pipeline Created**

![](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/notebookpipelinecreated.png)

**Pipeline Endpoint**

![](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/notebookpipelineendpoint.png)

**Pipeline Active Status**
![pipeline active](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/biketrainpipelineactivestatus.png)

**Pipeline Executed Run Widget**

![](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/project/notebookpipelinecompleted.png)


## Aditional details

**Endpoint Execution Results**

![Endpoint Execution results](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/endpoint/endpoint1.png)


**Benchmark Results form ab command**
![ab_benchmark_result1](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/benchmark/ab_benchmark_result1.png)


**Notebook run Confusion matrics**

![Notebook confusion matrics](https://github.com/Nazeer2013/nd00333_AZMLND_C2/blob/master/assignment2/images/notebook/confusionmatricsvisual.png)



## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

## References
https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore.datastore?view=azure-ml-py

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?tabs=python

https://docs.microsoft.com/en-us/azure/machine-learning/concept-workspace

https://docs.microsoft.com/en-us/azure/machine-learning/concept-endpoints

https://docs.microsoft.com/en-us/azure/machine-learning/concept-environments







