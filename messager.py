import os
import socket
import sys
import threading
import time

NameToIP = []

def get_ip_address(empfang):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((empfang, 80))
    return s.getsockname()[0]





def NameListener():
    global NameToIP

    end = "#END#"
    sep = "#SEP#"
    exitTag = "#EXIT#"
    nameTag = "#NAME#"
    messageTag = "#MES#"
    buffer = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]

    del s

    # try:
    while True:
        sserver = socket.socket()
        sserver.bind((local_ip, 9899))
        sserver.listen()
        client_socket, address = sserver.accept()

        message = ""
        while True:
            text = client_socket.recv(buffer).decode()
            message += text
            if end in text:
                break
        message = message.replace(end, "")
        if (nameTag in message):
            message = message.replace(sep, "")
            message = message.replace(nameTag, "")
            NameToIP.append([address[0], message])
        if (logoutTag in message):
            message = message.replace(sep, "")
            message = message.replace(logoutTag, "")
            NameToIP.remove([address[0], message])
        if (exitTag in message):
            if (address[0] == local_ip):
                exit()

        del sserver
        del client_socket
        del address
    # except:
    #     print("")
    #     print("Ende")




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
exitTag = "#EXIT#"
nameTag = "#NAME#"
messageTag = "#MES#"
logoutTag = "#LOGOUT#"
port = 9898
buffer = 1024
notende = True

def logoutIP9899():
    for x in range(2, 255):
        try:
            ip = local_ip
            ip = ip.split(".")
            empfang1 = str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(x)
            host = get_ip_address(empfang1)
            s = socket.socket()
            s.settimeout(0.001)
            s.connect((empfang1, 9899))
            s.send(bytes(logoutTag + sep + name + end, 'UTF-8'))
            s.close()
        except:
            x = "a"

def sayIP9898():
    for x in range(2, 255):
        try:
            ip = local_ip
            ip = ip.split(".")
            empfang1 = str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(x)
            host = get_ip_address(empfang1)
            s = socket.socket()
            s.settimeout(0.001)
            s.connect((empfang1, port))
            s.send(bytes(nameTag + sep + name + end, 'UTF-8'))
            s.close()
        except:
            x = "a"

def sayIP9899():
    for x in range(2, 255):
        try:
            ip = local_ip
            ip = ip.split(".")
            empfang1 = str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(x)
            host = get_ip_address(empfang1)
            s = socket.socket()
            s.settimeout(0.001)
            s.connect((empfang1, 9899))
            s.send(bytes(nameTag + sep + name + end, 'UTF-8'))
            s.close()
        except:
            x = "a"


x = threading.Thread(target=sayIP9898)
x.start()
z = threading.Thread(target=sayIP9899)
z.start()
y = threading.Thread(target=NameListener)
y.start()


# try:
while notende:

    empfang = input("Empfänger: ")
    if empfang == "":
        empfang = altEmpfang
        var = input("Nachricht: ")
    elif empfang == "ende":
        logoutIP9899()
        empfang = local_ip
        var = exitTag
        host = get_ip_address(empfang)
        host = empfang
        if end in var:
            print("Die Nachricht darf nicht #END# enthalten")
            exit(-1)
        if sep in var:
            print("Die Nachricht darf nicht #sep# enthalten")
            exit(-1)

        s = socket.socket()
        s.connect((host, 9899))
        s.send(bytes(logoutTag, 'UTF-8'))
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

        var = exitTag




        notende = False
        # break
    else:
        empfang = ""
        for x in NameToIP:
            if (x[1] == empfang):
                empfang = x[0]
                continue
        altEmpfang = empfang
        var = input("Nachricht: ")

    if var != "":
        host = get_ip_address(empfang)
        host = empfang
        if end in var:
            print("Die Nachricht darf nicht #END# enthalten")
            exit(-1)
        if sep in var:
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
