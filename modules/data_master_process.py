##? not sure what this is ... 
from numpy.core.numeric import True_

import pandas as pd
import numpy as np


## this function gives detailed info on NaN values of input df
from data_clean import perc_null

#these functionas add a date column (x2) and correct mp season format
from data_fix_dates import game_add_mp_date, bet_add_mp_date,  fix_mp_season 

#these functions assign nhl_names eg 'NYR' to bet, mp, and game; 
# functions use simple dictionaries

from data_fix_team_names import bet_to_nhl, mp_to_nhl, game_to_nhl

##these are two different functions for assigning game_id to df_betting, based on team, date, H/A
##one uses df_game as look up table ... other uses df_mp_teams as look up table
from data_bet_add_game_id import mp_to_bet_add_game_id, game_to_bet_add_game_id


##import all the files 

##file paths

Kaggle_path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/Data/Kaggle_Data_Ellis/"
mp_path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/Data/Money_Puck_Data/"
betting_path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/Data/Betting_Data/"

#Kaggle_path = "/Users/joejohns/data_bootcamp/Final_Project_NHL_prediction/Data/Kaggle_Data_Ellis/"
#mp_path = "/Users/joejohns/data_bootcamp/Final_Project_NHL_prediction/Data/Money_Puck_Data/"
#betting_path = "/Users/joejohns/data_bootcamp/Final_Project_NHL_prediction/Data/Betting_Data/"

##Kaggle files

df_game = pd.read_csv(Kaggle_path+'game.csv')
df_game_team_stats = pd.read_csv(Kaggle_path+'game_teams_stats.csv')
df_game_skater_stats = pd.read_csv(Kaggle_path+'game_skater_stats.csv')
df_game_goalie_stats = pd.read_csv(Kaggle_path+'game_goalie_stats.csv')

##more subtle Kaggle features:
df_game_scratches = pd.read_csv(Kaggle_path+'game_scratches.csv')
df_game_officials = pd.read_csv(Kaggle_path+'game_officials.csv')
df_team_info = pd.read_csv(Kaggle_path+'team_info.csv')

## grab all the moneypuck data 

df_mp_teams = pd.read_csv(mp_path+'all_teams.csv')


## grab all betting data 
df1 = pd.read_excel(io = betting_path+'nhl odds 2007-08.xlsx')
df2 = pd.read_excel(io = betting_path+'nhl odds 2008-09.xlsx')
df3 = pd.read_excel(io = betting_path+'nhl odds 2009-10.xlsx')
df4 = pd.read_excel(io = betting_path+'nhl odds 2010-11.xlsx')
df5 = pd.read_excel(io = betting_path+'nhl odds 2011-12.xlsx')
df6 = pd.read_excel(io = betting_path+'nhl odds 2012-13.xlsx')
df7 = pd.read_excel(io = betting_path+'nhl odds 2013-14.xlsx')
df8 = pd.read_excel(io = betting_path+'nhl odds 2014-15.xlsx')
df9 = pd.read_excel(io = betting_path+'nhl odds 2015-16.xlsx')
df10 = pd.read_excel(io = betting_path+'nhl odds 2016-17.xlsx')
df11 = pd.read_excel(io = betting_path+'nhl odds 2017-18.xlsx')
df12 = pd.read_excel(io = betting_path+'nhl odds 2018-19.xlsx')
df13 = pd.read_excel(io = betting_path+'nhl odds 2019-20.xlsx')




df1['season'] = 20072008
df2['season'] = 20082009
df3['season'] = 20092010
df4['season'] = 20102011
df5['season'] = 20112012
df6['season'] = 20122013
df7['season'] = 20132014
df8['season'] = 20142015
df9['season'] = 20152016
df10['season'] = 20162017
df11['season'] = 20172018
df12['season'] = 20182019
df13['season'] = 20192020

df_betting = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])

###Stage 1. Drop some rows, columns


df_betting = df_betting.loc[:, ['Date', 'season','VH', 'Team', 'Open']].copy()
df_mp_teams.rename(columns={"teamId": "team_id", 'gameDate': 'mp_date', 'gameId':'game_id' }, inplace = True)
##note there are other column names which differ, but team_id is the joining column so 
##make it consistent


##has 5 rows for each game_id+team for all the different situations, 5v4, etc
df_mp_teams_all = df_mp_teams.copy()  

##only has the rows for all situations (divide num rows by 5)
df_mp_teams = df_mp_teams.loc[df_mp_teams['situation'] == 'all', :].copy()


##deal with NaN values later ... 
# notes: it appears most of missing values are in df_mp
##note there are more nan values in df_game_skaters/team/goalies
#df_game.drop(columns = ['home_rink_side_start'], inplace = True)


### get rid of some weird rows


df_game.drop_duplicates(inplace = True)
df_game = df_game[~df_game['away_team_id'].isin([87,88,89,90])].copy()
df_game = df_game[~df_game['home_team_id'].isin([87,88,89,90])].copy()
df_betting = df_betting[~(df_betting['VH'] == 'N')].copy()

##Stage 2 Restrict the seaons to 20082009 to 20192020 is the range common to all 3 df's
## fix seasons format in df_mp (other 2 already have 20082009 format)


df_mp_teams['season'] = df_mp_teams['season'].map(fix_mp_season)
df_mp_teams_all['season'] = df_mp_teams_all['season'].map(fix_mp_season)


##restrict seasons; 
seasons = []
for n in range(2008,2020):
    seasons.append(int(str(n)+str(n+1)))

#check seasons look ok
print(seasons)



### set up list of all the df's for easy for loops
data_frames_all = [df_mp_teams, df_mp_teams_all,
df_betting,
df_game,
df_game_team_stats, 
df_game_goalie_stats,
df_team_info,
df_game_officials,
df_game_scratches, 
df_game_skater_stats]

##for now just worry about joining these ones:

data_frames = [df_mp_teams, df_mp_teams_all, df_betting, df_game]

# for X in data_frames:
#     X = X.loc[X['season'].isin(seasons), :].copy()
#     X.reset_index(drop = True, inplace = True)
# ##!! need to check this works. It does NOT
# for X in data_frames:
#     print(sorted(list(set(X['season']))))


##Note: I check in notebook the df's had same num of rows in the colums we kept before 
# and after

df_betting = df_betting.loc[df_game['season'].isin(seasons), :].copy()
df_game = df_game.loc[df_game['season'].isin(seasons), :].copy()
df_mp_teams = df_mp_teams.loc[df_mp_teams['season'].isin(seasons), :].copy()
df_mp_teams_all = df_mp_teams_all.loc[df_mp_teams_all['season'].isin(seasons), :].copy()

## the index is no longer consecutive so we reset:

df_betting.reset_index(drop = True, inplace = True)
df_game.reset_index(drop = True, inplace = True)
df_mp_teams.reset_index(drop = True, inplace = True)
df_mp_teams_all.reset_index(drop = True, inplace = True)

##here is a count of how many games in each df ... approx the same ... so looks likely there 
##should be close to full overlap in game_id's

#for seas in seasons:
#    print(seas, len(df_mp_teams_all.loc[df_mp_teams['season']==seas])/2, len(df_game.loc[df_game['season']==seas]), len(df_betting.loc[df_betting['season']==seas])/2)

    

## do mp_date for df_games and df_betting format is integer =20080923

df_game['date_time_GMT'] = pd.to_datetime(df_game['date_time_GMT']) 
df_game['mp_date'] = df_game['date_time_GMT'].apply(game_add_mp_date)
df_betting['mp_date'] = np.vectorize(bet_add_mp_date)(df_betting['Date'], df_betting['season'])

##fix or append team_names, etc "NYR" following df_team_info (from nhl.com)

df_betting['nhl_name'] = df_betting['Team'].apply(bet_to_nhl)
df_game['nhl_name_away_team'] = df_game['away_team_id'].apply(game_to_nhl)
df_game['nhl_name_home_team'] = df_game['home_team_id'].apply(game_to_nhl)
df_mp_teams['nhl_name'] = df_mp_teams['name'].apply(mp_to_nhl)
df_mp_teams_all['nhl_name'] = df_mp_teams_all['name'].apply(mp_to_nhl)

##assign game_id to df_betting ... using two different look up tables, df_game and df_mp_teams
##note the following error codes are assigned if a game is not found or found more than once 
# if a home game is empty: 80
# if a home game has >= 2 entries: 82
# if an away game is empty: 10
# if an away game has >= 12 entries: 82

##below we add excluded ={0} to indicate that the 0th argment (the look up df) is not to be vectorized
df_betting['mp_game_id'] =  np.vectorize(mp_to_bet_add_game_id, excluded={0})(df_mp_teams, df_betting['mp_date'], df_betting['nhl_name'], df_betting['VH'] ) 
df_betting['gm_game_id'] =  np.vectorize(game_to_bet_add_game_id, excluded={0})(df_game, df_betting['mp_date'], df_betting['nhl_name'], df_betting['VH'] ) 

