import tweepy 
import re
import codecs
import urllib2

ckey = "Consumer Key"
csecret = 'Consumer Secret'
atoken = 'Access Token'
asecret = 'Access Secret'
count = 0

def internet_on():
	try:
		response=urllib2.urlopen('https://www.google.co.in',timeout=20)
		return True
	except urllib2.URLError as err: pass
	return False


auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)


quotes = open('ThriveQuotes.txt','r')
quotes = quotes.readlines()
quotes[count] = quotes[count].decode('ascii','ignore')


if internet_on() == True:
	if len(quotes[count]) <= 144:
		api.update_status(status = quotes[count])
		quotes = quotes[count+2:]
	else:
		quotes = quotes[count+2:]

	quotelist = open('ThriveQuotes.txt','w')
	quotelist = open('ThriveQuotes.txt','a')
	for items in quotes:
		quotelist.write("%s"% items)


	


