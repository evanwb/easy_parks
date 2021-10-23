import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

url = 'localhost:3030/parse_data'

def read_input() 
    response = requests.get(url, verify=False)
    data = response.json()
    print(data.items())


def print_json(input_obj):
    res = json.dumps(input_obj, sort_keys=True, indent=5)
    print(res)
    




