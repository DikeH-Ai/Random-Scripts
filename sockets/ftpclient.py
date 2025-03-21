import socket

# intantiate client socket connection
client = socket.socket()
# connect to server
client.connect(("localhost", 5101))

while True:
    # pass filename to server
    message = input("Filename: ")
    if message == "q":
        break
    client.send(message.encode())
    data = client.recv(5000)
    if not data:
        break
    with open("recv", "wb") as file:
        file.write(data)
    print("Successfully received")
client.close()
