import socket

# threding implementation is pending

def run_client():
    # creating a socker object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.0.102"  # server IP address
    server_port = 8888 # server port number

    # establish connection with server

    client.connect((server_ip, server_port))

    try:
        while True:
            # getting input message from user and send it to the server
            msg = input("Enter message: ")
            
            # sending the messsage to the server after encoding it
            client.send(msg.encode('utf-8')[:1024])

            # receive message from the server
            response = client.recv(1024)  
            response = response.decode("utf-8")

            # if server send us "closed" in the payload, we break out of the loop and close our socket
            if response.lower() == "close":
                break

            print(f"Recived: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close client socket (connection to the server)
        client.close()
        print("Connection to server closed")


if __name__ == "__main__":
    run_client()

