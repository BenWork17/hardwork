import socket
import re

def safe_evaluate(expression):
    # Loại bỏ ký tự nguy hiểm, chỉ giữ số và toán tử +-*/(). và khoảng trắng
    sanitized = re.sub(r'[^\d+\-*/().\s]', '', expression)
    
    try:
        # Kiểm tra tính hợp lệ của biểu thức
        if not re.match(r'^[\s\d+\-*/().]*$', sanitized):
            return "Error: Invalid expression"
        
        # Thực hiện tính toán
        result = eval(sanitized)
        return str(result)
    except:
        return "Error: Invalid expression"
def safe_evaluate(expression):
    # Thay thế các loại dấu gạch ngang khác thành dấu trừ chuẩn
    expression = expression.replace('–', '-').replace('—', '-')  # en dash, em dash
    sanitized = re.sub(r'[^\d+\-*/().\s]', '', expression)
    
    try:
        if not re.match(r'^[\s\d+\-*/().]*$', sanitized):
            return "Error: Invalid expression"
        
        result = eval(sanitized)
        return str(result)
    except:
        return "Error: Invalid expression"
def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server is listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode().strip()
                response = safe_evaluate(data)
                conn.sendall(response.encode())

if __name__ == "__main__":
    main()