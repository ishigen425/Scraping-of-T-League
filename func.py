import requests
from bs4 import BeautifulSoup
import re

basicurl = "https://tleague.jp/match/"

def get_link():
  link_list = []
  for month in ["201810","201811","201812","201901","201902"]:
    url = basicurl + "?season=2018&month=" + month + "&mw="
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
  home = 0
  away = 0
  if is_final:
    home = 6
    away = 6
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
  match = []
  match_serve = []
  match_timeout = []
  home_timeout, away_timeout = 0, 0
  is_final = False
  for i in soup.find_all("div",class_="match-game"):
    game = []
    game_serve = []
    game_timeout = []
    for w in i.find_all(class_="wrap-table"):
      point = []
      serve = []
      timeout = []
      tmp = ""
      for k_ind,k in enumerate(w.find_all("td")):
        if k_ind == 0:
          if k.get_text() == "1" or k.get_text() == "0":
            point.append(k.get_text())
          else:
            point.append(str(int(k.get_text()) - 6))
            is_final = True
        else:
          if k.get_text() == "T":
              home_timeout = 1
              continue
          elif re.match("[0-9]", k.get_text()) == None:
              away_timeout = 1
              continue
          elif tmp == k.get_text():
            point.append("0")
          else:
            point.append("1")
        timeout.append([home_timeout, away_timeout])
        home_timeout, away_timeout = 0, 0
        tmp = k.get_text()
        if k.get("class") != None:
          serve.append(1)
        else:
          serve.append(2)

        if judge_end_set(point, is_final):
          is_final = False
          game.append(point)
          game_serve.append(serve)
          game_timeout.append(timeout)
          break
    match.append(game)
    match_timeout.append(game_timeout)
    match_serve.append(game_serve)

  return match, match_timeout, match_serve

