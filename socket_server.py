import socket
"""
Implementiert einen einfachen Socket-Server
"""
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('127.0.0.214', 2400))
serversocket.listen(0)
try:
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
except KeyboardInterrupt:
    print('Abgebrochen')


clientsocket.close()
serversocket.close()
