from socket import *
import time

port=5566
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', port))
print("[STARING] the server is starting...")
count = 0
while True:
    message,adddress = serverSocket.recvfrom(1024)
    print(message)
    if count==0:
        start_time = time.time()
    count+=1
    if message==b'1000000':
        break

end_time=time.time()
print(f"Received {count} packets in {end_time - start_time:.5f} seconds.")



