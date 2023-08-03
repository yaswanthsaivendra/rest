import requests
import json

def custom_sort(item):
    country, population = item.split(',')
    return (int(population), country.strip())

def findCountries(region, name):
    url = f"https://jsonmock.hackerrank.com/api/countries/search?region={region}name={name}"

    result = requests.get(url)
    response = json.loads(result.content)

    total_pages = response['total_pages']

    curr_page = 1

    countries = []

    while curr_page <= total_pages:
        url = f"https://jsonmock.hackerrank.com/api/countries/search?region={region}name={name}&page={curr_page}"
        
        result = requests.get(url)
        response = json.loads(result.content)

        for i in response['data']:
            countries.append(f"{i['name']},{i['population']}")

        curr_page += 1

    return sorted(countries, key=custom_sort)


