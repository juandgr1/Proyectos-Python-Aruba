import requests
import csv
import json
import time
import pprint

base_url = "https://sheet.best/api/sheets/e2c356c0-1690-45ec-a67a-1b8307135019"

resp = requests.get(base_url,params=parameters)
print (resp.json())
