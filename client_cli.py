from socket_client import Client
from os import system
import json

with open("config.json", "r") as file:
    data = json.load(file)


def print_intro():
    print(f"""
         111   1   1    1    11111
        11     11111   1 1     1
        11  1  1   1  11111    1
         111   1   1  1   1    1\n
    name: {data["config"]["name"]}
    ip: {data["config"]["ip"]}
    port: {data["config"]["port"]}\n
    type 'help' for get manual
       """)


def write_in_conf(param, value):
    data["config"][param] = value
    with open("config.json", "w") as file:
        json.dump(data, file)


def handle_commands(command):
    match command:
        case "set_name":
            name = input("Enter your name: ")
            write_in_conf("name", name)
            system('clear')
            print_intro()
        case "set_ip":
            ip = input("Enter server ip: ")
            write_in_conf("ip", ip)
            system('clear')
            print_intro()
        case "set_port":
            port = input("Enter server port: ")
            write_in_conf("port", port)
            system('clear')
            print_intro()
        case "set_key":
            key = input("Enter your key: ")
            write_in_conf("key", key)
            system('clear')
            print_intro()
        case "clear":
            system('clear')
        case "exit":
            exit(0)
        case "help":
            with open("help", 'r') as file:
                documentation = file.readlines()
                print(*documentation)
        case "connect":
            if Client.name:
                Client.connect_to_chat()
            else:
                print("You didn't set your name")
        case _:
            print("command not found")


if __name__ == "__main__":
    print_intro()
    try:
        while True:
            command = input("> ").strip()
            handle_commands(command)
    except KeyboardInterrupt:
        print("Quiting")
        exit(0)
