import requests, json
from util import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

global api_key


api_key='i9sM3jW7SsBvCXfYV50AugYvXa2zX1pL3HevmxLR'

def park_search(park_code):
    url = 'https://developer.nps.gov/api/v1/parks?parkCode={}&api_key={}'.format(park_code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()

    for i in range(len(data["data"])):
        park = {
            "name": data["data"][0]["fullName"],
            "code": data["data"][0]["parkCode"],
            "desc": data["data"][0]["description"],
            "act": data["data"][0]["activities"],
            "imgs": data["data"][0]["images"]
        }
    return park


def state_search(state_code):
    url = 'https://developer.nps.gov/api/v1/parks?stateCode={}&api_key={}'.format(state_code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()

    parks = []
  
    for i in range(len(data["data"])):
        park = {
            "name": data["data"][i]["fullName"],
            "code": data["data"][i]["parkCode"],
            "desc": data["data"][i]["description"],
            "act": data["data"][i]["activities"],
            "imgs": data["data"][i]["images"]
        }

        #names = names.split("\r\n")
        '''park_names.append(name)
        park_codes.append(code)
        park_descs.append(desc)'''
        parks.append(park)
        #text = '{} \r\n'.format(names)
    
    
    return parks

def get_acts():
    url = 'https://developer.nps.gov/api/v1/activities?api_key={}'.format(api_key)   
    response = requests.get(url, verify=False)
    data = response.json()
    acts = []

    for i in range(len(data["data"])):
        act = {
            "name": data["data"][i]["name"],
            "id": data["data"][i]["id"]
        }
        acts.append(act)

    return acts

def act_search(id):
    url = 'https://developer.nps.gov/api/v1/activities/parks?id={}&limit=10&api_key={}'.format(id, api_key)   
    response = requests.get(url, verify=False)
    data = response.json()
    parks = []
    if data["data"]:
        for i in range(len(data["data"][0]['parks'])):
            park = data["data"][0]['parks'][i]["parkCode"]
            parks.append(park)

    return parks , data["data"][0]['name']





def park_total(code):
    url = 'https://developer.nps.gov/api/v1/parks?stateCode={}&api_key={}'.format(code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()
    if len(data["data"]) == 0:
        res = 'Please enter a valid state'
    else:     
        res = 'There are a total of {} parks in {}'.format(len(data["data"]), get_state_name(code))

    return (res)

def cli_test(code):
    parks = park_search(code)
    print(parks)
