from socket import *
port = 7788 # Determine the port on 7788

# Create a socket and bind it to the server's address
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("localhost",port))
serverSocket.listen(1) # Listen for incoming connections
print("[STARING] the server is starting...")
while True:
    connectionSocket,addr=serverSocket.accept() # Accept a connection (the server is waiting for a client to connect)
    # Get the client's IP address and port
    ip=addr[0]
    port=addr[1]
    sentence=connectionSocket.recv(1024).decode() # Receive the request message and decode it
    print(sentence)
    # Parse the request to determine the requested file
    fileName = sentence.split('\n')[0]
    fileName = fileName.split(' ')[1]
    fileName=fileName.lstrip('/')

    try:
        if fileName == '' or fileName =='index.html' or fileName =='main_en.html' or fileName == 'en':# If the file is the main page, send the corresponding HTML file
            openFile = open("main-en.html", "rb")  # Open and read the requested file in byte format.
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) # the case of the request is ok
            connectionSocket.send("Content-Type: text/html \r\n".encode()) # the Content-Type will be text/html
            connectionSocket.send('\r\n'.encode())
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        elif fileName == 'ar': # If the file is the arabic version page, send the corresponding HTML file
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) # the case of the request is ok
            connectionSocket.send("Content-Type: text/html \r\n".encode()) # the Content-Type will be text/html
            connectionSocket.send('\r\n'.encode())
            openFile = open("main-ar.html", "rb")  # Open and read the requested file in byte format.
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        elif fileName.endswith('.html'): # If the file is anything.html page, send the corresponding HTML file
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) # the case of the request is ok
            connectionSocket.send("Content-Type: text/html \r\n".encode())# the Content-Type will be text/html
            connectionSocket.send('\r\n'.encode())
            try: # if the fileName is exist then it will opens
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read()) #open the HTML file
            except: # if not exist the other.html file will opens
                openFile = open("other.html", "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())#open the HTML file
            connectionSocket.close()

        elif fileName.endswith('.css'):# If the file is anything.css page, send the corresponding css file named style.css
            file="style.css"
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())# the case of the request is ok
            connectionSocket.send("Content-Type: text/css \r\n".encode())# the Content-Type will be text/css
            connectionSocket.send('\r\n'.encode())
            openFile = open(file, "rb")  # Open and read the requested file in byte format.
            connectionSocket.send(openFile.read()) #open the css file
            connectionSocket.close()

        elif fileName.endswith('.png'): # If the file is an image of .png, send the corresponding image png
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())# the case of the request is ok
            connectionSocket.send("Content-Type: image/png \r\n".encode())# the Content-Type will be image/png
            connectionSocket.send('\r\n'.encode())
            try :# if the fileName (which it is an image) is exist then it will opens
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())#open the image
            except:# if not exist the bzu.png image will opens
                openFile = open("images/bzu.png", "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())
                connectionSocket.close()

        elif fileName.endswith('.jpg'):
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())# the case of the request is ok
            connectionSocket.send("Content-Type: image/jpeg \r\n".encode())# the Content-Type will be image/jpeg
            connectionSocket.send('\r\n'.encode())
            try :# if the fileName (which it is an image) is exist then it will opens
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())#open the image
            except:# if not exist the Pudge.jpg image will opens
                openFile = open("images/Pudge.jpg", "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read())



        elif fileName == 'go':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())# the case of the request is Temporary Redirect
            connectionSocket.send(b"location: https://www.google.com/ \r\n") #  redirect to google website

            connectionSocket.close()

        elif fileName == 'so':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())# the case of the request is Temporary Redirect
            connectionSocket.send(b"location: https://www.stackoverflow.com \r\n") # redirect to stackoverflow website

            connectionSocket.close()

        elif fileName == 'bzu':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())# the case of the request is Temporary Redirect
            connectionSocket.send(b"location: https://www.birzeit.edu/ar \r\n") #  redirect to birzeit university website

            connectionSocket.close()
        else:
            #if the fileName not exist it will raise an error
            raise error
    except Exception as error:
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())# the case of the request is ok
        connectionSocket.send("Content-Type: text/html \r\n".encode())# the Content-Type will be text/html
        connectionSocket.send('\r\n'.encode())
        ErrorPage=("""<!DOCTYPE html>  <html lang="en">      <head>          <meta charset="utf-8"/>              <title>Error</title>      </head>      <style>       body        {          background: #bcefff;              background-image: -webkit-gradient(radial, 50% 50%, 0, 50% 50%,800);             padding-top: 5%;             padding-left: 40%;        }         img          {              width:250px;              height:250px;         }      .names{          margin-top: 50px;          margin-bottom: 50px;         }        </style>       <body>          <div class="error_page">                  <img src="images/404.jpg">                 <h1 style="color: red">The file is not found</h1>                     <div class="names">                  <p><b>Osaid Hamza - 1200875</b></p>                  <p><b>Dalia Hamza - 1180732</b></p>                 <p><b>Asma Romany - 1180989</b></p>             </div>     </body>      </html>"""+"""<div class="IpAndPort"><p><b>IP_CLIENT:"""+str(addr[0])+"</b></p><p><b>PORT_CLIENT:"+str(addr[1])+"</b></p></div>")
        connectionSocket.send(ErrorPage.encode()) # the error page that contains our names  and ip and port of the client will opened
        connectionSocket.close()
