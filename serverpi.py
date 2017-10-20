def execute_unix(inputcommand):
    p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output

# wolframalpha answer function
def getAnswer(str):
    import wolframalpha
    import os
    from serverKeys import app_id
    client = wolframalpha.Client(app_id)
    print('[Checkpoint 10] Sending question to Wolframalpha: %s' % (str))
    result = client.query(str)
    if next(result.results).text :
        stringAnswer = next(result.results).text
        print('[Checkpoint 11] Received answer from Wolframalpha: %s' % (stringAnswer))
        print('[Checkpoint 12] Speaking answer parsed for only alphanumeric and space characters: %s' % (stringAnswer))
        execute_unix('espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % stringAnswer)
        return stringAnswer
    else :
        print('Question could not be answered')

# server reply function
def reply(clientpi, response):
    replyPickle = pickle.dumps(response)
    clientin.send(replyPickle)
    print('[Checkpoint 13] Sending Answer: %s' % (response))

import socket
import sys
import pickle
import os
import subprocess

server_port = int(sys.argv[2])
backlog_size = int(sys.argv[4])
socket_size = int(sys.argv[6])
host = ''

s = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(host)
print(server_port)
s.bind((host, server_port))
print('[Checkpoint 01] Created socket at 0.0.0.0 on port %d' % (server_port))
s.listen(backlog_size)
print('[Checkpoint 02] Listing for client connections')
while 1:
    client, address = s.accept()
    print('[Checkpoint 07] Accepted client connection from %s on port %s' % (client, address))
    data = client.recv(socket_size)
    if data:
        message = pickle.loads(data)
        print('[Checkpoint 09] Received question: %s' % (message))
        question = message.split('#')[0]
        myAnswer = getAnswer(question)
        reply(client, myAnswer)
