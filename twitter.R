library('twitteR')
library("ROAuth")
accessToken="1088035550978691072-2kR3vIaNc0ojwx4pGU5ugIUzSuC1RI"
accessTokenSecret="CmgSgt1CKfgEeIOSiAsPwC05cVGU3dUwkpnp2hm0Lllca"
consumerKey="DGjnvrSC3zY3CNhYJVazdf132"
consumerSecret="q65jCQvsl1xX8lKSPsnJKAKg5viS7OM3t8gxV1fabLtGx0IkPI"
setup_twitter_oauth (consumerKey, consumerSecret, accessToken, accessTokenSecret) 
tweets <- searchTwitter("tcs",n=10000,lang='en',since = "2019-04-01" ,until = "2019-04-10")
tweetsDF <- twListToDF(tweets)
write.csv(tweetsDF,"C:\\Users\\pawan_300\\Desktop\\tweets.csv")

