#~/usr/bin/python
import threading

class ClientThreadReadHandle(threading.Thread):
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
        self.clientSocket=clientSocket          # the socket returned by the accept function
        self.allClients=allClients

    def run(self):
        """
        The run method is called when the thread is started

        Here this method checks the clientSocket(here the clientSocket is the Socket instance returned from the serverSocket class) for messages, if any messages are found it receives those messages and broadcasts it to all clients
        """
        msg=self.clientSocket.recv(1024)
        print('message received from client side: {}'.format(msg))
        
        for client in self.allClients:          # broadcast to all clients except itself.
            if client is not self.clientSocket:
                client.send(msg)
        
