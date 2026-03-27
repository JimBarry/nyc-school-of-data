#Python script for using the ArcGIS Online GeocodeServer REST API

import requests
from arcgis.gis import GIS
gis = GIS("home")

#paste an ArcGIS API Key below between the quotes
#you can create your own API Key for geocoding by signing up
#for a free ArcGIS Locator Platform account here:
# https://location.arcgis.com/
apiKey = "";

try:
    url = r"https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"

    params = {
        "f": "json",
        "token": apiKey,
        "SingleLine": "500 7th Ave, New York, NY 10018"
    }

    get_response = requests.get(url, params=params)

    print(f"GET Status Code: {get_response.status_code}")
    print(f"GET Response: {get_response.json()}")

except Exception as e:
    print(e)
