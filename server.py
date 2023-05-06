import sys
import socket
from threading import Thread


class Server:
    def __init__(self):
        self.host = '0.0.0.0'  # allow any incoming connections
        self.port = 8888
        self.socket = socket.socket()

    @staticmethod  # this method is static because it does not use any of the server's attributes
    def on_new_client(client_socket, addr):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            # do some checks and if msg == someWeirdSignal: break:
            print(f"Data from {addr} >> {data}")
        client_socket.close()

    def listen(self):
        try:
            self.socket.bind((self.host, self.port))  # bind the socket to the port and ip address
            self.socket.listen(5)  # wait for new connections
            listening = True
        except:
            # print(f"Unable to start the server. Port {self.port} is already in use.")
            print(f"Unable to successfully start the server")
            listening = False
        return listening

    def start(self):
        while True:
            # work out how to keep looping
            listening = self.listen()
            if listening:
                print(f"Employee detail server is running locally, clients can connect on port {self.port}")
                break  # exit while loop once connected
            else:
                valid = False
                while not valid:
                    retry = input("Would you like to try starting the server again, Yes or No? ")
                    if retry in ['Y', 'YES', 'Yes', 'yes', 'y']:

                        valid_port = False
                        while not valid_port:
                            try:
                                port = int(input("Enter the port number you would like the server to run on: "))
                                valid_port = True
                                self.port = port
                            except ValueError:
                                print("Port must be a valid integer")
                            else:  # if the input is a valid integer, break the loop
                                break
                        valid = True

                    elif retry in ['N', 'NO', 'no', 'No', 'n']:
                        valid = True
                        print("Exiting program")
                        sys.exit()
                    else:
                        print("Invalid input! The answer can be 'Yes' or 'No'")

        while True:
            c, addr = self.socket.accept()  # Establish connection with client.
            # this returns a new socket object and the IP address of the client
            print(f"New connection from: {addr}")
            thread = Thread(target=self.on_new_client, args=(c, addr))  # create the thread
            thread.start()  # start the thread
        c.close()
        thread.join()


def main():
    server = Server()
    server.start()


if __name__ == '__main__':
    main()
