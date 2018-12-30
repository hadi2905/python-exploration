import socket
"""
Implementiert einen einfachen Socket-Client
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.214', 2400))

while True:
    msg = str(input('Eingabe?'))
    msg = msg.encode()
    s.send(msg)

    msg = s.recv(1024)
    msg = msg.decode()
    print('Server antwortet: ' + msg)

s.close()

