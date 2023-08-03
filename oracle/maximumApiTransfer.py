import requests
import json


def maxApiTransfer():
    url = "https://jsonmock.hackerrank.com/api/transactions"
    result = requests.get(url)
    response = json.loads(result.content)

    total_pages = response['total_pages']
    curr_page = 1

    while curr_page <= total_pages:
        url1 = f"{url}?page={curr_page}"
        response = requests.get(url1)
        result = json.loads(response.content)

        for i in result['data']:
            
