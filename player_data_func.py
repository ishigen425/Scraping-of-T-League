import requests
from bs4 import BeautifulSoup
import re

def get_team_link():
    team_list_url = "https://tleague.jp/team/"
    team_list = []
    response = requests.get(team_list_url)
    soup = BeautifulSoup(response.text, "html.parser")
    matchlist = soup.find(class_="nav-team")
    for a in matchlist.find_all("a"):
        team_list.append(a.get("href"))

    return team_list

def get_player_link(team_url):
    player_list_url = []
    response = requests.get(team_url)
    soup = BeautifulSoup(response.text, "html.parser")
    matchlist = soup.find(class_="main")
    for a in matchlist.find_all("a"):
        player_list_url.append(a.get("href"))
    return player_list_url


def parse_date(date):
    birth = date
    birth = birth[5:]
    year = birth[:4]
    birth = birth[5:]
    month = birth[:2]
    day = birth[2:]
    month = re.sub("\D", "", month) if len(re.sub("\D", "", month)) == 2 else "0" + re.sub("\D", "", month)
    day = re.sub("\D", "", day) if len(re.sub("\D", "", day)) == 2 else "0" + re.sub("\D", "", day)
    return year + month + day

def get_player_data(player_url):
    player_data_list = []
    response = requests.get(player_url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find(class_="ttl-heavy")
    name = name.find("span")
    player_data_list.append(name.get_text().strip())
    matchlist = soup.find(class_="profile-player")
    for index, li in enumerate(matchlist.find_all("li")):
        if index in [2,3,4,5,8,9]:
            player_data_list.append(li.get_text())
    for index, li in enumerate(player_data_list):
        if index in [1]:
            value = li[3:]
        elif index in [2]:
            value =  parse_date(li)
        elif index in [3]:
            pattern = "\D"
            value = re.sub(pattern, "", li)
            if len(value) == 4: value = value[:3]
        elif index in [4]:
            value = li[4:]
        elif index in [5]:
            value = re.sub(pattern, "", li)
        elif index in [6]:
            value = re.sub(pattern, "", li[:len(li)-9])
        else:
            value = li
        player_data_list[index] = value
    return player_data_list
