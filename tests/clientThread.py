#!/usr/bin/python
"""
The client thread will be spawned by the server for connection with each client
"""
import threading
from clientThreadReadHandle import ClientThreadReadHandle

class ClientThread(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket, allClients):
        # call init function of Thread class
        # allClients is a list of all the sockets connected to this server
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket # the socket returned by the accept function
        self.allClients=allClients

    def run(self):
        # this thread will spawn 2 other threads, the reading and writing handles
        clientThreadReadHandle=ClientThreadReadHandle(1, 'readHandle', 1, self.clientSocket, self.allClients)# this will take data from the client and broadcast to all clients
        clientThreadReadHandle.start()
