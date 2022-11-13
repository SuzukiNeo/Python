import requests
import json
import requests
import json
import sys

# Over View
# arg1: Code

# get param
config=json.load(open('config.json', 'r'))
username=config["username"]
password=config["password"]

def main():
    data={"mailaddress":username, "password":password}
    r_post = requests.post("https://api.jpx-jquants.com/v1/token/auth_user", data=json.dumps(data))
    r_post.json()
    refreshToken=r_post.json()["refreshToken"]
    r_post = requests.post(f"https://api.jpx-jquants.com/v1/token/auth_refresh?refreshtoken={refreshToken}")
    idToken=r_post.json()['idToken']
    headers = {'Authorization': 'Bearer {}'.format(idToken)}
    r = requests.get("https://api.jpx-jquants.com/v1/listed/sections?code="+sys.argv[1]+"0", headers=headers)
    print(r.json())
    return r.json()

if __name__ == "__main__":
    main()