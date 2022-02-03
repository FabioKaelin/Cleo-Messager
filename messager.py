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


try:
    while True:

        empfang = input("Empfänger: ")
        if empfang == "":
            empfang = altEmpfang
            # print(empfang)

            altEmpfang = empfang
            var = input("Nachricht: ")
        elif empfang == "ende":
            var = "ende"
        else:
            altEmpfang = empfang
            var = input("Nachricht: ")

        if var != "":
            host = get_ip_address(empfang)
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
            s.close()
            print("")
            if var == "ende":
                exit(-1)
        else:
            print("Bitte eine Nachricht")
except:
    print("Ende")