#!/usr/bin/python
"""
.. automodule:: clientSocket
"""
import socket                               # Import socket module
from readingThread import ReadingThread
from writingThread import WritingThread
s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 1337                                 # Reserve a port for your service.

s.connect((host, port))
# here 1024 is the buffer size, which means we are trying to basically receive a message of size 1024
print ('message received from server: {}'.format(str(s.recv(1024))))          

while True:
    readingThread=ReadingThread(1, 'read', 1, s)
    writingThread=WritingThread(2, 'write', 2, s)
    readingThread.start()
    writingThread.start()
    
s.close                                     # Close the socket when done