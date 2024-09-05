import requests
from bs4 import BeautifulSoup

def get_codechef_contests():
    url = 'https://www.codechef.com/contests'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    contests = []

    for contest in soup.find_all('table', class_='dataTable'):
        contests.append(contest.get_text())

    return contests
