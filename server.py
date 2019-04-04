import socket
from time import sleep
from threading import Thread

clients = {}
messages = []

def start_broadcast_server():
    ip = "127.0.0.1"
    port = 2000
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.bind((ip,port))
    ss.listen()
    while True:
        sleep(3)
        global messages
        try:
            if(messages[0] == None):
                pass
            for msg in messages:
                broadcast_message(msg)
        except IndexError:
            pass


def broadcast_message(msg):
    global messages
    for client in clients:
        clients[client].send(msg.encode())
        sleep(1)
        clients[client].send(str(client).encode())
    print("[*] Message : %s broadcasted"%(msg))

def handler(client,addr):
    global clients
    clients[addr] = client
    client.send("WELCOME".encode())
    while True:
        message = client.recv(409600).decode()
        messages.append(message)

def main():
    ip = "127.0.0.1"
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
