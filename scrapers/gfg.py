import requests
from bs4 import BeautifulSoup

# Scraping GFG Contest Data
def get_gfg_contests():
    url = 'https://practice.geeksforgeeks.org/contest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    contests = []

    for contest in soup.find_all('div', class_='contest-title'):
        contests.append(contest.get_text())

    return contests