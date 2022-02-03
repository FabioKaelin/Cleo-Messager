import socket
import os

host = "0.0.0.0"
end = "#END#"
port = 9898
buffer = 1024

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

try:
    while True:
        s = socket.socket()
        s.bind((host, port))
        s.listen()

        client_socket, address = s.accept()
        message = ""
        while True:
            text = client_socket.recv(buffer).decode()
            if  end in text:
                message += text
                break
            print(message)
        message = message.replace(end, "")

        if address[0] == local_ip and message == "ende":
            exit(-1)
        print(str(address[0]) + ": " + str(message))

        client_socket.close()
        s.close()
        del s
        del client_socket
except:
    print("")
    print("Ende")