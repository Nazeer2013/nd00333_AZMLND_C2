
*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Project Title - Operationalizing Bank Loan Recommendation Model

Before getting into project overview I would like to in short describe  **WHY**  Machine learning.

We all know there's something  powerfull with Machine Learning 'So what's that?'

*Its the iterative nature of machine learning that is really important, because unlike traditional computing with machine learning as models are exposed to new data, they are able to independently evolve without any human intervention.* WOW!

In this project we will demonstrate ML pipeline automation using both Azure ML Studio and Python SDK. 
We'll also showcase ML components and how they work together in the process of 

    1. Authentication
    2. Ingest Data
    2. TrainAuto ML model
    3. Deploy Best model 
    4. Enable logging 
    5. Consume model endpoints
    6. Create and Publish pipeline
    7. Documentation

We'll elaborate on above items from architecture, Auto ML and Python SDK project task perspective. It  gives  a high-level understanding of the components and how they work together to assist in the process of building, deploying, and maintaining machine learning models.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

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

It provides: Authentication using "key & token". 

A **deployment** is a set of resources required for hosting the model that does the actual inferencing.

A single endpoint can contain multiple deployments. Endpoints and deployments are independent Azure Resource Manager resources that appear in the Azure porta

**Pipelines** are reusable workflows for training and retraining your model.
    
**Azure Machine Learning environment** is where your machine learning training happens. They specify the Python packages, environment variables, and software settings around your training and scoring scripts. They also specify run times (Python, Spark, or Docker)
    
    
    
    
## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

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







