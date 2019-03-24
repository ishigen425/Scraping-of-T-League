import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from game_data_func import get_game_recorde,get_link,get_match_recorde,get_point_record

conn = mysql.connector.connect(
    host = '172.17.0.3',#localhost
    port = 3306,
    user = '',
    password = '',
    database = 'TLeagu',
)

cur = conn.cursor()

basicurl = "https://tleague.jp"
link = get_link()
# link = ["/match/20181024m01"]
try:
    cur.execute("DELETE FROM team_match;")
    cur.execute("DELETE FROM game;")
    cur.execute("DELETE FROM point;")
    for i in link:
        url = basicurl + i
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        sex = 0 if i[-3] == "m" else 1
        date = i[-11:-3]
        match_id = i[7:]
        all_match = get_match_recorde(soup)
        all_match_game = get_game_recorde(soup)
        all_match_point, all_match_timeout, all_match_serve = get_point_record(soup)
        
        # inesrt match table
        execute_str = "INSERT INTO team_match VALUES ('{}','{}','{}','{}',{},{},{},{});".format(
            match_id, date, all_match[0], all_match[1], int(all_match[2]), int(all_match[3]), int(all_match[4]), int(sex)
        )
        cur.execute(execute_str)

        # insert game table
        for a_game_index, a_game in enumerate(all_match_game):
            if a_game[1] != None:
                execute_str = "INSERT INTO game VALUES ('{}',{},'{}','{}','{}','{}',{},{});".format(
                    match_id, a_game_index, a_game[0], a_game[1], a_game[2], a_game[3], int(a_game[4]), int(a_game[5])
                )
            else:
                execute_str = "INSERT INTO game VALUES ('{}',{},'{}',NULL,'{}',NULL,{},{});".format(
                    match_id, a_game_index, a_game[0], a_game[2], int(a_game[4]), int(a_game[5])
                )
            cur.execute(execute_str)

        # insert point table
        for a_match_point_index, a_match_point in enumerate(all_match_point):
            for a_set_point_index, a_set_point in enumerate(a_match_point):
                for a_point_index, a_point in enumerate(a_set_point):
                    execute_str = "INSERT INTO point VALUES ('{}',{},{},{},{},{},{},{});".format(
                        match_id, a_match_point_index, a_set_point_index, a_point_index,
                        int(a_point), int(all_match_serve[a_match_point_index][a_set_point_index][a_point_index]),
                        all_match_timeout[a_match_point_index][a_set_point_index][a_point_index][0],
                        all_match_timeout[a_match_point_index][a_set_point_index][a_point_index][1]
                    )
                    cur.execute(execute_str)
except:
    print(all_match)
    print(all_match_game)
    print(all_match_point)
    conn.rollback()
    raise

conn.commit()