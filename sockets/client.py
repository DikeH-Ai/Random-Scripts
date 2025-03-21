# import socket
import socket

# client socket
# instantiate client socket obj
client_server = socket.socket()
# connect to server socket
client_server.connect(("192.168.38.218", 5005))
# send data and recieve response
message = input("to Sever: ")
while message != "q":
    client_server.send(message.encode())
    data = client_server.recv(1024).decode()
    print("from server: " + data)
    message = input("to Sever: ")
client_server.close()
