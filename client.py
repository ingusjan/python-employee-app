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
    while running:
        i += 1
        first_name = input("Enter the employee's first name: ")
        surname = input("Enter the employee's surname: ")
        age = int(input("Enter the employee's age: "))
        employed = input("Is the employee currently employed, Yes or No? ")
        if employed == "Yes" or employed == "Y" or employed == "YES" or employed == "yes":
            employed = True
        else:
            employed = False

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
        if go in ["N", "No", "NO", "no"]:
            running = False

    s.close()  # close connection to the server


if __name__ == '__main__':
    main()
