import pickle
import sys

state = {}

def handle_view_requests(server_socket):
    """Handles the '/viewRequests' command."""
    server_socket.send(b".")
    response = server_socket.recv(1024).decode("utf-8")
    if response == "/sendingData":
        server_socket.send(b"/readyForData")
        data = pickle.loads(server_socket.recv(1024))
        if data == set():
            print("Received empty data set.")
        else:
            print(f"Data received: {data}")
        return True
    return False

def listen_to_server(server_socket):
    """Main server listener function."""
    while True:
        try:
            msg = server_socket.recv(1024).decode("utf-8")
            if msg == "/viewRequests":
                if handle_view_requests(server_socket):
                    continue
            # Add other message handling logic as needed
            else:
                print(f"Unhandled message: {msg}")
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
