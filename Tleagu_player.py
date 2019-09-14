import csv
import requests
from bs4 import BeautifulSoup
import re
import sys, traceback
from player_data_func import get_team_link, get_player_data, get_player_link

SEASON = "2019"
BASIC_URL = "https://tleague.jp"

def main():
    link = get_team_link()
    try:
        player_table = make_table(link)
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t,v,tb))
        print(traceback.format_tb(e.__traceback__))
    finally:
        export_csv(player_table)

def make_table(link):
    player_table = []
    for i in link:
        url = BASIC_URL + i + "player/"
        season = "?season=" + SEASON
        player_list_url = get_player_link(url + season)
        for player_index, player_url in enumerate(player_list_url):
            player_url = url + player_url 
            print(player_url)
            player_data = get_player_data(player_url)
            player_table.append([
                season[len(season)-4:],player_data[0].strip(), i[6:-1], player_data[1].strip(), player_data[2], 
                player_data[3], player_data[4].replace("\t", " ").strip(), player_data[5] or 'NULL', player_data[6] or 'NULL'
            ])

    return player_table

def export_csv(player_table):
    player_header = ["season", "player_name", "team_name", "type", "birthday", "height", "birthplace", "latest_world_rank", "highest_world_rank"]
    with open('./data/player_table.csv' ,'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(player_header)
        writer.writerows(player_table)

if __name__ == '__main__':
    main()
