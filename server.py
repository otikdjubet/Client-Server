import socket
import tkinter as tk
import threading

def start_server():
    def server_thread():
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

    # Start the server in a separate thread
    server_thread = threading.Thread(target=server_thread)
    server_thread.start()

# Function to start the server when the button is clicked
def on_button_click():
    start_server()
    btn_start_server.config(state=tk.DISABLED)  # Disable the button after starting the server
    label_status.config(text="Server started")

# Create the GUI
root = tk.Tk()
root.title("Server Controller")

frame = tk.Frame(root)
frame.pack(pady=20)

btn_start_server = tk.Button(frame, text="Start Server", command=on_button_click)
btn_start_server.pack()

label_status = tk.Label(frame, text="")
label_status.pack()

root.mainloop()
