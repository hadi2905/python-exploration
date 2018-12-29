import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('192.168.0.10', 54000))
serversocket.listen(0)

(clientsocket, adress) = serversocket.accept()
print('client connected')


while True:
    msg= clientsocket.recv(1024)
    msg = msg.decode()
    print(msg)

    ans = "Server hat folgende Anfrage bekommen: " + msg
    print(ans)
    ans = ans.encode()
    clientsocket.send(ans)

clientsocket.close()
serversocket.close()
/usr/bin