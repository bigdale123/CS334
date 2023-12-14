import socket
import random
import time

##########################
# Group Members:
#   Name: Brandon Pham
#     blazerID: vpham
#   Name: Dylan Calvin
#     blazerID: dylcal13
#########################

HOST = "172.24.183.229"
LISTEN_PORT = 3310

## Part 1: Connect & Send blazerID
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, LISTEN_PORT))
s.sendall("dylcal13".encode('utf-8'))


## Part 2: Get new port and create listener
LISTEN_PORT = int(s.recv(10))
print("Got New LISTEN_PORT: "+str(LISTEN_PORT))
s_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_2.bind(('',LISTEN_PORT))
s_2.listen(5)
print("Started new Listener on port: "+str(LISTEN_PORT))

s2_acpt, address = s_2.accept()


## Part 3: Do some stuff
data = str(s2_acpt.recv(24))
# Strip out UTF8 Garbage
data = data.replace("'","")
data = data.replace("b","")
# Split on comma and store values
data = data.split(",")
#print(data)
# Send data on new port
s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s3.bind(('',int(data[1])))
s3.sendto(str(random.randint(6,10)).encode(), (HOST,int(data[0])))

# Receive String
data_new, addr = s3.recvfrom(100)
data_new = str(data_new)
# Remove UTF8 Garbage
data_new = data_new.replace("b", "")
data_new = data_new.replace("'","")
print("Received Data from Robot: "+data_new)


## Part 4: Send back the string
for i in range(0,5):
    s3.sendto(data_new.encode(),(HOST,int(data[0])))
    time.sleep(1)
    print("UDP packet %d sent" %(i+1))