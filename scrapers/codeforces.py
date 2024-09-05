import requests
from bs4 import BeautifulSoup


# Fetching Codeforces Contest Data via API
def get_codeforces_contests():
    url = 'https://codeforces.com/api/contest.list'
    response = requests.get(url)
    data = response.json()

    contests = []
    for contest in data['result']:
        if contest['phase'] == 'BEFORE':
            contests.append(contest['name'])

    return contests