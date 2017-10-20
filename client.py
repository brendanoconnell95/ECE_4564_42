import tweepy
import pickle
import hashlib
import socket
import sys

from client_params import *
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

#API keys imported from client_params file
consumer_key = ckey
consumer_secret = csecret
access_token = atoken
access_token_secret = asecret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(StreamListener):
    def on_data(self,data):
        question = data.split('"text":"')[1].split('",')[0]
        
        print (question)
        #send(ipaddr, port, question)
        
        return True
    
    def on_status(self, status):
        print(status.text)
        
    def on_error(self, status_code):
        print (status_code)
        return False

myStream = Stream(auth, MyStreamListener())
myStream.filter(track=["#ECE4564T14"])

def send(ipaddr, port, question):
    picklepayload = pickle.dumps(question)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ipaddr,port)
    s.send(poicklepayload)
    size = 1024
    reply = s.recv(size)
    unpickled = pickle.loads(reply)
    print (unpickled[0])
    return unpickled[0]

    
