import requests
import json

# Добавление нового питомца
info={
  "id": 0,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Marusya",
  "photoUrls": [
    ""
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_post_add_pet = requests.post( f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
data=json.dumps(info, ensure_ascii=False))
print(res_post_add_pet.status_code)
print(res_post_add_pet.json())

#
res_get_petid = requests.get(f'https://petstore.swagger.io/v2/pet/9223372036854775807', headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(res_get_petid.status_code)
print(res_get_petid.json())

# Изменение имени питомца
new_info={
  "id":9223372036854775807,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name":"Zoe",
  "photoUrls": [
    ""
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_put_new_name = requests.put( f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
data=json.dumps(new_info, ensure_ascii=False))
print(res_put_new_name.status_code)
print(res_put_new_name.json())


#Удаление питомца
res_del_petid = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854775807', headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(res_del_petid.status_code)
print(res_del_petid.json())
