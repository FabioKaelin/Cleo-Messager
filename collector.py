import socket
import os
import threading
import time


def server():

    end = "#END#"
    sep = "#SEP#"
    exitTag = "#EXIT#"
    nameTag = "#NAME#"
    messageTag = "#MES#"
    logoutTag = "#LOGOUT#"
    port = 9898
    buffer = 1024


    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    print("Eigene IP: " + local_ip)

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
        # print(message)
        if (exitTag in message and address[0] == local_ip):
            if (address[0] == local_ip):

                message = message.replace(exitTag, "")
                message = message.replace(logoutTag, "")
                message = message.replace(sep, "")
                message = message.replace(nameTag, "")
                message = message.replace(messageTag, "")
                print(message + " ist ausgeloggt ")
                exit()
        if (logoutTag in message):
            message = message.replace(exitTag, "")
            message = message.replace(logoutTag, "")
            message = message.replace(sep, "")
            message = message.replace(messageTag, "")
            message = message.replace(nameTag, "")
            print(message + " ist ausgeloggt")
        if (messageTag in message):
            message = message.replace(messageTag, "")
            messagesplit = message.split(sep)

            client_socket.close()
            sserver.close



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


x = threading.Thread(target=server)
x.start()