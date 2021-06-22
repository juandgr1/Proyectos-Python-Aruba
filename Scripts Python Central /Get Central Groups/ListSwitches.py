import requests
import json

base_url = "https://internal-apigw.central.arubanetworks.com"

url = "/monitoring/v1/switches"
fullurl = base_url + url

access_token= "bLJPZpTj225dzpXJ8y9fArHY3O0uG2Kk"

parameters = {"access_token": access_token,}

resp = requests.get(fullurl,params=parameters)
print(resp.json())