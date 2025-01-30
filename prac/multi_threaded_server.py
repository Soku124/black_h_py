import socket
import threading





def handle_client(client_socket, addr):
    try:
        while True:
            # receive and print client messages
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == "close":
                client_socket.send("close".encode("utf-8"))
                break

            print(f"Received: {request}")

            # converting and sending accepted response to the client
            response = "accepted"

            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Erro rwhen handling client: {e}")
    finally:
        client_socket.close()
        print(f'Connection to client ({addr[0]}:{addr[1]}) closed.')




def run_server():
    server_ip = "192.168.0.102" # server IP address
    port  = 8888 # server port number

    # creaing a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # binding the socket to the host and port
        server.bind((server_ip, port))

        #listening for the incoming connections
        server.listen()

        print(f"Listning on {server_ip}:{port}")

        while True:
            # accepting a client connection
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")

            # start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket,addr))
            thread.start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()


if __name__ == "__main__":
    run_server()