import requests

response = requests.get("https://realearth.ssec.wisc.edu/api/products?exclude=times")

for i in response.json():
    print(i["id"])
