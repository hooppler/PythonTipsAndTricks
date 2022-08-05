# Socket Client HTTP Exampe
#
# How to send HTTP request and get HTTP response using socket.
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

http_request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

data = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('www.google.com', 80))
    s.sendall(http_request.encode())
    http_response = repr(s.recv(1024))

print('Sent HTTP request:')
print(http_request)

print('Received HTTP response:', http_response)
