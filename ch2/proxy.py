import sys
import socket
import threading

HEX_FILTER = ''.join(
    [ (len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)]
)

def hexdump(src, length =16, show=True):
    if isinstance(src, bytes):
        src=src.decode()

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        
        printtable = word.translate(HEX_FILTER)
        hexa = ' '.join([f' {ord(c):02x} for c in word'])
        hexwidth = length*3

        results.append(f'{i:04x} {hexa:<{hexwidth}}
                        {printtable}' )
        
        if show:
            for line in results:
                print(line)
        else:
            return results


def receive_from(connection):
    buffer  = b""

    connection.settimeout(5)

    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data

    except Exception as e:
        pass
    return buffer


def request_handler(buffer):
    # Perform packet modifications
    return buffer

def response_handler(buffer):
    # perform packet modification
    return buffer


def proxy_handler(client_socket, remote_host, remote_port, recive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    remote_socket.connect((remote_host, remote_port))

    if recive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

    remote_buffer = response_handler(remote_buffer)
    if len(remote_buffer):
        print(f"[<==] Sending {len(remote_buffer)} bytes to localhost.")
        client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            line = f"[==>] Received {len(local_buffer)} bytes from localhost."
            print(line)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)

            remote_socket.send(local_buffer)
            print("[==>] Send to remote.")

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print(f"[<==] Received {len(remote_buffer)} bytes from remote.")
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] Send to localhost.")

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print(f'problem on bind: {e}')

        print(f"[!!] Failed to listen on {local_host, local_port}")

        print(f"[!!] Check for other listening sockets or correct permissions.")
        sys.exit(0)

    print(f"[*] Listening on {local_host, local_port}")

    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        #print out the local connection information
        line = f"> Received incoming connection from {addr[0], addr[1]}"
        print(line)

        # start a thread to talk to the remote host

        proxy_thread = threading.Thread(
            target=proxy_handler,
            args=(client_socket, remote_host, remote_port, receive_first)
        )

        proxy_thread.start()



