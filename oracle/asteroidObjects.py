import requests
import json

def asteroidOrbit(year, orbitclass):
    url = f"https://jsonmock.hackerrank.com/api/asteroids/search?page={1}"

    result = requests.get(url)
    response = json.loads(result.content)

    total_pages = response['total_pages']

    curr_page = 1

    asteroid_designations = []

    while curr_page <= total_pages:
        url = f"https://jsonmock.hackerrank.com/api/asteroids/search?page={curr_page}"
        result = requests.get(url)
        response = json.loads(result.content)


        for i in response['data']:
            if str(year) == i['discovery_date'][:4] and orbitclass.lower() in i['orbit_class'].lower(): 
                if i.get("period_yr") == None or i.get("period_yr") == '':
                    i['period_yr'] = 1
                i['period_yr'] = float(i['period_yr'])
                asteroid_designations.append(i)
        curr_page += 1


    asteroid_designations.sort(key=lambda x : (x["period_yr"],x["designation"]))

    return [asteroid['designation'] for asteroid in asteroid_designations]

# Example usage
year_of_discovery = 2010
orbit_class_keyword = "aten"
result = asteroidOrbit(year_of_discovery, orbit_class_keyword)
print(result)
