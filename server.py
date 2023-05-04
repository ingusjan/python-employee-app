import socket


def main():
    host = '0.0.0.0'  # allow any incoming connections
    port = 8888

    s = socket.socket()
    s.bind((host, port))  # bind the socket to the port and ip address

    s.listen(1)  # wait for new connections
    print(f"Server is running, machines can connect on port {port}")
    c, addr = s.accept()  # accepts the incoming connection
    # this returns a new socket object and the IP address of the client
    print(f"New connection from: {addr}")

    while True:
        data = c.recv(1024).decode('utf-8')  # accepts data from the client
        if not data:
            break
        print(f"Incoming data: {data}")
        data = data.upper()
        c.send(data.encode('utf-8'))
    c.close()


if __name__ == '__main__':
    main()