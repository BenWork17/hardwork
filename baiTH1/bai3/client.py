import socket
import sys
import threading
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

def clear_line():
    """Xóa dòng hiện tại trong terminal"""
    print("\033[K", end="")
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
                
            # Xử lý hiển thị không bị chồng lên dòng nhập liệu
            sys.stdout.write("\033[F\033[K")  # Di chuyển lên dòng trước và xóa
            print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
            sys.stdout.write(f"{Fore.CYAN}> Your message: {Style.RESET_ALL}")
            sys.stdout.flush()
            
        except Exception as e:
            print(f"\n{Fore.RED}Connection error: {e}{Style.RESET_ALL}")
            break

import socket
import threading
import sys
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

def clear_line():
    """Xóa dòng hiện tại trong terminal"""
    print("\033[K", end="")

def receive_messages(sock):
    """Xử lý nhận tin nhắn"""
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
                
            # Di chuyển con trỏ lên và xóa dòng nhập liệu hiện tại
            sys.stdout.write("\033[F\033[K")
            
            # Xử lý tin nhắn hệ thống
            if message.startswith("[SYS]"):
                print(f"{Fore.RED}{message}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
                
            # Hiển thị lại dòng nhập liệu
            sys.stdout.write(f"{Fore.CYAN}> Your message: {Style.RESET_ALL}")
            sys.stdout.flush()
            
        except Exception as e:
            print(f"\n{Fore.RED}Error receiving message: {e}{Style.RESET_ALL}")
            break

def main():
    host = 'localhost'
    port = 12345

    print(f"{Fore.GREEN}=== CHAT CLIENT ==={Style.RESET_ALL}")
    
    # Nhập và validate nickname
    while True:
        nickname = input(f"{Fore.CYAN}Enter your nickname: {Style.RESET_ALL}").strip()
        if len(nickname) > 0 and len(nickname) <= 20:
            break
        print(f"{Fore.RED}Nickname must be 1-20 characters!{Style.RESET_ALL}")

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        
        # Gửi nickname đầu tiên
        client.send(nickname.encode())
        
        receive_thread = threading.Thread(
            target=receive_messages, 
            args=(client,), 
            daemon=True
        )
        receive_thread.start()
        
        print(f"\n{Fore.GREEN}Connected to chat server!{Style.RESET_ALL}")
        print(f"{Fore.RED}Type '/exit' to quit{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*30}{Style.RESET_ALL}\n")
        
        while True:
            try:
                message = input(f"{Fore.CYAN}> Your message: {Style.RESET_ALL}")
                clear_line()
                
                if message.lower() == '/exit':
                    break
                    
                if message.strip():
                    client.send(message.encode())
                    
            except KeyboardInterrupt:
                print("\nUse '/exit' to properly quit")
                continue
                
    except ConnectionRefusedError:
        print(f"\n{Fore.RED}Could not connect to server at {host}:{port}{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
    finally:
        try:
            client.close()
            print(f"\n{Fore.RED}Disconnected from server{Style.RESET_ALL}")
        except:
            pass

if __name__ == "__main__":

    main()