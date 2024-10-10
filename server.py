import socket
import threading

def main():
    #Get host and port
    host = input("Host: ")
    port = int(input("Port: "))

    #Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)






main()
