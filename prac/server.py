import socket


def run_server():

    # Creating a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.112.159"
    port = 8888


    # binding the socket to a specific address and port
    server.bind((server_ip, port))

    # listening for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accepting incoming connections
    client_socket, client_adress = server.accept()
    print(f"Accepted connection from {client_adress[0]}:{client_adress[1]}")

    # receiving data from the client
    while True:
        request =  client_socket.recv(1024)
        request = request.decode("utf-8")  # converting bytes to sting

        # if we received "close" from the client, then we break
        # out of the loop and close the connection

        if request.lower() == "close":
            # send response to the client which acknowledge that the
            # conneciton should be closed and break out of the loop

            client_socket.send("closed".encode("utf-8"))
            break
        
        print(f"Received: {request}")

        response = "accepted".encode("utf-8") # converting string into bytes
        # converting and sending accept response to the client
        client_socket.send(response)

    # closing connection socket with the client
    client_socket.close()
    print("Connection to client")
    server.close()

run_server()

