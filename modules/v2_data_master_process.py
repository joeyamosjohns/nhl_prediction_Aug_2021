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

from data_bet_add_game_id import mp_to_bet_add_game_id_no_VH
##Stage 1. Import all the files 

##file paths
path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/"
Kaggle_path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/Data/Kaggle_Data_Ellis/"
mp_path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/Data/Money_Puck_Data/"
betting_path = "/Users/joejohns/data_bootcamp/GitHub/final_project_nhl_prediction/Data/Betting_Data/"
#data_bootcamp/GitHub/final_project_nhl_prediction/Data/Betting_Data/nhl odds 2007-08.xlsx
#data_bootcamp/GitHub/final_project_nhl_prediction/Data/Kaggle_Data_Ellis/
#data_bootcamp/GitHub/final_project_nhl_prediction/Data/Money_Puck_Data/


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

##omit 20072008 
df_betting = pd.concat([df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])


# ### set up list of all the df's for easy for loops
# data_frames_all = [df_mp_teams, 
# df_betting,
# df_game,
# df_game_team_stats, 
# df_game_goalie_stats,
# df_team_info,
# df_game_officials,
# df_game_scratches, 
# df_game_skater_stats]

# ##for now just worry about joining these ones:

# data_frames = [df_mp_teams, df_betting, df_game_team_stats]


###PLAN: combine df_betting (betting odds), df_game_team_stats (basic outcome, plus basic stats),
#  df_mp_teams (much more stats) into one master df. 
# 
# Key points
# 
#-the common seasons are 20082009 to 20192020 ... 
#-the main key to join on will be game_id; this is not present in df_betting
#-other key fields for joining will be home_or_away; nhl_team_name;
#-in order to fill in the game_id we will use date, team (and home/away) from df_mp_teams as lookup
# turns out df_game has issues with dates labelling which made it not work as a look up table for game_id


##Stage 2. Throw away some columns and rows 



df_betting = df_betting.loc[:, ['Date', 'season','VH', 'Team', 'Open']].copy()
df_mp_teams.rename(columns={"teamId": "team_id", 'gameDate': 'mp_date', 'gameId':'game_id' }, inplace = True)
##note there are other column names which differ, but team_id, mp_date, game_id are key for joining so we  
##make it consistent

df_mp_teams_big = df_mp_teams.copy()
##only has the rows for all situations (divide num rows by 5)
df_mp_teams = df_mp_teams.loc[(df_mp_teams['situation'] == 'all'), :] #&(df_mp_teams['playoffGame']==0), :].copy()

##restrict types to all situations later before merge 

df_game_team_stats.drop_duplicates(inplace = True)
df_game_team_stats = df_game_team_stats[~df_game_team_stats['team_id'].isin([87,88,89,90])].copy()
df_betting = df_betting[~(df_betting['VH'] == 'N')].copy() 

#Stage 3. Fix seasons label in df_mp_teams; then restrict the seasons to 20082009 to 20192020 [in common all 3]

df_mp_teams['season'] = df_mp_teams['season'].map(fix_mp_season)


##restrict seasons; 
seasons = []
for n in range(2008,2020):
    seasons.append(int(str(n)+str(n+1)))

#check seasons look ok
print(seasons)
 

df_betting = df_betting.loc[df_betting['season'].isin(seasons), :].copy()
#df_game_team_stats = df_game_team_stats.loc[df_game_team_stats['season'].isin(seasons), :].copy()
df_mp_teams = df_mp_teams.loc[df_mp_teams['season'].isin(seasons), :].copy()
#df_mp_teams = df_mp_teams.loc[df_mp_teams['season'].isin(seasons), :].copy()


## the index is no longer consecutive so we reset:

df_betting.reset_index(drop = True, inplace = True)
#df_game_team_stats.reset_index(drop = True, inplace = True)
df_mp_teams.reset_index(drop = True, inplace = True)


##! restrict df_game_team_stats later using the game_id

##Stage 4. Add date to df_bettinf; make common HoA format; make common nhl_name format; add (!) game_id to df_betting

df_betting['mp_date'] = np.vectorize(bet_add_mp_date)(df_betting['Date'], df_betting['season'])

HA_dic = { 'H': 'home', 'V': 'away', 'HOME': 'home', 'AWAY':'away'}
def add_HoA(h_or_a):  # h_or_a can be either of the formats used by mp or betting
    return HA_dic[h_or_a]

df_betting['HoA'] = df_betting['VH'].apply(add_HoA)

df_mp_teams['HoA'] = df_mp_teams['home_or_away'].apply(add_HoA)


df_betting['nhl_name'] = df_betting['Team'].apply(bet_to_nhl)
df_game_team_stats['nhl_name'] = df_game_team_stats['team_id'].apply(game_to_nhl)
df_mp_teams['nhl_name'] = df_mp_teams['name'].apply(mp_to_nhl)

df_betting['game_id'] =  np.vectorize(mp_to_bet_add_game_id_no_VH, excluded={0})(df_mp_teams, df_betting['mp_date'], df_betting['nhl_name'] ) 

##Stage 6. Join the three data frames ... we will first cut them all down to the common set of game_ids
## inspection of the number of game_ids shows that the number does not drop much when we do intersections (see notebook
# v2_Merge); sepifically, the numbers drop as follows
# 15277
# 15146
# 23730 ##because it had lots more seasons I didn't cut down 

#pairwise intersections
# 15145
# 14969
# 15101

#triple intersection
# 14969

#final inner join when we lose some weird labels H/A teams switched; team names off (around 85 games)


mp_game_ids = set(df_mp_teams['game_id'])
bet_game_ids = set(df_betting['game_id'])
game_stats_ids = set(df_game_team_stats['game_id'])

common_game_ids = set.intersection( mp_game_ids, bet_game_ids, game_stats_ids) 

df_betting = df_betting.loc[df_betting['game_id'].isin(common_game_ids), :].copy()
df_game_team_stats = df_game_team_stats.loc[df_game_team_stats['game_id'].isin(common_game_ids), :].copy()
df_mp_teams = df_mp_teams.loc[df_mp_teams['game_id'].isin(common_game_ids), :].copy()

X_merge = pd.merge(df_betting, df_game_team_stats, on = ['game_id', 'nhl_name'], how = 'inner', suffixes = ('_bet', '_gm_stats'))
X_merge2 = pd.merge(X_merge, df_mp_teams, on = ['game_id', 'nhl_name', 'mp_date', 'season'], how = 'inner', suffixes = ('_merge', '_mp_teams'))
##season and mp_date are not features of df_game_team_stats
##there are ~100 discrepencies as far as HoA labelling so I have not merged on that; one should 
##us df_game_team_stats as the arbitor of H/A 
##note: most of the errors are from df_mp labelling both games "away"
##there are only around 10 where bet and df_game disagree; hockey ref showed bet is wrong (20200117)

#check for loss of rows:
print(2*len(common_game_ids), X_merge2.shape[0])

#data_bet_stats_mp = X_merge2.copy()
#data_bet_stats_mp.to_csv(path + "Data/Shaped_Data/")

data = X_merge2.copy()

from data_features import feat_drop, feat_rename
data.drop(columns=feat_drop, inplace=True)
data.rename(columns=feat_rename, inplace = True)
data.reset_index(drop = True, inplace = True)
data.to_csv('data_bet_stats_mp.csv')