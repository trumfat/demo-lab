import requests

r = requests.get("https://10.10.5.81/api/initial-data?format=json", auth=("admin", "avi123"), verify=False)
data = r.json()
print data
