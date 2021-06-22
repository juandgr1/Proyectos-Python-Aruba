import requests
import csv
import json
import time
import pprint

access_token= "bLJPZpTj225dzpXJ8y9fArHY3O0uG2Kk"
base_url = "https://internal-apigw.central.arubanetworks.com"
get_var_url = "/configuration/v1/devices/"
device_serial="CN71HKZ1D9"
temp_var="/template_variables"
fullurl = base_url + get_var_url + device_serial + temp_var

parameters = {"access_token": access_token}

response = requests.get(fullurl,params=parameters)
datos = response.json()
#print (datos)
#pprint.pprint(response.json())
#decoded_json =  resp.json()
#datos = json.loads(response.text)
print (datos["data"]["total"])
print (datos["data"]["variables"]["ip"])




