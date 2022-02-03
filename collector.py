import socket
import os

end = "#END#"
sep = "#SEP#"
port = 9898
buffer = 1024

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# try:
while True:
    s = socket.socket()
    s.bind((local_ip, port))
    s.listen()

    client_socket, address = s.accept()
    message = ""
    while True:
        text = client_socket.recv(buffer).decode()
        message += text
        if  end in text:
            break
    message = message.replace(end, "")
    messagesplit = message.split(sep)

    client_socket.close()
    s.close

    if address[0] == local_ip and messagesplit[1] == "ende":
        break

    print(messagesplit[0] + ": " + messagesplit[1])
    del s
    del client_socket
    del address
# except:
#     print("")
#     print("Ende")