#~/usr/bin/python
# will take data from the specific client and write to all clients
import threading

class ClientThreadReadHandle(threading.Thread):
    def __init__(self, threadID, name, counter, clientSocket, allClients):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        self.clientSocket=clientSocket # the socket returned by the accept function
        self.allClients=allClients

    def run(self):
        msg=self.clientSocket.recv(1024)
        # broadcast to all clients except itself.
        for client in self.allClients:
            if client is not self.clientSocket:
                client.send(msg)
        
