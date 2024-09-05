import requests
from bs4 import BeautifulSoup

def get_leetcode_contests():
    url = 'https://leetcode.com/contest/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    contests = []

    for contest in soup.find_all('div', class_='contest-title'):
        contests.append(contest.get_text())

    return contests
