import requests, json
from util import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

global api_key
global park
global webcams

api_key='mKq6LYmilSkfmzGIDcWpkT84kTmhUTgmnd2ytocs'

def park_search(park_code):
    url = 'https://developer.nps.gov/api/v1/parks?parkCode={}&api_key={}'.format(park_code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()
    park ={}

    for i in range(len(data["data"])):
        park = {
            "name": data["data"][0]["fullName"],
            "code": data["data"][0]["parkCode"],
            "desc": data["data"][0]["description"],
            "act": data["data"][0]["activities"],
            "imgs": data["data"][0]["images"],
            "state": data["data"][0]["states"],
            "contacts": data["data"][0]["contacts"],
            "addresses": data["data"][0]["addresses"],
            "webcams": webcam_search(data["data"][0]["parkCode"])
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
            "imgs": data["data"][i]["images"],
            "states": data["data"][i]["states"],
            "addresses": data["data"][0]["addresses"],
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

def act_search(id, limit=10):
    url = 'https://developer.nps.gov/api/v1/activities/parks?id={}&limit=10&api_key={}'.format(id, api_key)   
    response = requests.get(url, verify=False)
    data = response.json()
    parks = []
    if data["data"]:
        if limit < len(data["data"][0]['parks']):
            for i in range(limit):
                code = data["data"][0]['parks'][i]["parkCode"]
                park = park_search(code)
                parks.append(park)
        else:
            for i in range(len(data["data"][0]['parks'])):
                code = data["data"][0]['parks'][i]["parkCode"]
                park = park_search(code)
                parks.append(park)
        

    return parks, data["data"][0]['name']



def park_total(parks, code):
    if len(parks) == 0:
        res = 'Please enter a valid state'
    else:     
        res = 'There are a total of {} parks in {}'.format(len(parks), get_state_name(code))

    return (res)


def webcam_search(park_code):
    url = 'https://developer.nps.gov/api/v1/webcams?parkCode={}&api_key={}'.format(park_code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()
    webcams = []

    for i in range(len(data["data"])):
        webcam = {
            "title": data["data"][i]["title"],
            "url": data["data"][i]["url"],
            "desc": data["data"][i]["description"],
            "imgs": data["data"][i]["images"]
        }
        webcams.append(webcam)
        
    return webcams

#print(act_search('071BA73C-1D3C-46D4-A53C-00D5602F7F0E'))

#print(park_search('acad')['contacts']['phoneNumbers'])
for num in park_search('acad')['contacts']['phoneNumbers']:
    print(num['phoneNumber'],num['type'] )