#!/usr/bin/python
import threading
import socket
ENCODING='utf-8'

class WritingThread(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket):
        """
        This __init__ function overrides the __init__ function of the Thread class in the threading module. It calls the __init__ function to actually create an instance of the Thread class. It then initializes other variables to be required by the thread.

        Parameters
        ----------
        threadID: int
            unique id of the thread
        name: string
            name given to the thread
        counter: int
            number of threads instantiated
        clientSocket: Socket
            instance of Socket class refering to the client socket connected

        Returns
        -------
        None

        """
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket

    def run(self):
        """
        The run method contains the code that must be executed when the thread is started. 

        Here the method checks for anything that the client has written on the standard input. If so the message is sent across the clientSocket to the server.

        Returns
        -------
        None
        
        """
        # since this is the writing thread of the client it will simply read data from stdin and write it to the server.
        print('message: ', end='')
        message= input()

        # BUG: This line should wait for user input but is not waiting.

        message=bytes(message, ENCODING)
        self.clientSocket.send(message)
    