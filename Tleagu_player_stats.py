from argparse import ArgumentParser
import csv
import requests
from bs4 import BeautifulSoup
import re
import sys, traceback
from player_stats_data_func import get_player_data, get_player_link

BASIC_URL = "https://tleague.jp"

def parser():
    usage = "UIsage: python '2018 or 2019'"
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('season', type=str, help="2018 or 2019")
    args = argparser.parse_args()
    return args

def main(season):
    link = get_player_link(season)
    # link = ["/stats/player/?id=10012&season=2018"]
    try:
        player_stats_table = make_table(link, season)
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t,v,tb))
        print(traceback.format_tb(e.__traceback__))
        raise
    finally:
        export_csv(player_stats_table, season)

def make_table(link, season):
    player_stats_table = []
    for i in link:
        url = BASIC_URL + i
        print(url)
        name, team, player_stats_data, player_charts_data = get_player_data(url)
        player_stats_table.append([
            season, name, team, 
            player_stats_data[1], player_stats_data[2], player_stats_data[3], player_stats_data[4], player_stats_data[6], player_stats_data[7], player_stats_data[8], player_stats_data[9], player_stats_data[10],
            player_stats_data[11], player_stats_data[12], player_stats_data[13], player_stats_data[14], 
            player_charts_data[0][0][4], player_charts_data[0][0][3], player_charts_data[0][0][2], player_charts_data[0][0][1], player_charts_data[0][0][0],
            player_charts_data[0][1][4], player_charts_data[0][1][3], player_charts_data[0][1][2], player_charts_data[0][1][1], player_charts_data[0][1][0], 
            player_charts_data[1][0][0], player_charts_data[1][0][1], player_charts_data[1][0][2], player_charts_data[1][0][3], 
            player_charts_data[2][0][0], player_charts_data[2][0][1], player_charts_data[2][0][2], player_charts_data[2][0][3], 
            player_charts_data[3][0], player_charts_data[3][1], player_charts_data[3][2], player_charts_data[3][3], player_charts_data[3][4], player_charts_data[3][5], 
            player_charts_data[4][0][0], player_charts_data[4][0][1], player_charts_data[4][0][2], player_charts_data[4][0][3], player_charts_data[4][0][4], player_charts_data[4][0][5], 
            player_charts_data[4][1][0], player_charts_data[4][1][1], player_charts_data[4][1][2], player_charts_data[4][1][3], player_charts_data[4][1][4], player_charts_data[4][1][5], 
            player_charts_data[5][0][0], player_charts_data[5][0][1], player_charts_data[5][0][2], player_charts_data[5][0][3], player_charts_data[5][0][4], player_charts_data[5][0][5], 
            player_charts_data[5][1][0], player_charts_data[5][1][1], player_charts_data[5][1][2], player_charts_data[5][1][3], player_charts_data[5][1][4], player_charts_data[5][1][5]
        ])

    return player_stats_table

def export_csv(player_stats_table, season):
    player_stats_header = ["season", "player_name", "team_name", 
        "match_number", "VM_match_number", "win_match", "lose_match", "win_game", "lose_game", "shut_out_rate", "win_point", "lose_point",
        "max_continuous_game_get_number", "game_time", "reverse_win_number", "reverse_lose_number",
        "first_game_win_number", "second_game_win_number", "thrid_game_win_number", "forth_game_win_number", "fifth_game_win_number",
        "first_game_lose_number", "second_game_lose_number", "thrid_game_lose_number", "forth_game_lose_number", "fifth_game_lose_number", 
        "win_game_time_difference_2", "win_game_time_difference_3", "win_game_time_difference_4", "win_game_time_difference_5", 
        "lose_game_time_difference_2", "lose_game_time_difference_3", "lose_game_time_difference_4", "lose_game_time_difference_5", 
        "average_service_ace_number", "average_receive_ace_number", "average_rally_number", "get_points_rate_on_serve", "get_points_rate_on_receive", "5_continuous_get_point_game_rate",
        "rally_count_at_win_1", "rally_count_at_win_3", "rally_count_at_win_5", "rally_count_at_win_7", "rally_count_at_win_9", "rally_count_at_win_over_11", 
        "rally_count_at_lose_1", "rally_count_at_lose_3", "rally_count_at_lose_5", "rally_count_at_lose_7", "rally_count_at_lose_9", "rally_count_at_lose_over_11", 
        "rally_count_at_win_2", "rally_count_at_win_4", "rally_count_at_win_6", "rally_count_at_win_8", "rally_count_at_win_10", "rally_count_at_win_over_12", 
        "rally_count_at_lose_2", "rally_count_at_lose_4", "rally_count_at_lose_6", "rally_count_at_lose_8", "rally_count_at_lose_10", "rally_count_at_lose_over_12", 
        ]
    with open('./data/player_stats_table_{}.csv'.format(season) ,'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(player_stats_header)
        writer.writerows(player_stats_table)

if __name__ == '__main__':
    parser()
    season = sys.argv[1]
    main(season)
