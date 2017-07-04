#!/usr/bin/python
import threading
import socket

class ReadingThread(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket  

    def run(self):
        # since this is the reading thread of the client it will simply read the data sent from serverSocket and print it on the console.
        message=self.clientSocket.recv(1024)
        print('message from some client: {}'.format(str(message)))
    