 

import pandas as pd
import numpy as np

def to_string(n):
    s = str(n)
    if len(s) ==1:
        return "0"+s
    else:
        return s

##for assigning dates in df_game
#takes in date_time date and returns integer yyyymmdd eg 20080904
##note this is df_mp format

def game_add_mp_date(date_time):
    d = date_time.day
    m = date_time.month
    y = date_time.year
    dd = to_string(d)
    mm = to_string(m)
    yyyy = str(y)
    return(int(yyyy+mm+dd))

##test 
date_time1 = pd.to_datetime('2016-10-19T00:30:00Z')
date_time2 = pd.to_datetime('2008-09-19T00:30:00Z')

print("two tests for game_add_mp_date:")
print(game_add_mp_date(date_time1) == 20161019)
print(game_add_mp_date(date_time2)==20080919)
print(" ")
##for assigning dates to df_betting
#takes in ingegers date = 913 or 1026 season = 20082009 
# returns  returns integer yyyymmdd eg 20080904
#note this is df_mp format

def bet_add_mp_date(date, season):
    d = str(date)
    s = str(season)
    if len(d) == 3:
        d = "0"+d 
    if (900 < date):
        y= s[:4]
    else:
        y = s[4:]
    return int(y+d)

##test
print("three tests for bed_add_mp_date:")
print(bet_add_mp_date(912, 20082009) == 20080912)
print(bet_add_mp_date(1025,20102011) == 20101025)
print(bet_add_mp_date(227,20102011) == 20110227)
print(" ")

##fix season format for df_mp
##takes in integer 2008 and returns 20082009
##note: I have verified in df_mp for two seasons 2008 labels 20082009

def fix_mp_season(n):
    return int(str(n)+str(n+1))

##tests
print("two tests for fix_mp_season:")
print(fix_mp_season(2008) == 20082009)
print(fix_mp_season(2019) == 20192020)
print(" ")