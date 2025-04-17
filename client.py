import socket
import threading

# Server's IP address and port
SERVER_HOST = "0.0.0.0"  # Change this to the server's IP if running on a different machine
SERVER_PORT = 5002
separator_token = "<SEP>"  # Token to separate client name and message

# Create a TCP socket
client_socket = socket.socket()

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

def listen_for_messages():
    """
    This function keeps listening for messages from the server
    and prints them to the console.
    """
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
            else:
                # If no message is received, the server might have closed the connection
                print("[!] Server closed the connection.")
                break
        except Exception as e:
            print(f"[!] Error: {e}")
            break

# Start a thread to listen for messages from the server
threading.Thread(target=listen_for_messages, daemon=True).start()

# Main loop to send messages to the server
while True:
    # Get user input
    message = input()
    if message.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'
    
    # Send the message to the server
    client_socket.send(f"Client{separator_token}{message}".encode())

# Close the client socket
client_socket.close()