import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from player_data_func import get_team_link, get_player_data, get_player_link

conn = mysql.connector.connect(
    host = '172.17.0.4',#localhost
    port = 3306,
    user = '',
    password = '',
    database = 'TLeagu',
)

cur = conn.cursor()

basicurl = "https://tleague.jp"
link = get_team_link()
try:
    cur.execute("DELETE FROM player;")
    for i in link:
        url = basicurl + i + "player/"
        player_list_url = get_player_link(url)
        for player_index, player_url in enumerate(player_list_url):
            player_url = url + player_url 
            player_data = get_player_data(player_url)
            execute_str = "INSERT INTO player VALUES ('{}','{}','{}',{},{},'{}',{},{});".format(
                player_data[0].strip(), i[6:-1], player_data[1].strip(), player_data[2], player_data[3], 
                player_data[4].strip(), player_data[5] or 'NULL', player_data[6] or 'NULL'
            )
            cur.execute(execute_str)
except:
    conn.rollback()
    raise

conn.commit()
