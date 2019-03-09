CREATE DATABASE TLeagu;

CREATE TABLE team_match (
match_id VARCHAR(20) ,
date DATE ,
home VARCHAR(100) ,
away VARCHAR(100) ,
home_point INT ,
away_point INT ,
visitors INT ,
sex INT ,
PRIMARY KEY(match_id)
);

CREATE TABLE game (
match_id VARCHAR(20) ,
game_id INT ,
home_player1 VARCHAR(100) ,
home_player2 VARCHAR(100) ,
away_player1 VARCHAR(100) ,
away_player2 VARCHAR(100) ,
home_point INT ,
away_point INT ,
PRIMARY KEY(match_id,game_id)
);

CREATE TABLE point (
match_id VARCHAR(20) ,
game_id INT ,
set_id INT ,
point_id INT ,
point INT ,
serve INT ,
home_timeout_fag INT ,
away_timeout_fag INT ,
PRIMARY KEY(match_id,game_id,set_id,point_id)
);