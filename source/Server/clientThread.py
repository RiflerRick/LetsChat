#!/usr/bin/python
import threading
from clientThreadReadHandle import ClientThreadReadHandle

class ClientThread(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket, allClients):
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
        allClients: list
            list of Socket objects refering to all clients connected to the server

        Returns
        -------
        None

        """
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket              # the socket returned by the accept function
        self.allClients=allClients

    # this thread will spawn 2 other threads, the reading and writing handles
    def run(self):
        """
        The run method is called when the thread is started. The run method contains the code to be executed when we start the thread. 

        Here the run method creates a new thread called clientThreadReadHandle and starts it. 

        Returns
        -------
        None

        """
        # following line will take data from the client and broadcast to all clients
        clientThreadReadHandle=ClientThreadReadHandle(1, 'readHandle', 1, self.clientSocket, self.allClients) 
        
        clientThreadReadHandle.start()
