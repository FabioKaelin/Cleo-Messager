import os
import socket
import sys


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(hostname)
print(local_ip)

# import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname())

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
print(local_ip)