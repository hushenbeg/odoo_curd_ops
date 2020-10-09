import requests
import json
from odoo_client import OdooClient

# url = 'http://localhost:8069'

payload = {
    'url':'http://127.0.0.1:8069',
    'db': 'employee',
    'username' : 'xxxx@gmail.com',
    'password' : 'xxxx',
    'model_name': 'res.partner'
}


# headers = {
#     'content-type': 'application/json',
# }

# res = requests.post(payload['params']['url'], data=json.dumps(payload), headers=headers)

# res = res.json()

client = OdooClient(payload)

db_response = client.execute_db()

print('--------db_response-------------', db_response)

list_response = client.list_records()

print('-------list_response----------', list_response)

read_response = client.read_records()

print('---------read_records---------', read_response)

# create_response = client.create_records()

# print('----------create_response-----------', create_response)

update_response = client.update_records(10)

print('-----------update_response-----------', update_response)

# delete_response = client.delete_records(11)

# print('----------delete_response--------------', delete_response)

