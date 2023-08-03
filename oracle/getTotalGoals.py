import requests
import json

def getTotalGoals(team, year):
    # Write your code here
    
    url1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}'
    url2 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}'
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    
    #convert dicts into json
    result1 = json.loads(response1.content)
    result2 = json.loads(response2.content)
    
    numberOfPages1 = result1['total_pages']
    numberOfPages2 = result2['total_pages']
    
    curr_page1 = 1
    curr_page2 = 1
    
    total_goals = 0
    while curr_page1 <= numberOfPages1:
        url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={curr_page1}'
        
        response = requests.get(url)
        result = json.loads(response.content)
        
        for i in result['data']:
            total_goals += int(i['team1goals'])
        curr_page1 += 1
        
    while curr_page2 <= numberOfPages2:
            url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={curr_page2}'
            
            response = requests.get(url)
            result = json.loads(response.content)
            
            for i in result['data']:
                total_goals += int(i['team2goals'])
            curr_page2 += 1
            
    return total_goals




