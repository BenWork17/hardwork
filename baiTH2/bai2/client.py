import socket

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print("UDP Calculator Client. Type 'exit' to quit.")
        
        while True:
            expression = input("Enter expression: ")
            if expression.lower() == 'exit':
                break
                
            s.sendto(expression.encode(), (host, port))
            data, _ = s.recvfrom(1024)
            print("Result:", data.decode())

if __name__ == "__main__":
    main()