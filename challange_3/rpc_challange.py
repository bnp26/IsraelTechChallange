from xmlrpclib import ServerProxy
import json
import requests

url = "http://ITC@hack.israeltechchallenge.com:8000/jsonrpc"
headers = {'content-type': 'application/json'}

payload = {"method": "help", "jsonrpc": "2.0", "id": 0,}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()

print response["result"]
for method in proxy.system.listMethods():
    print method
    print proxy.system.methodHelp(method)
    print
methods = proxy.system.listMethods()

print methods

