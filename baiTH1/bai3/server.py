import socket
import threading
import time

clients = []
lock = threading.Lock()
nicknames = {}
chat_history = [] 


def handle_client(client_socket, addr):
    global clients
    try:
        # Nhận nickname đầu tiên
        nickname = client_socket.recv(1024).decode()
        nicknames[client_socket] = nickname
                # Gửi toàn bộ lịch sử chat
        for msg in chat_history:
            client_socket.send(msg.encode())
            time.sleep(0.1)  # Tránh bị tràn bộ đệm
        while True:
            message = client_socket.recv(1024).decode()
            if not message or message.lower() == 'exit':
                break
                
            print(f"Received from {nickname}: {message}")
            broadcast(message, client_socket, nickname)
            
    except ConnectionResetError:
        print(f"{nickname} disconnected unexpectedly")
    finally:
        with lock:
            if client_socket in clients:
                clients.remove(client_socket)
            if client_socket in nicknames:
                del nicknames[client_socket]
        client_socket.close()

def broadcast(message, sender_socket, sender_nickname):
    global chat_history
    formatted_msg = f"{sender_nickname}: {message}"
    chat_history.append(formatted_msg)  # Lưu vào lịch sử
    
    with lock:
        for client in clients:
            try:
                client.send(formatted_msg.encode())
            except:
                client.close()
                clients.remove(client)

def main():
    host = 'localhost'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Chat Server is listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        with lock:
            clients.append(client_socket)
        print(f"New connection from {addr}")
        client_thread = threading.Thread(
            target=handle_client, 
            args=(client_socket, addr)
        )
        client_thread.start()

if __name__ == "__main__":
    main()