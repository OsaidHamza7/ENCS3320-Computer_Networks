from socket import *
import time
Socket_Server_TCP= socket(AF_INET, SOCK_STREAM)
port=5566
server_address = ('', port)
print("[STARING] the server is starting...")
Socket_Server_TCP.bind(server_address)
Socket_Server_TCP.listen(1)
count = 0
start_time=time.time()
connection, address = Socket_Server_TCP.accept()
print("IP: " + address[0] + ", Port: " + str(address[1])) # get an ip and port

while True:
    data = connection.recv(len(str(count)))
    if not data:
        break
    else:
        count += 1
        print(data)


connection.close()
end_time = time.time()
print("[FINISH] the server is finishing...")
print(f"Received {count} packets in {end_time - start_time:.3f} seconds.")