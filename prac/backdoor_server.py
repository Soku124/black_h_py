import socket
import threading


# def receive_data(client_socket):
#     data = ""
#     while True:
#         response = client_socket.recv(4096)
#         if len(response) < 4096:
#             break
#         data += response.decode("utf-8")
#     return data

# def send_data(client_socket):
#     data = input(">> ")

#     client_socket.send(data.encode("utf-8"))


# def client_handler(client_socket, addr):
#     try:
#         while True:
#             send_data(client_socket=client_socket)

#             reponse = receive_data(client_socket=client_socket)

#             print(reponse+"\n")

            

#     except Exception as e:
#         print(f"Error occured: {e}")
#     finally:
#         client_socket.close()
#         print(f"Connection to client {addr[0]}:{addr[1]} closed.")






# def run_server():
#     server_ip = "192.168.112.159"
#     server_port = 8888

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#     print(f"Binding socket with: {server_ip}:{server_port}")
#     server_socket.bind((server_ip, server_port))
    
#     print(f"Listening for incomming connection")
#     server_socket.listen(0)


#     while True:

#         client_socket, addr = server_socket.accept()

#         print(f" Got connection from: {addr[0]}:{addr[1]}")

#         thread = threading.Thread(target=client_handler, args=(client_socket, addr))
#         thread.start()

# run_server()


def recieve_data(client_socket):
    response = ""

    while True:
        data = client_socket.recv(4096).decode("utf-8")

        response += data

        if len(data) < 4096:
            break

        

    return response 

def handle_client(client_socket, addr):

    while True:
        data = input(f"[{addr[0]}] >> ").encode("utf-8")

        client_socket.send(data)

        response = recieve_data(client_socket=client_socket)

        print(response)

def main():
    server_ip = "192.168.0.105"
    server_port = 8888


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_ip, server_port))
    server_socket.listen(0)

    print("Listening for incomming connection......")

    while True:

        client_socket, addr = server_socket.accept()

        print(f"Got connetion from: {addr[0]}:{addr[1]}")
        
        thread = threading.Thread(target=handle_client, args=(client_socket,addr))
        thread.start()


main()