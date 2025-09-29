import socket
import re

def safe_evaluate(expression):
    expression = expression.replace('–', '-').replace('—', '-')
    sanitized = re.sub(r'[^\d+\-*/().\s]', '', expression)
    
    try:
        if not re.match(r'^[\s\d+\-*/().]*$', sanitized):
            return "Error: Invalid expression"
        return str(eval(sanitized))
    except:
        return "Error: Invalid expression"

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP Calculator Server listening on {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            expression = data.decode().strip()
            print(f"Received from {addr}: {expression}")
            
            if expression.lower() == 'exit':
                break
                
            response = safe_evaluate(expression)
            s.sendto(response.encode(), addr)

if __name__ == "__main__":
    main()