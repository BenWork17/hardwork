import socket


def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("Enter a string: ")
        s.sendall(message.encode())
        data = s.recv(1024).decode().strip()
        if data:
            parts = data.split('\n')
            if len(parts) == 3:
                print(f"Uppercase: {parts[0]}")
                print(f"Lowercase: {parts[1]}")
                print(f"Word count: {parts[2]}")
            else:
                print("Invalid response from server")
        else:
            print("No data received")

if __name__ == "__main__":
    main()