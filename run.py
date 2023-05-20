from client import Client
from server import Server


def main():
    valid = False
    while not valid:
        choice = input("Would you like to run start a Client or Server? Enter C or S? ")
        if choice in ['C', 'c']:
            choice = "client"
            valid = True
        elif choice in ['S', 's']:
            choice = "server"
            valid = True
        else:
            print("Invalid input! The answer can be 'C' or 'S'")

    if choice == "server":
        server = Server()
        server.start()
    elif choice == "client":
        client = Client()
        client.start()


if __name__ == '__main__':
    main()
    