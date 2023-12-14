import socket

HOST = "127.0.0.1"
PORT = 42424

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        user_input = ""
        print(str(addr)+" Connected.")
        while(user_input != "!quit"):
            user_input = input(" > ")
            if(input != ""):
                conn.sendall(user_input.encode('utf-8'))
                print("    Message Sent.")
            else:
                conn.sendall(b"")
            print(conn.recv(1024))
            
        