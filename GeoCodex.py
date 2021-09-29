import json


removables = ['[', ']', '"', "\n", "address\n", ' ', "", "Co."]
def normalize_title(title):
    for remove in removables:
        title = title.replace(remove, '')
    title = title.lower()
    return title


coordinates_counties_geojson = []
with open('counties.geojson', 'r') as f:
    data = json.load(f)
    for county_detail in data['features']:
        county = county_detail['properties']['County'].lower()
        coords = county_detail['geometry']['coordinates']
        coordinates_counties_geojson.append(coords)




counties = ['carlow','cavan','clare','cork',
'donegal','dublin','galway','kerry','kildare','kilkenny',
'laois','leitrim','limerick','longford','louth','mayo','meath','monaghan',
'offaly','roscommon','sligo','tipperary','waterford','westmeath',
'wexford','wicklow']



addresses = []
Success = 0
Error = 0
with open('addresses_for_task.csv', 'r') as f:
    
    for line in f:
        title = normalize_title(line)
        title = title.split(",")
        if len(line) > 10:
            addresses.append(title)

    
    for single_address in addresses: 
        if single_address[-1] in counties:
            Success += 1
            countyID = (counties.index(single_address[-1]))
            county_coordinates = coordinates_counties_geojson[countyID]

        else:
            Error += 1 
            print("\nError, no working address found\n")
        

    print("\nSuccessful:",Success,"| Errors:",Error)