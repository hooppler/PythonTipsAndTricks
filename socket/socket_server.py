# Socket Server Exampe
#
# Source: https://docs.python.org/3/library/socket.html
#
# socket library is part of standard Python library and should not be installed separatelly
#
# How to start server:
# 1. Open CMD
# 2. From cmd
#    ..> cd <path to file location>
# 3. From cmd start socket_server.py
#    ..> socket_server.py
#
# NOTE: To stop server use Ctrl + Pause/Break


import socket

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print('Socket server is started and listening. Host: {} Port: {}'.format(HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
