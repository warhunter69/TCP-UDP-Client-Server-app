from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    # clientAddress is the ip address and portnumber
    message, clientAddress = serverSocket.recvfrom(2048)
    print("server has just recieved a message, content: {0}".format(message.decode()))
    modifiedMessage = message.decode().upper()
    # we now attach the ip address and portnumber to the message
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    # the server address is also attached to the packet, althought this is done automatically rather than explicit code