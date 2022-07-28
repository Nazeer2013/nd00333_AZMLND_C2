from azureml.core import Workspace
from azureml.core.webservice import Webservice

import urllib.request
import json
import os
import ssl


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
    "quantiles": [
      0.025,
      0.975
    ]
  }
}

body = str.encode(json.dumps(data))

url = 'https://udacitybikemodel.centralus.inference.ml.azure.com/score'
api_key = 'H8ZUmEyjLjeMlZPhQAKT2AaLm4XU7rs9' # Replace this with the API key for the web service

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'udacityassignment2bikemodel' }

req = urllib.request.Request(url, body, headers)

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config()

name='udacityassignment2bikemodel'

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