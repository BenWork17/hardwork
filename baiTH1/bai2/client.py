import socket

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to server. Type 'exit' to quit.")
        
        while True:
            expression = input("Enter expression: ")
            if expression.lower() == 'exit':
                break
            
            s.sendall(expression.encode())
            response = s.recv(1024).decode()
            print("Result:", response)

if __name__ == "__main__":
    main()