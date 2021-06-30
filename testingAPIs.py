import requests

response = requests.get("https://v2.namsor.com/NamSorAPIv2/355abda7daa743a3f786e193a3538e04/json/origin/Franziska/Hafner")

print(response.json())



