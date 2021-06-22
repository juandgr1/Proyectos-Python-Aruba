import requests
import csv
import json
import time
import pprint

base_url = "https://internal-apigw.central.arubanetworks.com"

url = "/configuration/v1/groups/"
fullurl = base_url + url

limit = 20
offset = 0
access_token= "bLJPZpTj225dzpXJ8y9fArHY3O0uG2Kk"

parameters = {"access_token": access_token, "limit": limit, "offset": offset}

resp = requests.get("https://internal-apigw.central.arubanetworks.com/configuration/v1/groups",params=parameters)
print (resp.json())
