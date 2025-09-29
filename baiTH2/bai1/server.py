import socket

def process_string(data):
    cleaned = data.strip()
    upper = cleaned.upper()
    lower = cleaned.lower()
    char_count = len(cleaned)
    return f"{upper}\n{lower}\n{char_count}"

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP Server listening on {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            
            if not data:
                continue
                
            response = process_string(data.decode())
            s.sendto(response.encode(), addr)

if __name__ == "__main__":
    main()