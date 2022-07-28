from azureml.core import Workspace
from azureml.core.webservice import Webservice

import urllib.request
import json
import os
import ssl

import azureml.core

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "instant": 0,
        "date": "2022-01-01T00:00:00.000Z",
        "season": 0,
        "yr": 0,
        "mnth": 0,
        "weekday": 0,
        "weathersit": 0,
        "temp": 0.0,
        "atemp": 0.0,
        "hum": 0.0,
        "windspeed": 0.0,
        "casual": 0,
        "registered": 0
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'https://demo-model-deploy-assignment2.centralus.inference.ml.azure.com/score'
api_key = 'cgDKuA7GFnQQHdavdMVd7GST1Xlfu1so' # Replace this with the API key for the web service

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'myudacitydeploymentmodel' }

req = urllib.request.Request(url, body, headers)

print(req.full_url)

# Requires the config to be downloaded first to the current working directory
# ws = Workspace.from_config()

# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
from azureml.core import Workspace, Dataset

subscription_id = '16bc73b5-82be-47f2-b5ab-f2373344794c'
resource_group = 'epe-poc-nazeer'
workspace_name = 'nahmed30-azureml-workspace'

ws = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(ws, name='UdacityAssignment2BikeNo')
dataset.to_pandas_dataframe()

# name='demo-model-deploy-assignment2'
# 'userTenantId': 'db05faca-c82a-4b9d-b9c5-0f64b6755421', 'userName': 'Ahmed', 'upn': None})


# name='myudacitydeploymentmodel'
# name='myudacitydeploymentmodel-demo-model-deploy-assignment2'
# name='demo-model-deploy-assignment2'

# name='udacityassignment2bikemodel-udacitybikemodel'

name='deploy-model-assign2'

# services = Webservice.list(ws)
#print('services array length ', len(services))
#print(services[0])
print('\n','--------------------------------------------------------------------')
#print(services[1])
# print(services[0].swagger_uri)

# Monitor and collect data from ML web service endpoints
# https://docs.microsoft.com/en-us/azure/machine-learning/how-to-enable-app-insights#web-service-metadata-and-response-data

# https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.aci.aciwebservice?view=azure-ml-py

# print(azureml.core.VERSION)
# load existing web service
service = Webservice(name=name, workspace=ws)
service.update(enable_app_insights=True)


logs = service.get_logs()

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
