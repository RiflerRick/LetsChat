# Architecture
It is a very basic group chat application which means that all messages that we get from one client will be broadcasted to all clients.

Every client will spawn 2 threads, a reading thread and a writing thread. Pretty basic.

The server on acceptance of connection from a client will spawn a new thread for the client. Thats the very basic idea.

Each client thread will also have a reading and writing handle. Needless to mention these are also threads.