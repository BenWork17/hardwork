import socket
import re

def process_string(data):
    cleaned = data.strip()
    upper = cleaned.upper()
    lower = cleaned.lower()
    char_count = len(cleaned)  # đếm cả khoảng trắng và ký tự đặc biệt
    return f"Uppercase: {upper}\nLowercase: {lower}\nCharacter count: {char_count}"


def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Server is listening on port", port)

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode().strip()
                if not data:
                    continue
                upper, lower, word_count = process_string(data)
                response = f"{upper}\n{lower}\n{word_count}\n"
                conn.sendall(response.encode())

if __name__ == "__main__":
    main()