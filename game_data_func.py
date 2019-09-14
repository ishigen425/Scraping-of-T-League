import requests
from bs4 import BeautifulSoup
import re

BASIC_URL = "https://tleague.jp/match/"

def get_link(season, months):
  link_list = []
  for month in months:
    url = BASIC_URL + "?season=" + season + "&month=" + month + "&mw="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    matchlist = soup.find(class_="ui-match-table")
    for i in matchlist.find_all(class_="match-men"):
      for inner in i.find_all(class_="inner"):
        link = inner.find("a").get("href")
        link_list.append(link)
    for i in matchlist.find_all(class_="match-women"):
      for inner in i.find_all(class_="inner"):
        link = inner.find("a").get("href")
        link_list.append(link)

  return link_list


def get_match_recorde(soup):
  match = soup.find(class_="match-info")
  home = match.find(class_="home").get_text()
  away = match.find(class_="away").get_text()
  point = match.find_all(class_="cell-score")
  home_point = point[0].get_text()
  away_point = point[1].get_text()
  itemclass = match.find(class_="item-spec").find_all("li")
  visitors = itemclass[2].get_text()
  visitors = re.sub(r"[^0-9]", "", visitors)

  return [home, away,home_point, away_point, visitors]


def get_game_recorde(soup):
  table = []
  match = soup.find(class_="cell-game")
  home_point = 0
  away_point = 0
  game = []
  for i, col in enumerate(match.find_all(class_="col")):
    if i % 3 == 1:
        # point col
        home_point = col.get_text()[0]
        away_point = col.get_text()[2]
        continue
    a_list = col.find_all("a")
    if len(a_list) >= 2:
        for a in a_list:
            game.append(a.get_text().replace("\n",""))
    else:
        for a in a_list:
            game.append(a.get_text().replace("\n",""))
            game.append(None)
    if i % 3 == 2:
      # reset
      game.append(home_point)
      game.append(away_point)
      table.append(game)
      game = []

  return table

def judge_end_set(point, is_final):
  home, away = 0, 0
  if is_final:
    home, away = 6, 6
  for i in point:
    if i == "1":
      home += 1
    else:
      away += 1
      
    if home >= 11 or away >= 11:
      if (home - away) ** 2 >= 4:
        return True
      
  return False

def get_point_record(soup):
  match, match_serve, match_timeout = [], [], []
  for i in soup.find_all("div",class_="match-game"):
    game, game_timeout, game_serve = [], [], []
    for w_idx, w in enumerate(i.find_all(class_="wrap-table")):
      point, serve, timeout = [], [], []
      for k_idx,k in enumerate(w.find_all("td")):
        txt = k.get_text()
        class_list = k.get("class")
        if txt == '':
          continue
        if class_list != None and "timeout" in class_list:
          timeout.append(1)
          continue
        if class_list != None and "serve" in class_list:
          serve.append(1)
        else:
          serve.append(2)
        point.append(txt)
        timeout.append(0)
      # game
      game_serve.append(serve[:len(serve)])
      game_tmp, game_timeout_tmp = convGameArray(point, timeout)
      game.append(game_tmp)
      game_timeout.append(game_timeout_tmp)

    match.append(game)
    match_timeout.append(game_timeout)
    match_serve.append(game_serve)

  return match, match_timeout, match_serve

def convGameArray(point, timeout):
  num_point = []
  for i, v in enumerate(point):
    if re.match("[0-9]", v):
      num_point.append(v)
  rally_cnt = len(num_point)//2
  ret_timeout = [0] * rally_cnt
  
  cnt = 0
  for i, v in enumerate(timeout):
    if v > 0:
      if i <= rally_cnt + cnt:
        ret_timeout[i] = 1
      else:
        ret_timeout[i-rally_cnt-cnt] = 2
      cnt += 1

  ret = []
  home = num_point[:rally_cnt]
  away = num_point[rally_cnt:]
  for i in range(rally_cnt):
    ret.append(home[i] + " " + away[i])
  return ret, ret_timeout