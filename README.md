# Scraping of TLeague

## 動作環境
python 3.6  
各ライブラリは以下のコマンドを実行
```
pip install -r requirements.txt
```

## 利用方法

試合データのcsvファイルの出力は以下のコマンドです。第一引数でシーズンを表す引数として、"2018"もしくは"2019"を入力してください。
```
python Tleagu_game.py 2018
```
選手データのcsvファイルの出力は以下のコマンドです。
こちらは2019年に登録されている選手のみとなります。
```
python Tleagu_player.py
```
個人スタッツの取得は以下のコマンドです。引数は"2018"もしくは"2019"です。
```
python Tleagu_player_stats.py 2018
```

それぞれのcsvファイルの説明をします。

## Tleagu_game.pyから出力されるファイル
* match_table_{シーズン}.csv  
文字コード:utf-8  
match_id:チームマッチのID URLの後方文字列  
date:試合日  
home:ホームのチーム  
away:アウェーのチーム  
home_point:ホームチームの勝利ゲーム数  
away_point:アウェーチームの勝利ゲーム数  
visitors:観客数  
sex:性別  

* game_table_{シーズン}.csv  
文字コード:utf-8  
match_id:チームマッチのID  
game_id:各マッチのインデックス番号  
home_player1:ホームチームの選手名  
home_player2:ホームチームの選手名（シングルスの場合は未設定）  
away_player1:アウェーチームの選手名  
away_player2:アウェーチームの選手名（シングルスの場合は未設定）  
home_point:ホームチームの獲得ゲーム数  
away_point:アウェーチームの獲得ゲーム数  

* point_table_{シーズン}.csv  
文字コード:utf-8  
match_id:チームマッチのID  
game_id:各マッチのインデックス番号  
set_id:各セットのインデックス番号  
point_id:各ポイントのインデックス番号  
home_point:ホームチームの獲得ポイント  
away_point:アウェーチームの獲得ポイント  
serve:サーブ権 1:ホームチーム、2:アウェーチーム  
timeout:タイムアウト 1:ホームチームのタイムアウト直後のポイント 2:アウェーチームのタイムアウト直後のポイント  


## Tleagu_player.pyから出力されるファイル
* player_table.csv  
文字コード:utf-8  
season:選手登録されているシーズン  
player_name:選手名  
team_name:所属チーム  
type:戦型  
birthday:生年月日  
height:身長  
birthplace:出身地  
latest_world_rank:最新世界ランク  
highest_world_rank:最高世界ランク  

## Tleagu_player_stats.pyから出力されるファイル
* player_table.csv  
文字コード:utf-8  
season:シーズン  
player_name:選手名  
team_name:所属チーム  
match_number:試合数  
VM_match_number:VM試合数  
win_match:勝利数  
lose_match:敗戦数  
win_game:獲得ゲーム  
lose_game:喪失ゲーム  
shut_out_rate:完封率  
win_point:獲得ポイント  
lose_point:喪失ポイント  
max_continuous_game_get_number:連続最大ゲーム勝利数  
game_time:平均試合時間  
reverse_win_number:逆転勝利数  
reverse_lose_number:逆転敗戦数  
first_game_win_number:第一ゲーム獲得数  
second_game_win_number:第二ゲーム獲得数  
thrid_game_win_number:第三ゲーム獲得数  
forth_game_win_number:第四ゲーム獲得数  
fifth_game_win_number:第五ゲーム獲得数  
first_game_lose_number:第一ゲーム喪失数  
second_game_lose_number:第二ゲーム喪失数  
thrid_game_lose_number:第三ゲーム喪失数  
forth_game_lose_number:第四ゲーム喪失数  
fifth_game_lose_number:第五ゲーム喪失数  
win_game_time_difference_2:勝ちゲーム時点差2点  
win_game_time_difference_3:勝ちゲーム時点差3点  
win_game_time_difference_4:勝ちゲーム時点差4点  
win_game_time_difference_5:勝ちゲーム時点差5点以上  
lose_game_time_difference_2:負けゲーム時点差2点  
lose_game_time_difference_3:負けゲーム時点差3点  
lose_game_time_difference_4:負けゲーム時点差4点  
lose_game_time_difference_5:負けゲーム時点差5点以上  
average_service_ace_number:平均サービスエース数  
average_receive_ace_number:平均レシーブエース数  
average_rally_number:平均ラリー数  
get_points_rate_on_serve:サーブ時ポイント獲得率  
get_points_rate_on_receive:レシーブ時ポイント獲得率  
5_continuous_get_point_game_rate:5連続ポイント取得ゲーム率  
rally_count_at_win_1:サービスエース数  
rally_count_at_win_3:3球目ポイント獲得数  
rally_count_at_win_5:5球目ポイント獲得数  
rally_count_at_win_7:7球目ポイント獲得数  
rally_count_at_win_9:9球目ポイント獲得数  
rally_count_at_win_over_11:11球目以上ポイント獲得数  
rally_count_at_lose_1:サーブミス数  
rally_count_at_lose_3:3球目ポイント喪失率  
rally_count_at_lose_5:5球目ポイント喪失率  
rally_count_at_lose_7:7球目ポイント喪失率  
rally_count_at_lose_9:9球目ポイント喪失率  
rally_count_at_lose_over_11:11球目以上ポイント喪失率  
rally_count_at_win_2:2球目ポイント獲得率  
rally_count_at_win_4:4球目ポイント獲得率  
rally_count_at_win_6:6球目ポイント獲得率  
rally_count_at_win_8:8球目ポイント獲得率  
rally_count_at_win_10:10球目ポイント獲得率  
rally_count_at_win_over_12:12球目以上ポイント獲得率  
rally_count_at_lose_2:2球目ポイント喪失率  
rally_count_at_lose_4:4球目ポイント喪失率  
rally_count_at_lose_6:6球目ポイント喪失率  
rally_count_at_lose_8:8球目ポイント喪失率  
rally_count_at_lose_10:10球目ポイント喪失率  
rally_count_at_lose_over_12:12球目以上ポイント喪失率  

項目が多すぎてわかりにくいですが、このページのグラフの数字を拾っているだけです。合わせて見てもらえればわかるかと思います。  
https://tleague.jp/stats/player/?season=2019&id=10054

