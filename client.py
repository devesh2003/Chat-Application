import socket
from threading import Thread

def receive(s):
    ip = "142.93.197.240"
    port = 2000

    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.connect((ip,port))

    while True:
        msg = ss.recv(409600).decode()
        addr = ss.recv(1024).decode()
        print("\n%s: %s"%(msg,addr))
        print(">>")

def main():
    ip = "142.93.197.240"
    port = 2003
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("[*] Connecting to server...")
    s.connect((ip,port))
    print("[*] Connected")
    receiver_thread = Thread(target=receive,args=(s,))
    receiver_thread.start()
    while True:
        msg = input(">>")
        s.send(msg.encode())

if __name__ == '__main__':
    main()
