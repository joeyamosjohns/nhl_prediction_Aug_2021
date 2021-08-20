# nhl_prediction_Aug_2021

This is a preliminary version of my final project for Lighthouse Labs data science bootcamp; 
this was a 2 week project completed Aug 12, 2021. The notebooks are still in somewhat rough form but I 
have cleaned them up to some degree and removed many of the extraneous notebooks that are still in the other repo nhl_predictions_rough_draft.


project goals:

1. To predict the outcome win/loss of regular season NHL games from past data; secondarily regression prediction of the goal differential (home -away) 
target: 60% accuracy or higher, and f1 score in the range 65-70 %

2. Test model from 1 in betting strategy to evaluate through ROI. Two components here: the model, and the betting stratgy.
target: ROI at least 10%


note: 60% accuracy is fairly good, as betting companies achieve an accuracy rate in the 59% range. Hockey is more random
than other major sports so accuracy in the 60% range is reasonable (as opposed to say basketball which is much easier
to predict, probably in great part beacuse of star dominance, where accuracy is more in the 70% range )


results so far:

The project at the moment is at a "minimal viable model" stage ... there is much room for other versions, 
which one would expect to improve the models  (tuning, many different features, and adding a neural net model 
are the main things to add). 

I should state at the outset that there are three modelling approaches I tried so far, but each of them is based on existing approaches of others (more details on that below). I will branch out into my own versions going forward but I thought it best to try versions which are known to work pretty well to start with. 


So far the minimal viable models have these results:

1. a few models in preliminary tests so far have accuracy in the 59-61% range and f1 scores in the 65-70% range
so the target has been achieved, but more rigorous testing is in order.  But still, there seems to be much room for improvement 
in the areas of tuning the models and trying many other possible features, both existing ones, and some new ones I have in mind to create.

2. Using basically no strategy in the betting, in simulated betting, using logistic regression, we have an ROI of 5.3% in 2016-17 and 10.1% in 2017-18 for an average of 7.5%. More sophisticated strategies will be attempted which may improve this, and certainly if the models improve then this should improve as well.

notes on the contents of this repo (as of August 2021):

-The main 4 notebooks that may be of interest are:

1. I have three approaches to modelling, which are in the notebooks labeled Model 1_... , Model 2_..., and Model 3_ ....
(each notebook has several models, but the overall approach is what is common to the notebook). 

2. I also have one notebook called Betting_strategy_ ... which goes through the rudimentary betting simulation.

-In addition, there is a folder called "data_shaping" which contains the notebooks I used to take the raw data and
turn it into usable csv files that each of the modelling approaches use. 

-Finally, there is a folder called "modules" which contains some of the more polished .py files that I created 
from the notebooks. These represent the beginnings of a more polished final draft of the project which will have .py files 
containing various functions (which may later be parts of classes), with a master file which imports the functions or classes as needed.


notes on the data used:

-the data (csv files) I used was from approximatley the last 10 seasons of the NHL and it came from 3 sources: On Kaggle, Martin Ellis kindly posted svearl high quality files with NHL data; Moneypuck.com provided very detailed shot level data (which I have not come close to fully using yet); and Milton Leung had some NHL data on his GitHub repo, which I have used as well.

-I want to say thanks! to the three people responsible for those sources.
-Going forward, I will probably scrape some of my own data from various websites such as nhl.com or hockey_reference in order
to customize my data further for exactly what I want to do.

-notes on the three approaches to modelling:

-I want to thank and acknowlede the three original authors (mentioned below) whose approaches I have
followed in my prelimnary attempts so far. 

-model 1 is a very basic model which only keeps track of which teams are playing (as dummy variables), who is home and away
and makes predictions of the goal differential (home goals - away goals). The way the dummy variables is set up is 
quite clever and was learned from rom this 2020 article by Lianne and Justin, thanks to them for sharing:
https://www.justintodata.com/improve-sports-betting-odds-guide-in-python/

results of model 1: the results here were decent in the 55% accuracy range (not as good as the accuracy reported in the article)

-model 2 is based on a paper of Pischedda from 2013 in which he himslef is replcating and slightly modifying work 
of Weissbock and others. I also tried combining this approach with the approach of model 1.
I also attempted to learn incrementally over the season which was different from the traditional train/test approach
that Pischedda took.


results of model 2: the results here were not very good - in the 52-53% range. Perhaps better tuning is needed but I certainly
did not match the results that Pischedda obtained; however he did work on single shortenned seaosn of 2012-13
so it's possible his results may not generalize easily.

-model 3 is based on the approach of Milton Leung described here: 
https://medium.com/coinmonks/4-718-using-machine-learning-to-bet-on-the-nhl-25d16649cd52
and further details are in his Githib repo referenced in the article.
The main difference here was that he trained on around 5 seasons with a traditional
test/train split and then did predictions on the subsequent 1 or 2 seasons ( I did 2 seasons)
I also used features similar to his in order to try to get decent first results.

results of model 3: these were the first quite favorable results, with 3-4 models in 
the 59-61% range on the two subsequent seasons, at least in this first round of testing


future plans:

There are many directions I will explore going forward in the coming weeks.

-The most important one is exploring features more systematically; there are many 
existing stats that I did not use (in the moneypuck data, there are ~ 100 for example, of which 
probably 20-30 I could easily incorporate). I also have several intriguing ideas for creating features 
of my own that I want to try.

-Next, systematic tuning has not yet been done so that might also give a slight improvement
(especially for complex models like xgboost).

-Finally, I plan on bringing in neural net model to see what it can do; several authors
have achieved good success with neural nets in the past in predicting hockey. One author 
even used a neural net as a means of optimizing betting strategy which could be interesting 
to explore.





