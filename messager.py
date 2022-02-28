import os
import socket
import sys

def get_ip_address(empfang):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((empfang, 80))
    # print(s)
    return s.getsockname()[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]

del s
altEmpfang = local_ip
print("Eigene IP: " + local_ip)
name = input("Name: ")
print("")

sep = "#SEP#"
end = "#END#"
nameTag = "#NAME#"
messageTag = "#MES#"
port = 9898
buffer = 1024
notende = True

for x in range(2, 255):
    try:
        ip = local_ip
        ip = ip.split(".")
        empfang1 = str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(x)
        print(empfang1)
        host = get_ip_address(empfang1)
        s = socket.socket()
        s.settimeout(0.1)
        s.connect((empfang1, port))
        # print(host)
        s.send(bytes(nameTag + sep + name + end, 'UTF-8'))
        s.close()
    except:
        x = "a"



# try:
while notende:

    empfang = input("Empfänger: ")
    if empfang == "":
        empfang = altEmpfang
        # print(empfang)
        var = input("Nachricht: ")
    elif empfang == "ende":
        empfang = local_ip
        var = "ende"
        notende = False
    else:
        altEmpfang = empfang
        var = input("Nachricht: ")

    if var != "":
        host = get_ip_address(empfang)
        # print(host)
        host = empfang
        # print(host)
        if end in var:
            print("Die Nachricht darf nicht #END# enthalten")
            exit(-1)
        if sep in var:
            #172.20.107.85
            print("Die Nachricht darf nicht #sep# enthalten")
            exit(-1)

        s = socket.socket()
        s.connect((host, port))
        s.send(bytes(messageTag, 'UTF-8'))
        s.send(bytes(name, 'UTF-8'))

        s.send(bytes(sep, 'UTF-8'))

        while True:
            var_bytes = var[:buffer]
            var = var[buffer:]
            if var_bytes == "":
                s.sendall(bytes(end, 'UTF-8'))
                break
            s.sendall(bytes(var_bytes, 'UTF-8'))
        s.close()
        print("")
    else:
        print("Eine Nachricht wird benötigt")
# except:
#     print("Ende")
