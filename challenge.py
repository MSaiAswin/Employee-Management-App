import requests

res = requests.get('https://fdeployserver.up.railway.app/challenge').json()

token = res["token"]
num1 = int(res["num1"])
num2 = int(res["num2"])

data = {"token":token, "answer": num1+num2}

print(requests.post('https://fdeployserver.up.railway.app/deploy',json=data).text)
