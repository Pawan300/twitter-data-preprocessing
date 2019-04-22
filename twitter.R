library('twitteR')
library("ROAuth")
accessToken="*******************"
accessTokenSecret="******************"
consumerKey="*******************"
consumerSecret="*********************"
setup_twitter_oauth (consumerKey, consumerSecret, accessToken, accessTokenSecret) 
tweets <- searchTwitter("Search Query",n=10000,lang='en',since = "2019-04-01" ,until = "2019-04-10")
tweetsDF <- twListToDF(tweets)
write.csv(tweetsDF,"tweets.csv")
# lang='en' Means English language only
