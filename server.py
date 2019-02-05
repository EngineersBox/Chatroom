from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import configparser
from os.path import dirname, abspath

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument.
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def broadcast(msg, prefix=""):  #Prefix is for name identification.
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

clients = {}
adresses = {}

f_path = dirname(abspath(__file__))
config = configparser.ConfigParser()
config.read(f_path + '/config/config.ini')

try:
    HOST = config['server_cfg']['host_address']
except KeyError:
    HOST = '127.0.0.1'

try:
    PORT = int(config['server_cfg']['port'])
except KeyError:
    PORT = 33000

try:
    BUFSIZ = int(config['server_cfg']['buffsize'])
except KeyError:
    BUFSIZ = 1024

ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
