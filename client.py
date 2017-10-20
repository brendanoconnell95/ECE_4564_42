import tweepy
import pickle
import hashlib
import socket
import sys
import os
import subprocess


from client_params import *
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

def execute_unix(inputcommand):
    p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output

#API keys imported from client_params file
consumer_key = ckey
consumer_secret = csecret
access_token = atoken
access_token_secret = asecret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ipaddr = sys.argv[2]
port = sys.argv[4]
hashtag = sys.argv[6]

def send(ipaddr, port, question):
    picklepayload = pickle.dumps(question)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_int = int(port)
    s.connect((ipaddr,port_int))
    print ("[Checkpoint 06] Connecting to %s on port %s" % (ipaddr, port))
    s.send(picklepayload)
    print ("[Checkpoint 08] Sending question: %s" % question)
    size = 1024
    reply = s.recv(size)
    unpickled = pickle.loads(reply)
    print ("[Checkpoint 14] Received answer: %s" % unpickled)
    return unpickled

    

class MyStreamListener(StreamListener):
    def on_data(self,data):
        question = data.split('"text":"')[1].split('",')[0]
        print ("[Checkpoint 04] New Tweet: %s" % question)
        
        #speak the question
        questionString = question.split('#')[0]
        print ("[Checkpoint 05] Speaking question parsed for only Alphanumeric and Space characters: %s" %questionString)
        execute_unix('espeak -ven+m3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % questionString)

        send(ipaddr, port, question)
        return True
    
    def on_status(self, status):
        print(status.text)
        
    def on_error(self, status_code):
        print (status_code)
        return False

myStream = Stream(auth, MyStreamListener())
myStream.filter(track=[hashtag])
print ("[Checkpoint 03] Listening for Tweets that contain %s" % hashtag)

