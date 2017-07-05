#!/usr/bin/python
"""
This is a server socket application
"""
import socket               # Import socket module
from clientThread import ClientThread

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1337               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
allClients=[]               # all clients will be stored here as sockets

s.listen(5)                 # Now wait for client connection.
print('started listening on port')
clientCounter=0
clientThreadsList=[]
while True:
    """
    There is one very important idea here and that is once a new client joins there is no way of updating the old threads for new clients, so we need to respawn all the threads. This is obviously a drawback. But for now it is okay
    """
    
    c, addr = s.accept()     # Establish connection with client, c is actually the client socket
    print('got the connection from {}'.format(addr))
    c.send(bytes('Thank you for connecting', 'utf-8'))
    clientCounter+=1
    allClients.append(c)

    if clientCounter > 1:
        print('stopping all previous client threads')
        for i in range(clientCounter-1):
            clientThreadsList[i].join()
    else:
        clientThread=ClientThread(clientCounter, 'client', clientCounter, c, allClients)
        clientThreadsList.append(clientThread)
        clientThread.start()
        continue

    print('re-initializing all threads')

    for i in range(clientCounter):
        clientThread=ClientThread(clientCounter, 'client', clientCounter, allClients[i], allClients)
        clientThreadsList[i]=clientThread
        clientThread.start()
