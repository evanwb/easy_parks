import requests, json
from util import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

global api_key
global parks

api_key='pQNtyh3wP65oZT5zeLWTMAIRTHTEnTCQE1nRHz9L'

def park_search(park_code):
    url = 'https://developer.nps.gov/api/v1/parks?parkCode={}&api_key={}'.format(park_code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()

    for i in range(len(data["data"])):
        park = {
            "name": data["data"][0]["fullName"],
            "code": data["data"][0]["parkCode"],
            "desc": data["data"][0]["description"],
            "act": data["data"][0]["activities"]
        }
    return park




def state_search(state_code):
    url = 'https://developer.nps.gov/api/v1/parks?stateCode={}&api_key={}'.format(state_code,api_key)
    response = requests.get(url, verify=False)
    data = response.json()

    park_names = []
    park_codes = []
    park_descs = []
    park_acts = []
    parks = []
  
    for i in range(len(data["data"])):
        park = {
            "name": data["data"][i]["fullName"],
            "code": data["data"][i]["parkCode"],
            "desc": data["data"][i]["description"],
            "act": data["data"][i]["activities"]
        }

        #names = names.split("\r\n")
        '''park_names.append(name)
        park_codes.append(code)
        park_descs.append(desc)'''
        parks.append(park)
        #text = '{} \r\n'.format(names)
    
    
    return parks
    #return list(zip(park_names,park_codes,park_descs,park_acts))


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

    '''for park in parks:
        print('{}\r'.format(park['name']))
        print('{}\r'.format(park['code']))
        print('{}\r'.format(park['desc']))
        acts = park['act']
        for act in acts:
            print(act['name'])'''
    print('\r\n')

#cli_test(input('code'))