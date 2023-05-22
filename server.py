import os
import csv
import sys
import json
import socket
from threading import Thread


class Server:
    def __init__(self):
        self.host = '0.0.0.0'  # allow any incoming connections
        self.port = 8888
        self.socket = socket.socket()
        self.json_filename = "employee_data.csv"  # using csv file rather than json because the headers are pre-defined and constant
        self.json_headers = ['first_name', 'last_name', 'age', 'employed']
        # check if the file exists, if it doesn't add the headers
        if not os.path.exists(self.json_filename):
            f = open(self.json_filename, 'w')
            writer = csv.writer(f)
            writer.writerow(self.json_headers)
            f.close()

    def on_new_client(self, client_socket, addr):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            print(f"Saving data from {addr}")
            json_data = json.loads(data)
            saved_data = [json_data['first_name'], json_data['last_name'], json_data['age'], json_data['employed']]

            # append incoming data to file
            with open(self.json_filename, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(saved_data)

            print(f"Saved data: {data}")
        client_socket.close()

    def listen(self):
        try:
            self.socket.bind((self.host, self.port))  # bind the socket to the port and ip address
            self.socket.listen(5)  # wait for new connections
            listening = True
        except OSError:
            print(f"Unable to start the server. Port {self.port} is already in use.")
            listening = False
        except:
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
