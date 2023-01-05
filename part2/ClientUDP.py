from socket import *
import time
start_time=time.time()
serverName = '127.0.0.1'
port = 5566
clientSocket = socket(AF_INET, SOCK_DGRAM)
count=0

for x in range(1000001):
    clientSocket.sendto(str(x).encode(),(serverName,port))
    count+=1

end_time=time.time()
print(f"Sent {count} packets in {end_time - start_time:.5f} seconds.")

clientSocket.close()

