import socket
import tkinter as tk
from tkinter import messagebox

def send_message():
    global message_count  # Track the number of messages sent
    message = entry_message.get()
    if not message:
        messagebox.showwarning("Warning", "Please enter a message.")
        return
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 65432))
        client_socket.sendall(message.encode('utf-8'))
        
        data = client_socket.recv(1024)
        messagebox.showinfo("Received", f'Received: {data.decode()}')
        
        message_count += 1  # Increment message count after sending a message
        if message_count >= MAX_MESSAGES:  # Close connection after reaching the maximum message count
            client_socket.close()
            root.destroy()  # Close the GUI window
    except Exception as e:
        messagebox.showerror("Error", f'Failed to connect: {e}')

# Constants
MAX_MESSAGES = 5  # Maximum number of messages to send

# Initialize message count
message_count = 0

# Setting up the GUI
root = tk.Tk()
root.title("Client Application")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter Message:")
label.pack(side=tk.LEFT)

entry_message = tk.Entry(frame)
entry_message.pack(side=tk.LEFT)

btn_connect = tk.Button(frame, text="Send to Server", command=send_message)
btn_connect.pack(side=tk.LEFT)

root.mainloop()
