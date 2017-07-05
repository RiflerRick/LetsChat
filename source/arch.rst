=============
API Reference
=============

Server
------
.. py:module:: serverSocket

.. py:module:: clientThread

.. py:class:: ClientThread

    The ClientThread is a thread class. Its instance is created as a thread that is spawned by the serverSocket module for handling a new client. For each new user that connects to the server, we would create a new thread for handling that client. 

    .. py:method:: __init__(self, threadID, name, counter, clientSocket, allClients)

        This __init__ method overrides the __init__ function of the Thread class in the threading module. It calls the __init__ function to actually create an instance of the Thread class. It then initializes other variables to be required by the thread.

        :param threadID: unique ID given to each thread
        :param name: name given to the thread
        :param counter: number of threads of this name generated
        :param clientSocket: Socket instance of the client.
        :param allClients: a list of Socket instances of all clients connected to the server
        :rtype: None

    .. py:method:: run(self)

        The run method is executed when a thread is started. Here the run method is used to spawn a new thread called clientThreadReadHandle that handles client read operations. 

        :rtype: None

Client
------

.. py:module:: clientSocket

.. py:module:: writingThread

.. py:class:: WritingThread

    The WritingThread is a thread class. Its instance is created as a thread that is spawned by the clientSocket module for sending data from the client to the server. It reads data from the standard input and sends it to the server.

    .. py:method::  __init__(self, threadID, name, counter, clientSocket)

        This __init__ method overrides the __init__ function of the Thread class in the threading module. It calls the __init__ function to actually create an instance of the Thread class. It then initializes other variables to be required by the thread.

        :param threadID: unique ID given to each thread
        :param name: name given to the thread
        :param counter: number of threads of this name generated
        :param clientSocket: Socket instance of the client.
        :rtype: None

    .. py:method: run(self)

        The run method is executed when the thread is started. Here the run method is used to wait for user input into the standard input from the client side and send it to the server.

        :rtype: None

.. py:module:: readingThread

.. py:class:: ReadingThread

    The ReadingThread is a thread class. Its instance is created as a thread that is spawned by the clientSocket module.

    .. py:method:: __init__(self, threadID, name, counter, clientSocket)

        This __init__ method overrides the __init__ function of the Thread class in the threading module. It calls the __init__ function to actually create an instance of the Thread class. It then initializes other variables to be required by the thread.

        :param threadID: unique ID given to each thread
        :param name: name given to the thread
        :param counter: number of threads of this name generated
        :param clientSocket: Socket instance of the client.
        :rtype: None

    .. py:method:: run(self)

        The run method contains code that must be executed when the thread is started. Here the run method checks the clientSocket for any messages that the server has sent. If so the message is displayed on the client's console.

        :rtype: None
