import requests
import json
import requests
import json
import sys

# Over View
# arg1: Code
# arg2/arg3: Fromdate/ToDate

# get param
config=json.load(open('config.json', 'r'))
username=config["username"]
password=config["password"]
if len(sys.argv) > 1 : parameters="?code="+sys.argv[1]+"0"
if len(sys.argv) > 2 : parameters=parameters+"&from="+sys.argv[2]
if len(sys.argv) > 3 : parameters=parameters+"&to="+sys.argv[3]

def main():
    data={"mailaddress":username, "password":password}
    r_post = requests.post("https://api.jpx-jquants.com/v1/token/auth_user", data=json.dumps(data))
    r_post.json()
    refreshToken=r_post.json()["refreshToken"]
    r_post = requests.post(f"https://api.jpx-jquants.com/v1/token/auth_refresh?refreshtoken={refreshToken}")
    idToken=r_post.json()['idToken']
    headers = {'Authorization': 'Bearer {}'.format(idToken)}
    r = requests.get("https://api.jpx-jquants.com/v1/prices/daily_quotes"+parameters, headers=headers)
    print(r.json())
    return r.json()

if __name__ == "__main__":
    main()