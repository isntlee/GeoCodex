import json


counties = ['carlow','cavan','clare','cork','donegal','dublin',
'galway','kerry','kildare','kilkenny','laois','leitrim','limerick',
'longford','louth','mayo','meath','monaghan','offaly','roscommon',
'sligo','tipperary','waterford','westmeath','wexford','wicklow']



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



coordinates_popcentres_list = []
popcentres_list = []
with open('popCentres.geojson', 'r') as f:
    data = json.load(f)
    for popcentre_detail in data['features']:
        popcentres = popcentre_detail['properties']['English_Name'].lower()
        coords = popcentre_detail['geometry']['coordinates']
        coordinates_popcentres_list.append(coords)
        popcentres_list.append(popcentres)



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

            print("\nLevel of Precision: low")
            print(county_coordinates,"      -     County:",str(single_address[-1]).capitalize())

            if single_address[-2] in popcentres_list:
                popcentreID = (popcentres_list.index(single_address[-2]))
                popcentre_coordinates = coordinates_popcentres_list[popcentreID]

                print("\nLevel of Precision: medium")
                print(popcentre_coordinates,"      -     Town:",str(single_address[-2]).capitalize())

        else:
            Error += 1 
            print("\nError, no working address found\n")
        

    print("\nSuccessful:",Success,"| Errors:",Error)