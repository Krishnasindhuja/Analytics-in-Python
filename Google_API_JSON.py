#working with google API and dealing with JSON data 

import json 

address = "Columbia University, New york, NY"
url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % address 

try: 
    response = requests.get(url)
    if not response.status_code ==200 :
        print("HTTP error", response.status_code)
    else:
        try:
            response_data = response.json()
        except:
            print("Invalid JSON format")
except:
    print("Something wrong with response")
    
#response_data['results'][0]

for types in response_data['results'][0]:
    print(types)
    

latitude = response_data['results'][0]['geometry']['location']['lat']
longitude = response_data['results'][0]['geometry']['location']['lng']
print(latitude, longitude)
