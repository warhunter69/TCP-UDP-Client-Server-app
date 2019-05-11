from socket import *

serverName = '127.0.69.69' #😉
serverPort = 16969 
#af_inet is ipv4
clientSocket = socket(AF_INET, SOCK_STREAM)
#the program assign a client port number by default,also the client ip kinda
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
# using the telnet program i figured out that
# i think the client port doesn't need 
# to be the same as the destination port 
# when it's speaking on reserved ports like 80