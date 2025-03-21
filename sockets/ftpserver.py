import socket
# instantiate server socket object
server = socket.socket()
# bind server socket object
server.bind(("localhost", 5101))
# listen for incoming connections
server.listen()
# accept connection
connection, address = server.accept()

while True:
    filename = connection.recv(1024).decode()
    if not filename:
        break
    data = None
    with open(filename, "rb") as file:
        data = file.read()
    if data:
        print("Sending data")
        connection.send(data)
        print("file transfered")
connection.close()
