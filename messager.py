import os
import socket
import sys

def get_ip_address(empfang):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((empfang, 80))
    return s.getsockname()[0]


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
altEmpfang = local_ip
print("Eigene IP: " + local_ip)
name = input("Name: ")

sep = "#SEP#"
end = "#END#"
port = 9898
buffer = 1024



try:
    while True:

        empfang = input("Empfänger: ")
        if empfang == "":
            empfang = altEmpfang
            # print(empfang)

            altEmpfang = empfang
            var = input("Nachricht: ")
        elif empfang == "ende":
            empfang = local_ip
            var = "ende"
        else:
            altEmpfang = empfang
            var = input("Nachricht: ")

        if var != "":
            host = get_ip_address(empfang)
            if end in var:
                print("Die Nachricht darf nicht #END# enthalten")
                exit(-1)
            if sep in var:
                print("Die Nachricht darf nicht #sep# enthalten")
                exit(-1)

            s = socket.socket()
            s.connect((host, port))
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
            if var == "ende":
                exit(-1)
        else:
            print("Eine Nachricht wird benötigt")
except:
    print("Ende")