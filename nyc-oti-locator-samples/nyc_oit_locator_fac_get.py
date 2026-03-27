#Python script for using the NYC OTI Locator REST API

import requests

url = "https://api.nyc.gov/arcgis/rest/services/NYC_OTI_Locator/GeocodeServer/findAddressCandidates"


#put your subscription key between the quotes below
#obtain a subscription key by signing up at this website here:
#https://api-portal.nyc.gov/api-details#api=arcgis-enterprise&operation=Root
headers = {
    "Ocp-Apim-Subscription-Key": ""
}    

params = {
    "f": "json",
    "outFields": "*",
    "singleLine": "500 7th Ave, New York, NY 10018"
}

get_response = requests.get(url, headers=headers, params=params)

print(f"GET Status Code: {get_response.status_code}")
print(f"GET Response: {get_response.json()}")
