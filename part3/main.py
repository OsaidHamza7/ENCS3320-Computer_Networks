from socket import *
port = 7788
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",port))
serverSocket.listen(1)
print("[STARING] the server is starting...")
while True:
    connectionSocket,addr=serverSocket.accept()
    ip=addr[0]
    port=addr[1]
    sentence=connectionSocket.recv(1024).decode()
    print(sentence)
    fileName = sentence.split('\n')[0]
    fileName = fileName.split(' ')[1]
    fileName=fileName.lstrip('/')

    try:
        if fileName == '' or fileName =='index.html' or fileName =='main_en.html' or fileName == 'en':
            openFile = open("main-en.html", "rb")  # Open and read the requested file in byte format.
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        elif fileName == 'ar':
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            openFile = open("main-ar.html", "rb")  # Open and read the requested file in byte format.
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        elif fileName.endswith('.html'):
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            try:
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())
            except:
                openFile = open("other.html", "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())
            connectionSocket.close()

        elif fileName.endswith('.css'):
            file="style.css"
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/css \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            openFile = open(file, "rb")  # Open and read the requested file in byte format.
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        elif fileName.endswith('.png'):
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: image/png \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            try :
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())
            except:
                openFile = open("images/bzu.png", "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())
                connectionSocket.close()

        elif fileName.endswith('.jpg'):
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            try :
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())
            except:
                openFile = open("images/Pudge.jpg", "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())



        elif fileName == 'go':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send(b"location: https://www.google.com/ \r\n")
            connectionSocket.close()

        elif fileName == 'so':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send(b"location: https://www.stackoverflow.com \r\n")
            connectionSocket.close()

        elif fileName == 'bzu':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send(b"location: https://www.birzeit.edu/ar \r\n")
            connectionSocket.close()
        else:
            raise error

    except Exception as error:
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send('\r\n'.encode())
        ErrorPage=("""<!DOCTYPE html>  <html lang="en">      <head>          <meta charset="utf-8"/>              <title>Error</title>      </head>      <style>       body        {          background: #bcefff;              background-image: -webkit-gradient(radial, 50% 50%, 0, 50% 50%,800);             padding-top: 5%;             padding-left: 40%;        }         img          {              width:250px;              height:250px;         }      .names{          margin-top: 50px;          margin-bottom: 50px;         }        </style>       <body>          <div class="error_page">                  <img src="images/404.jpg">                 <h1 style="color: red">The file is not found</h1>                     <div class="names">                  <p><b>Osaid Hamza - 1200875</b></p>                  <p><b>Dalia Hamza - 1180732</b></p>                 <p><b>Asma Romany - 1180989</b></p>             </div>     </body>      </html>"""+"""<div class="IpAndPort"><p><b>IP_CLIENT:"""+str(addr[0])+"</b></p><p><b>PORT_CLIENT:"+str(addr[1])+"</b></p></div>")
        connectionSocket.send(ErrorPage.encode())
        connectionSocket.close()
