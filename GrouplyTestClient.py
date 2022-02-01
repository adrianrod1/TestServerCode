#!/usr/bin/env python3

import requests

# This client is intended to test receiving a request from the iOS API since I can't get past the cert issues on xcode. 
# For now this will simulate requests from the app.

# importing the requests library

  
# api-endpoint
URL = "https://127.0.0.1:61617/CreateNewProfile"
  
# # location given here
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}
userRequest =  '{"request": "CreateNewProfile", "id": "01","FirstName": "Adrian","LastName": "Rodriguez","UserName": "adrian_rod"}'

  
# sending get request and saving the response as response object
try: 
    r = requests.post(url = URL, json=userRequest, verify=False)
    # extracting data in json format
    data = r .json()
    print(data)
except requests.exceptions.RequestException as e:
    print("ERROR")
    print(e)


  
  