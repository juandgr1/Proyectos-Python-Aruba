import requests
import csv
import json
import time
import pprint

access_token= "xwIqSbyev4qrefDGG6lbZie7h4FS9AOy"
base_url = "https://internal-apigw.central.arubanetworks.com"
get_var_url = "/configuration/v1/devices/"
get_sw_info = "/monitoring/v1/switches"
device_serial="CN71HKZ1D9"
temp_var="/template_variables"
get_var_full_url = base_url + get_var_url + device_serial + temp_var
get_sw_info_url = base_url + get_sw_info
header = {'content-type': 'application/json'}
parameters = {"access_token": access_token}
response1 = requests.get(get_var_full_url,params=parameters)
response3 = requests.get(get_sw_info_url,params=parameters)
datos1 = response1.json()
datos2 = response3.json()
print (datos1["data"]["total"])
print (datos1["data"]["variables"]["ip"])
#print datos2
#print datos2["data"]

print("\n DIGITE DATOS DE LA VLAN A CREAR")
vlan_id=str(raw_input("Digite el ID de la vlan: "))
vlan_name=raw_input(("Digite el nombre de la vlan: "))
print ("El ID de la VLAN es: " + vlan_id + " y el nombre de la vlan es: " + vlan_name)

act_var={"total": 33, "variables": {"_sys_lan_mac": "f4:03:43:07:96:50","vlan.id.new1":vlan_id,"vlan.id.nombre1":vlan_name}}
#print act_var["variables"]["_sys_lan_mac"]
data=json.dumps(act_var)

response2=requests.patch(get_var_full_url, data=data, params=parameters, headers=header)
print("\n Configuracion Exitosa")
