========
Tutorial
========

Pre-requisites
=============
There are 2 pre-requisites for installing the application.

- Python 3.6.0 must be installed in your system. In case you do not have python 3.6.0 installed head over to the official `download site`_ of python. The official site contains all required documentation for installing python in your local machine. 

- pip must be installed in your system in order to install all modules required for running the application. pip is an extrememly popular installer that is extensively used for installing python modules. For guidelines on installing pip head to the official pip `installation site`_.

.. _download site: https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiKlbiey_HUAhURS48KHdjwBOQQFggnMAA&url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&usg=AFQjCNHmio9Qjvf1yGEMWKJTaXeMN7k2W 

.. _installation site: https://pip.pypa.io/en/stable/installing/

Installing
==========
The entire project is uploaded on github_.

.. _github: https://github.com/RiflerRick/LetsChat

Installing requisite modules
----------------------------
To start the server go to the source directory present in the root directory. Then execute the following command on the command prompt on your Windows machine or the terminal on your Linux/Max machines.

.. code-block:: shell

    pip install requirements.txt

.. _above:

Starting the server
-------------------
Once you are through with installing all necessary modules you should be okay to start the server. The server runs on port 1337 so its important that this port is free. To check that no process is currently active in port 1337 execute the following command on the command prompt on your Windows machine. 

.. code-block:: shell

    netstat -a

The above command will show all process running on all ports available on the machine. If port 1337 is not shown, it means that the port is not currently running any process.

On Linux/Mac you can check the ports running on the local machine using the following terminal command.

.. code-block:: shell

    netstat -pnlt | grep ':1337'

If there are any processes running on port 1337, we would need to kill that process before starting the server.
Once you are reaady to start the server, head over to the source directory inside the root directory. Next go inside the server directory present in the source directory. Then execute the following command on the command prompt on your Windows machine or the terminal on your Linux/Max machines. T

.. code-block:: shell

    python serverSocket.py

With this command the server should be started on your local machine and listening on port 1337.

Connecting to the server
------------------------
If you are a client and would like to start a group chat or get involved in an existing group chat, you will be required to connect to the server through port 1337. Make sure that the port is not blocked by another process. To check for processes running on port 1337 follow the procedure listed above_.

Once you are ready to connect to the server head over to the Client directory inside source. Now execute the following command in the command prompt of your Windows machine or in the terminal of your Linux/Mac machine. 

.. code-block:: shell

    python clientSocket.py

Now the client should be connected to the server. Now you can exchange messages with other clients on the network. 

