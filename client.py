import json
import socket


def main():
    running = True
    host = '127.0.0.1'  # server ip address
    port = 8888  # port of the server
    i = 0

    s = socket.socket()
    s.connect((host, port))  # bind the socket to the port and ip address

    print("Successfully connected to the server")
    while running:  # loop for as many times as the user wants
        i += 1

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
            'First Name': first_name,
            'Last Name': surname,
            'Age': age,
            'Employed': employed
            }

        employee_json = json.dumps(employee_dict)
        s.send(employee_json.encode('utf-8'))
        print("Employee information sent")

        go = input("Would you like to input anymore employee information, Yes or No? ")
        if go in ["N", "No", "NO", "no", 'n']:
            running = False

    s.close()  # close connection to the server


if __name__ == '__main__':
    main()
