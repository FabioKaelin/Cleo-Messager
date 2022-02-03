import os
import socket
import sys

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
ip = get_ip_address()

print("IP: " + ip)
varName = r"C:\Users\super\fabiokaelin\lehre\Cleo-Messager\files\text.txt"
var = "Ich bin fabio"
host = ip
end = "#END#"
port = 9898
buffer = 1024

if end in var:
    print("Das isch ä Wornig: #end# isch im Dateiname ErRRORRRRRRRRRR")
    exit(-1)

s = socket.socket()
s.connect((host, port))

while True:
    var_bytes = var[:buffer]
    var = var[buffer:]
    if var_bytes == "":
        s.sendall(bytes(end, 'UTF-8'))
        break
    s.sendall(bytes(var_bytes, 'UTF-8'))
    print(var_bytes)
s.close()
