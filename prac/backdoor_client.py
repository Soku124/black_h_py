import socket


# def receive_data(server_socket):
#     data = ""
#     while True:
#         response = server_socket.recv(4096).decode("utf-8")
#         if len(response) < 4096:
#             break
#         data += response
#     print(data)


# def send_data(server_socket):
#     data = input(">> ")

#     server_socket.send(data.encode("utf-8"))




# def run_client():
#     server_ip = "192.168.112.159"
#     server_port = 8888


#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     server_socket.connect((server_ip, server_port))

#     while True:
#         receive_data(server_socket=server_socket)
        

#         send_data(server_socket=server_socket)

        



# run_client()
                       

def recieve_data(client_socket):
    response = ""

    while True:
        data = client_socket.recv(4096).decode("utf-8")

        response += data

        if len(data) < 4096:
            break

        

    return response 




def main():
    server_ip = "192.168.0.105"
    server_port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_ip, server_port))


    while True:
        response = recieve_data(client_socket=client_socket)

        print(response)

        send_data = f"Accepted: {response}"

        client_socket.send(send_data.encode("utf-8"))

main()