from socket import *
serverPort = 8080
host = 'localhost'
serverSocket = socket(AF_INET, SOCK_STREAM)
# i think it binds to a local network by default #confirmed
# serverSocket.bind(('', serverPort))
serverSocket.bind((host, serverPort))

serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # connection socket has 2 other parameters, client 
    # ip and port if the client ip is different but same port it makes a new socket
    #
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()