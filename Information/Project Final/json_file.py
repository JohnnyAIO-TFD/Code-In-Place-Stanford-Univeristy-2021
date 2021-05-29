import json

codigo = []
sku = []
precio = []

archivo = open("Data_Needs.txt", "r")
for line in archivo.readlines():
    cols = line.split('\t')
    codigo.append(cols[0])
    sku.append(cols[1])
    precio.append(cols[2])
archivo.close()

json_file = open('Information_Example.json', 'w')


modelo = {
    "code": " ",
    "imagen": "Image Folder",
    "sku": " ",
    "active": True,
    "stock": 338,
    "default": 1,
    "pvp": 0,
    "laboratory": {
        "id": {
            "$oid": "603175cec969ac088c573a56"
        },
        "name": "Example Works",
        "corporation": "J000252084",
        "logo": "Something Else"
    },
    "proveedor": {
        "id": {
            "$oid": "603175cec969ac088c573a56"
        },
        "name": "Example Works",
        "corporation": "J000252084",
        "logo": "Something Else"
    },
    "createdAt": "2020-12-04T22:05:04.065Z",
    "updatedAt": "2020-12-04T22:05:04.065Z",
    "promotion": {
        "bonification": [],
        "descount": 20
    }
}

n = len(codigo)

for comp in range(0, n):
    modelo['code'] = codigo[comp]
    modelo['sku'] = sku[comp]
    modelo['pvp'] = float(precio[comp])
    json.dump(modelo, json_file)
