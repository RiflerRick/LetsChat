#!/usr/bin/python
"""
.. automodule:: clientThread
"""
import threading
from clientThreadReadHandle import ClientThreadReadHandle

class ClientThread(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket, allClients):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket              # the socket returned by the accept function
        self.allClients=allClients

    # this thread will spawn 2 other threads, the reading and writing handles
    def run(self):
        # following line will take data from the client and broadcast to all clients
        clientThreadReadHandle=ClientThreadReadHandle(1, 'readHandle', 1, self.clientSocket, self.allClients) 
        
        clientThreadReadHandle.start()
