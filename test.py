import requests
response = requests.get('http://127.0.0.1:5000/api/testing', json={"net_ident": "1111",
                                                                   "net": "Tg"})

print(response.content)