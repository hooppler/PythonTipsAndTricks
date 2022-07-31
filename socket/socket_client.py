# Socket Client Exampe
#
# Source: https://docs.python.org/3/library/socket.html
#
# socket library is part of standard Python library and should not be installed separatelly
#
# How to start client:
# 1. Open CMD
# 2. From cmd
#    ..> cd <path to file location>
# 3. From cmd start socket_client.py
#    ..> socket_client.py


import socket

HOST = 'localhost'        # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
