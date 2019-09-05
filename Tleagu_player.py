import csv
import requests
from bs4 import BeautifulSoup
import re
from player_data_func import get_team_link, get_player_data, get_player_link

def main():
    SEASON = "2019"
    BASIC_URL = "https://tleague.jp"
    link = get_team_link()
    player_table = []
    try:
        for i in link:
            url = basicurl + i + "player/"
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
    except:
        raise
    finally:
        player_header = ["season", "player_name", "team_name", "type", "birthday", "height", "birthplace", "latest_world_rank", "highest_world_rank"]
        with open('./data/player_table.csv' ,'w', encoding='utf-8') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(player_header)
            writer.writerows(player_table)

if __name__ == '__main__':
    main()
