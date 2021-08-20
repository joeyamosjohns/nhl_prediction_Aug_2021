

feat_rename = {'Date':'date', 'mp_date':'full_date', 'HoA_gm_stats':'HoA',  }


feat_drop = [ 
'startRinkSide',
'HoA',   #this is mp  ###many of these are repeated from mp_data
'HoA_bet',
'VH',
'home_or_away',
'team',
'name',
'Team',
#'Unnamed: 0',
'playerTeam',
'position',
'blocked',  ## Same as bSAAgainst
'pim', ## same as penaltyminFor
'goals',  ##goalsFor
'shots',
'giveaways',
 'hits',
]    


#################################first round
feat_goals = [
'goalsAgainst',
 'goalsFor',]

##do ga - gf and maybe gf/(gf+ga) ... can I get rid of OT and SO ? Not so easy ... would need to use situation stuff.

##
feat_SOG = [
'shotsOnGoalAgainst',
 'shotsOnGoalFor',
]
##sh%, sv%

feat_saves = [
'savedShotsOnGoalAgainst',
 'savedShotsOnGoalFor',
#pair with shots for sv%, sh%
]

##pp, pk, penalties

feat_pen_pp_pk = [
'penalityMinutesAgainst',  #Penalties 
 'penalityMinutesFor',
# 'penaltiesAgainst',
# 'penaltiesFor',  not sure so useful compared to minutes 
'powerPlayGoals',
 'powerPlayOpportunities',  #Powerplay
]
##! Need to create pk stat and pp%, pk%


##xgoals
feat_xgoals =[
'xGoalsAgainst', #(measure of quality of chances for and against)
'xGoalsFor',
 'xGoalsPercentage', #derived from above two
]

##possession 

feat_SA = [
'unblockedShotAttemptsAgainst',
 'unblockedShotAttemptsFor',
 'shotAttemptsAgainst',
 'shotAttemptsFor',
'corsiPercentage',  ##derived from 4 above
'fenwickPercentage',
 ]

##a way to get possession 

feat_FO = [
  'faceOffsWonAgainst',
 'faceOffsWonFor',
'faceOffWinPercentage',]  #has missing nan ... re-do it using last 2.

##measures of possession loss/gain 

feat_give_aways = [
 'giveawaysAgainst',
 'giveawaysFor',
 ] 

feat_dzone_give_aways = [ 
'dZoneGiveawaysAgainst',
 'dZoneGiveawaysFor',]

##should cause more give aways and recoveries 

feat_hits = [
'hitsAgainst',
 'hitsFor',
] 



#measures defensive stat ... also ability to get shots thru

feat_blocked = [ 
'blockedShotAttemptsAgainst',
'blockedShotAttemptsFor',]

##measures shooting skill to hit the net or ability to make guys shoot wide if you are in lane (kind of like block)

feat_missed = [
'missedShotsAgainst',
'missedShotsFor',]

##measures how many rebounds you give up (degense)... and how many you generate (offense)

##g/rb 
##sht/rb 
##hml sht/rb
## xg/rb 

feat_rebounds = [
'reboundGoalsAgainst',  #could put with goals ... prolly want g/rb; pair with high rebounds for
 'reboundGoalsFor',
 'reboundsAgainst',
 'reboundsFor',
 ] 

##ability to maintain pressure ... 

feat_pressure = [
 'playContinuedInZoneAgainst',  #after a shot is next shot in zone (no events outside+ same players on ice)
 'playContinuedInZoneFor',
  
 'playContinuedOutsideZoneAgainst',
 'playContinuedOutsideZoneFor',
]

                  
feat_pressure_stoppage = [
'freezeAgainst',  # "freeze after shot attempt For/Against"
'freezeFor',

'playStoppedAgainst',
 'playStoppedFor',   #non-freeze reason

]

################################second round

feat_goals_hml_danger = [
 'highDangerGoalsAgainst',
 'highDangerGoalsFor',
 'mediumDangerGoalsAgainst',
 'mediumDangerGoalsFor',
 'lowDangerGoalsAgainst',
 'lowDangerGoalsFor',
]

feat_saves_fen = [
'savedUnblockedShotAttemptsAgainst',  ##mised shots plus saved SOG
'savedUnblockedShotAttemptsFor',  #pair with unblocked shots for Fsv%
]

feat_xgoals_adj = [ 
'scoreVenueAdjustedxGoalsAgainst',  ##probably select one of these 3 versions? 
 'scoreVenueAdjustedxGoalsFor',
    
'flurryAdjustedxGoalsAgainst',
'flurryAdjustedxGoalsFor',

'flurryScoreVenueAdjustedxGoalsAgainst',
'flurryScoreVenueAdjustedxGoalsFor',
]


feat_xgoals_hml_danger = [
 'highDangerxGoalsAgainst',
 'highDangerxGoalsFor',
 
 'mediumDangerxGoalsAgainst',
 'mediumDangerxGoalsFor',
 
 'lowDangerxGoalsAgainst',
 'lowDangerxGoalsFor',
] 

feat_xgoals_rebounds = [
'xGoalsFromActualReboundsOfShotsAgainst',
'xGoalsFromActualReboundsOfShotsFor',
'xGoalsFromxReboundsOfShotsAgainst',
'xGoalsFromxReboundsOfShotsFor',
'totalShotCreditAgainst',  ##xgoals + xgoalsfromxreb -reboundxgoals ?
'totalShotCreditFor',
]

feat_SA_adj = [
'scoreAdjustedShotsAttemptsAgainst',
'scoreAdjustedShotsAttemptsFor',
'scoreAdjustedUnblockedShotAttemptsAgainst',   
'scoreAdjustedUnblockedShotAttemptsFor',

]


feat_SOG_hml_danger = [
'highDangerShotsAgainst',
 'highDangerShotsFor',

'mediumDangerShotsAgainst',
 'mediumDangerShotsFor',

'lowDangerShotsAgainst',
 'lowDangerShotsFor',
]

feat_xrebounds = [
'reboundxGoalsAgainst',
 'reboundxGoalsFor',
 'xReboundsAgainst',
 'xReboundsFor']

feat_xpressure = [
'xPlayStoppedAgainst',
 'xPlayStoppedFor',

 'xPlayContinuedInZoneAgainst',   ##maybe do PCIZA and PCIZA - xPCIZA (measures lucky/unlucky)
 'xPlayContinuedInZoneFor',
 
'xPlayStoppedAgainst',
 'xPlayStoppedFor',
]
