

# wolframalpha answer function
#def getAnswer(str):
#    import wolframalpha
#    from server_params import app_id

# server reply function
#def reply(clientpi):


#def speak:


import socket
import sys
import pickle

server_port = int(sys.argv[2])
backlog_size = int(sys.argv[4])
socket_size = int(sys.argv[6])
host = ''

s = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(host)
print(server_port)
s.bind((host, server_port))
print('Created socket at 0.0.0.0 on port %d' % (server_port))
s.listen(backlog_size)
print('Listing for client connections')
while 1:
    client, address = s.accept()
    print('Accepted client connection from %d on port %d' % (client, address))
    data = client.recv(socket_size)
    if data:
