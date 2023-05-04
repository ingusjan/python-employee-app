import socket


def main():
    host = '127.0.0.1'  # server ip address
    port = 8888  # port of the server

    s = socket.socket()
    s.connect((host, port))  # bind the socket to the port and ip address

    message = input(f"Connected to the server, input a message:")
    while message != 'q':
        s.send(message.encode('utf-8'))  # sending data over the socket

        response = s.recv(1024).decode('utf-8')
        print(f"Response from the server: {response}")
        message = input('->')

    s.close()  # close connection to the server


if __name__ == '__main__':
    main()