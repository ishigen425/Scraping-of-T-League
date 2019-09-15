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
Tleagu_game.py 2018
```
選手データのcsvファイルの出力は以下のコマンドです。
こちらは2019年に登録されている選手のみとなります。
```
Tleagu_player.py
```
個人スタッツはまだ取得できません。対応する予定です。

それぞれのcsvファイルの説明をします。

## Tleagu_game.pyから出力されるファイル
* match_table_{シーズン}.csv  
文字コード:utf-8  
カラム  
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
カラム  
season:選手登録されているシーズン  
player_name:選手名  
team_name:所属チーム  
type:戦型  
birthday:生年月日  
height:身長  
birthplace:出身地  
latest_world_rank:最新世界ランク  
highest_world_rank:最高世界ランク  

