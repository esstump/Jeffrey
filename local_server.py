import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for connection')
    connection,client_address = sock.accept()

    try:
        print('connection from', client_address)

        while True:
            data =connection.recv(16)
            print('received "%s"' % data)
            if data == 'quit':
                break
            else:
                print("%s", data)

    finally:
        connection.close()
