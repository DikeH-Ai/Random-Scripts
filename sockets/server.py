# import socket module
import socket

# Server program
# instantiate socket/server object
server = socket.socket()
# bind server object to hostname, port
port = 5005
server.bind(("192.168.38.218", port))
# listen for incoming connections
server.listen()
# accept incoming connections
conn, address = server.accept()
print("Connection from " + str(address))
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = str(data)
    print("from client: " + data)
    message = input("To client: ")
    conn.send(message.encode())
conn.close()
