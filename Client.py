import socket
import time

PORT = 5050
SERVER = "YOUR_SERVER_ADDRESS"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return
    
    connection = connect()
    while True:
        
        if (msg := input("Message (q for quit): ")) == 'q':
            break
        
        send(connection, msg)
    
    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()
