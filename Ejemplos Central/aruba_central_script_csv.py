import requests
import csv
import json
import time
import pprint

#####################################

client_id = 'bf4b92503bda482aa6388a96b8d7198c'
client_secret = '1f3c50a4697b481b914b32adf3c61b59'
refresh_token = '1f2a55889ea140c692e767d4585c1729'
access_token = 'cee9f6f5e471401893716a4275f26e98'

#refresh_token
#refresh_token = requests.get('https://internal-apigw.central.arubanetworks.com/oauth2/token?client_id=' + client_id + '&client_secret=' + client_secret + '&grant_type=refresh_token&refresh_token='+ refresh_token)
#access_token = refresh_token.json()
#pprint.pprint('access_token')

#date to epoch
date_start = input("Date from:  dd.mm.yyyy hh:mm:ss ")
date_end = input("Date to:  dd.mm.yyyy hh:mm:ss ")
pattern = '%d.%m.%Y %H:%M:%S'
start = int(time.mktime(time.strptime(date_start, pattern)))
end = int(time.mktime(time.strptime(date_end, pattern)))

#API Bandwith_usage
url = requests.get('https://internal-apigw.central.arubanetworks.com/monitoring/v1/clients/bandwidth_usage/topn?access_token=' + access_token + '&from_timestamp='+ str(start) + '&to_timestamp='+ str(end))
json_parsed = url.json()

pprint.pprint (json_parsed)
#####################################
#

emp_data = json_parsed['clients'] #KeyError <-----

#print (type(json_parsed))


# open a file for writing
employ_data = open('/home/nreyes/Documents/api/ReporteEjemplo.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(employ_data)

count = 0

for emp in emp_data:
    if count == 0:
        header = emp.keys()
        csvwriter.writerow(header)
    count += 1
    csvwriter.writerow(emp.values())

employ_data.close()
