import sys
import json
import socket
import ipaddress


class Client:
    def __init__(self):
        self.host = '127.0.0.1'  # server ip address
        self.port = 8888  # port of the server
        self.socket = socket.socket()

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))  # bind the socket to the port and ip address
            connected = True
        except ConnectionRefusedError:
            print(f"Unable to connect to host: {self.host} on port: {self.port}")
            connected = False
        return connected

    def start(self):
        while True:
            # work out how to keep looping
            connected = self.connect()
            if connected:
                print(f"Successfully connected to server {self.host}, on port {self.port}")
                break  # exit while loop once connected
            else:
                valid = False
                while not valid:
                    retry = input("Would you like to try connecting again, Yes or No? ")
                    if retry in ['Y', 'YES', 'Yes', 'yes', 'y']:
                        valid_ip = False
                        while not valid_ip:
                            host = input("Enter the IP address of the host you would like to connect to: ")
                            try:
                                ipaddress.ip_address(self.host)  # will throw an exception if the ip address is not valid
                                valid_ip = True
                                self.host = host
                            except ValueError:
                                print("Invalid input! IPv4 address only")

                        valid_port = False
                        while not valid_port:
                            try:
                                port = int(input("Enter the port of the host you would like to connect to: "))
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

        print("Successfully connected to the server")

        running = True
        while running:  # loop for as many times as the user wants

            valid = False
            while not valid:  # keep letting the user input first names until they enter a valid one
                first_name = input("Enter the employee's first name: ")
                if first_name.isalpha():
                    first_name.capitalize()
                    valid = True
                else:
                    print("Invalid input! First name should only contain letters")
            valid = False

            while not valid:
                surname = input("Enter the employee's surname: ")
                if surname.isalpha():
                    surname.capitalize()
                    valid = True
                else:
                    print("Invalid input! Surname should only contain letters")

            while True:
                try:
                    age = int(input("Enter the employee's age: "))
                except ValueError:
                    print("Age must be a valid integer")
                else:  # if the input is a valid integer, break the loop
                    break

            valid = False
            while not valid:
                employed = input("Is the employee currently employed, Yes or No? ")
                if employed in ['Y', 'YES', 'Yes', 'yes', 'y']:
                    employed = True
                    valid = True
                elif employed in ['N', 'NO', 'no', 'No', 'n']:
                    employed = False
                    valid = True
                else:
                    print("Invalid input! The answer can be 'Yes' or 'No'")

            employee_dict = {
                'first_name': first_name,
                'last_name': surname,
                'age': age,
                'Employed': employed
            }

            employee_json = json.dumps(employee_dict)
            self.socket.send(employee_json.encode('utf-8'))  # encode the data before it is sent
            print("Employee information sent")

            go = input("Would you like to input anymore employee information, Yes or No? ")
            if go in ["N", "No", "NO", "no", 'n']:
                running = False

        self.socket.close()  # close connection to the server


def main():
    client = Client()
    client.start()


if __name__ == '__main__':
    main()
