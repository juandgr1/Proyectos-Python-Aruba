import requests
import csv
import json
import time
import pprint

access_token= "qzLnt1ghijuCo12GrhSitC4TZA2J3Cmo"
base_url = "https://internal-apigw.central.arubanetworks.com"
get_var_url = "/configuration/v1/devices/"
device_serial="CN71HKZ1D9"
temp_var="/template_variables"
fullurl = base_url + get_var_url + device_serial + temp_var
header = {'content-type': 'application/json'}
parameters = {"access_token": access_token}

response = requests.get(fullurl,params=parameters)
datos = response.json()
print("\n Switch IP:" )
print (datos["data"]["variables"]["ip"])
print("Ingrese los valores de la VLAN a Configurar\n " )
vlan_id=str(raw_input("Digite el ID de la vlan: "))
vlan_name=raw_input(("Digite el nombre de la vlan: "))
print ("El ID de la VLAN a configurar es: " + vlan_id + " y el nombre de la vlan es: " + vlan_name)

act_var={"total": 33, "variables": {"_sys_lan_mac": "f4:03:43:07:96:50","vlan.id.new1":vlan_id,"vlan.id.nombre1":vlan_name}}
#print act_var["variables"]["_sys_lan_mac"]
data=json.dumps(act_var)

response2=requests.patch(fullurl, data=data, params=parameters, headers=header)
print("\n Configuracion Exitosa")
