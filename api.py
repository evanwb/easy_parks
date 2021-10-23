import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

global api_key
api_key='pQNtyh3wP65oZT5zeLWTMAIRTHTEnTCQE1nRHz9L'




def print_json(input_obj):
    res = json.dumps(input_obj, sort_keys=True, indent=5)
    print(res)
    

def park_total(code):
    url = 'https://developer.nps.gov/api/v1/parks?stateCode={}&api_key={}'.format(code,api_key)
    response = requests.get(url, verify=False)
    js = response.json()
    if len(js["data"]) == 0:
        res = 'Please enter a valid state'
    else:     
        res = 'There are a total of {} parks in {}'.format(len(js["data"]), code.upper())
    return (res)


""" for i in range(len(js["data"])):
	list = [js["data"][i]["fullName"], js["data"][i]["parkCode"]] 
	text = '{} Park name: {}, Park Code: {}'.format(i+1,list[0],list[1])
	print(text+'\r\n') """
#print_json(js["data"][0]["fullName"])

#print_json(response.json())
