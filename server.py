import socket
from threading import Thread


def on_new_client(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        # do some checks and if msg == someWeirdSignal: break:
        print(f"Data from {addr} >> {data}")
    client_socket.close()


def main():
    host = '0.0.0.0'  # allow any incoming connections
    port = 8888

    s = socket.socket()
    s.bind((host, port))  # bind the socket to the port and ip address

    s.listen(5)  # wait for new connections
    print(f"Employee detail server is running, clients can connect on port {port}")

    while True:
        c, addr = s.accept()  # Establish connection with client.
        # this returns a new socket object and the IP address of the client
        print(f"New connection from: {addr}")
        thread = Thread(target=on_new_client, args=(c, addr))  # create the thread
        thread.start()  # start the thread
    c.close()
    thread.join()


if __name__ == '__main__':
    main()
