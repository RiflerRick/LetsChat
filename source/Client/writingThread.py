#!/usr/bin/python
"""
.. automodule:: writingThread
"""
import threading
import socket
ENCODING='utf-8'

class WritingThread(threading.Thread):
    """
    .. autoclass:: WritingThread(threading.Thread)
    """
    def __init__(self, threadID, name, counter, clientSocket):
        """
        .. automethod:: __init__(self, threadID, name, counter, clientSocket)
        """
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket

    def run(self):
        """
        .. automethod:: run(self)
        """
        # since this is the writing thread of the client it will simply read data from stdin and write it to the server.
        print('message: ', end='')
        message= input()

        # BUG: This line should wait for user input but is not waiting.

        message=bytes(message, ENCODING)
        self.clientSocket.send(message)
    