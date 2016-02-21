from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('localhost',12000))
    serversocket.listen(1)
    (clientsocket, address) = serversocket.accept()
    clientsocket.send("Hello CS374!")
    print "message sent..."
    clientsocket.close()
    serversocket.close()

createServer()