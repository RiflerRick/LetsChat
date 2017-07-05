#~/usr/bin/python
import threading

class ClientThreadReadHandle(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket, allClients):
        
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket          # the socket returned by the accept function
        self.allClients=allClients

    def run(self):
        msg=self.clientSocket.recv(1024)
        print('message received from client side: {}'.format(msg))
        
        for client in self.allClients:          # broadcast to all clients except itself.
            if client is not self.clientSocket:
                client.send(msg)
        
