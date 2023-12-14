import socket

HOST = "127.0.0.1"
PORT = 42424

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    user_input = ""
    while (user_input != "!quit"):
        user_input = input(" > ")
        if(user_input != ""):
            s.sendall(user_input.encode('utf-8'))
        else:
            s.sendall(b"")
        print(s.recv(1024))