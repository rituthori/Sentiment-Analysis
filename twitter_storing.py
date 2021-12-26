from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor

#Custom stream listener class to collect relevant details
class StreamListener(StreamListener):
    def on_status(self, status):
        if hasattr(status, 'retweeted_status'): # if the tweet is a retweeted tweet it 
        	 return								#will give the control back to stream.fliter
        print(status.text+"\n")
        fp.write(status.text+"\n")
    def on_error(self, status_code):
        if status_code == 420:
            return False

#API keys
ckey = 'GB60Bf9zmyLjuZpHJYjVs2sD9'
csec = 'WvmiAI0Lftl4JrVa2d9qVvQBnLyEl7gIJZKpRby47yzDFIpPg7'
atok = '1301009070887821313-r6W72ocuZF7sLUpDBflKip5JMyFMX4'
asec = 'fHaauDYsl5DfZU56lVYm3UVp5kAe5qGWNRKdZ3JsrB4of'

#Auth
auth = OAuthHandler(ckey, csec)
auth.set_access_token(atok, asec)
api = API(auth)

# \U0001F602 refers to 'happy'
#1F602 = happy, 1F62D = sad, 1F621= angry, 2764 = love, 1F61C = playful, 1F631 = confused
query = [u'\U0001F621']


fp = open("store.txt",'w',encoding='utf-8')
stream = Stream(auth = api.auth, listener = StreamListener())
stream.filter(track = query, languages = ["en"], stall_warnings = True)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

