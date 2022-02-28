import socket
import os

end = "#END#"
sep = "#SEP#"
nameTag = "#NAME#"
messageTag = "#MES#"
port = 9898
buffer = 1024

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# local_ip = s.getsockname()[0]
# print(local_ip)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
print(local_ip)

del s

# try:
while True:
    sserver = socket.socket()
    sserver.bind((local_ip, port))
    sserver.listen()

    client_socket, address = sserver.accept()
    message = ""
    while True:
        text = client_socket.recv(buffer).decode()
        message += text
        if  end in text:
            break
    message = message.replace(end, "")
    if (messageTag in message):
        message = message.replace(messageTag, "")
        messagesplit = message.split(sep)

        client_socket.close()
        sserver.close

        if address[0] == local_ip and messagesplit[1] == "ende":
            break

        print(messagesplit[0] + ": " + messagesplit[1])
    elif (nameTag in message):
        message = message.replace(sep, "")
        message = message.replace(nameTag, "")
        print(address[0] + " ist " + message)

    del sserver
    del client_socket
    del address
# except:
#     print("")
#     print("Ende")