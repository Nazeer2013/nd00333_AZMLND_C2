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
        "age": 40,
        "job": "admin",
        "marital": "married",
        "education": "university.degree",
        "default": "no",
        "housing": "no",
        "loan": "yes",
        "contact": "telephone",
        "month": "jun",
        "day_of_week": "wed",
        "duration": 126,
        "campaign": 4,
        "pdays": 999,
        "previous": 0,
        "poutcome": "nonexistent",
        "emp.var.rate": 1.4,
        "cons.price.idx": 98,
        "cons.conf.idx": -40,
        "euribor3m": 4.9,
        "nr.employed": 5200
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

body = str.encode(json.dumps(data))

url = 'http://1f655212-371f-4f32-b0dd-17c0a1882ed3.centralus.azurecontainer.io/score'
api_key = 'UCtQO9i75A2HGF6g9HpFkqjbXbC5dgYM' # Replace this with the API key for the web service

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
