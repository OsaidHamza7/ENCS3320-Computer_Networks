from socket import *
import time
Socket_Client_TCP= socket(AF_INET,SOCK_STREAM)
port=5566
server_address = ('192.168.1.71', port)
print(f'Connecting to {server_address}')
Socket_Client_TCP.connect(server_address)
count=0
start_time = time.time()

for i in range(1000001):
    msg=str(i).encode()
    Socket_Client_TCP.sendall(str(i).encode())
    print(msg)
    count+=1


Socket_Client_TCP.close()
end_time = time.time()
print(f"Sent {count} packets in {end_time - start_time:.3f} seconds.")




