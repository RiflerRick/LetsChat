#!/usr/bin/python
import threading
import socket

class ReadingThread(threading.Thread):
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
        The run method contains code that must be executed when the thread is started.

        Here the run method checks the clientSocket for any messages that the server has sent. If so the message is displayed on the client's console.

        Returns
        -------
        None
        
        """
        # since this is the reading thread of the client it will simply read the data sent from serverSocket and print it on the console.
        message=self.clientSocket.recv(1024)
        print('message from some client: {}'.format(str(message)))
    