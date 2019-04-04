import socket
from time import sleep
from threading import Thread

clients = {}
messages = []

def beta(s,addr):
    while True:
        sleep(3)
        global messages
        try:
            if(messages[0] == None):
                pass
            for msg in messages:
                broadcast_message(msg,s,addr[0])
                messages.remove(msg)
        except IndexError:
            pass

def start_broadcast_server():
    ip = "142.93.197.240"
    port = 2000
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.bind((ip,port))
    ss.listen()

    while True:
        client,addr = ss.accept()
        t = Thread(target=beta,args=(client,addr))
        t.start()

def broadcast_message(msg,s,addr):
    s.send(msg.encode())
    sleep(1)
    s.send(str(addr).encode())

def handler(client,addr):
    global clients,messages
    clients[addr] = client
    print(clients)
    #client.send("WELCOME".encode())
    while True:
        message = client.recv(409600).decode()
        messages.append(message)

def main():
    ip = "142.93.197.240"
    port = 2003
    address = (ip,port)

    relay_thread = Thread(target=start_broadcast_server,args=())
    relay_thread.start()

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(address)
    s.listen()
    print("[*] Server started!")

    while True:
        client,addr = s.accept()
        handler(client,str(addr[0]))

if __name__ == '__main__':
    main()
