import twitter
import datetime
user = 1301497579
file = open ("TwitterCredentials.txt")
creds = file.readline().strip().split(',')
api = twitter.Api(creds[0],creds[1], creds[2], creds[3])
currentSession = open (users/[chulbert1]/library/Application Support/Google/Chrome/Default/)


#statuses = api.getUserTimeline(user)
#print (statuses[0].text)

timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("New message tweeted at " + str(timestamp)+ currentSession)
print("Status updated to: " + response.text)




