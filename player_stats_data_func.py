import requests
from bs4 import BeautifulSoup
import re
import json

CONV_TEAM_NAME_JPN_TO_ENG = {"T.T彩たま":"tt-saitama",
                    "木下マイスター東京":'kinoshitameister-tokyo',
                    "岡山リベッツ":'okayama-rivets',
                    "琉球アスティーダ":'ryukyu-asteeda',
                    "トップおとめピンポンズ名古屋":"top-nagoya",
                    "日本生命レッドエルフ":"nissay-redelf",
                    "日本ペイントマレッツ":"nipponpaint-mallets",
                    "木下アビエル神奈川":"kinoshitaabyell-kanagawa"
                    }


def get_player_link(season):
    player_list_url = []
    for sex in ("m", "w"):
        url = "https://tleague.jp/standings/player/?mw={}&season={}".format(sex, season)
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        matchlist = soup.find(class_="ui-standings-table")
        for a in matchlist.find_all("a"):
            link = a.get("href")
            if link[:6] == "/stats":
                player_list_url.append(link)
    return player_list_url

def get_player_data(url):
    player_data_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    item_charts = soup.find_all(class_="item-chart")
    name = get_name(soup)
    team = get_team(soup)
    stats_data = get_stats_data(soup)
    charts_data = []
    for idx, item_chart in enumerate(item_charts):
        if idx > 5:
            break
        script = item_chart.find("script").get_text()
        if idx == 3:
            charts_data.append(get_cahtsjs_labels_text(script))
        else:
            charts_data.append(get_chartjs_data_text(script))
    return name, team, stats_data, charts_data

def get_chartjs_data_text(script):
    script = re.sub("\s","", script)
    script = re.search("data:\{.*\},", script)
    data = script.group()
    data = re.findall("data:\[.*?\],", data)
    for i in range(len(data)):
        data[i] = data[i][6:-2]
    ret = []
    for i in data:
        tmp = i.split(",")
        ret.append([int(re.search("\d{1,10000}", t).group()) if t != '' else 0 for t in tmp])
    return ret

def get_name(soup):
    head_stats = soup.find(class_="head-stats")
    name = head_stats.find(class_="reset")
    name = name.get_text()
    name = re.sub("[^a-zA-Z\s]", "", name)
    return name.strip()

def get_team(soup):
    spec_stats = soup.find(class_="spec-stats")
    btag = spec_stats.find("b")
    return CONV_TEAM_NAME_JPN_TO_ENG[btag.get_text()]

def get_cahtsjs_labels_text(script):
    script = re.sub("\s","", script)
    labels = re.search("labels:\[.*],datasets", script)
    labels = labels.group()[:-8]
    labels = re.sub("5連続ポイント", "", labels)
    data = re.findall("[0-9\.]{1,10000}", labels)
    ret = []
    for i in data:
        if i[0] == ".":
            i = "0" + i
        ret.append(float(i))
    return ret

def get_stats_data(soup):
    ui_total_stats = soup.find(class_="ui-total-stats")
    ui_total_stats = ui_total_stats.find_all("li")
    ret = []
    for i in ui_total_stats:
        ret.append(i.find("div").get_text())
    ui_sub_stats = soup.find(class_="ui-sub-stats")
    ui_sub_stats = ui_sub_stats.find_all("b")
    for i in ui_sub_stats:
        ret.append(i.get_text())
    return ret