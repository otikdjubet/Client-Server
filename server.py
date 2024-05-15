import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()
    print('Server is listening...')

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'Received: {data.decode()}')
                conn.sendall(data)  # Echo the received data

if __name__ == "__main__":
    start_server()
