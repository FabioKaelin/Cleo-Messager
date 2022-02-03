import socket
import os

host = "0.0.0.0"
end = "#END#"
port = 9898
buffer = 1024

s = socket.socket()
s.bind((host, port))
s.listen(5)
print("Server open...")

client_socket, address = s.accept()
print("IP: " + str(address))
# file, file_size = client_socket.recv(buffer).decode().split(sep)
# print(file + " ___" + file_size)

message = ""

# text = client_socket.recv(buffer).decode()
# print(text)

while True:
    text = client_socket.recv(buffer).decode()
    if  end in text:
        message += text
        break
    print(message)
message = message.replace(end, "")
print(message)

# file_name = os.path.basename(file)
# file_size = int(file_size)
# with open(file_name, "wb") as f:
#     bytes_recv = client_socket.recv(buffer)
#     while bytes_recv:
#         f.write(bytes_recv)
#         # print(len(bytes_recv))
#         bytes_recv = client_socket.recv(buffer)

client_socket.close()
s.close()