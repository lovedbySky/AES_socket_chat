import socket
from threading import Thread
from AES import AESCipher
import json


class Client:
    def __new__(cls, *args, **kwargs):
        raise "Cannot create object by this class"

    file = open("config.json", "r")
    data = json.load(file)
    file.close()

    aes = AESCipher(data["config"]["key"])
    ip = data["config"]["ip"]
    port = data["config"]["port"]
    name = data["config"]["name"] + ": "
    client = None
    connect = False

    @classmethod
    def __connect_to_server(cls, ip, port):
        cls.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        cls.client.connect((ip, port))

    @classmethod
    def __accept_messages(cls):
        while True:
            if not cls.connect:
                break
            else:
                msg = cls.client.recv(1024).decode("utf-8")
                msg = cls.aes.decrypt(msg)
                if cls.name not in msg:
                    print(msg.strip())

    @classmethod
    def connect_to_chat(cls):
        cls.__connect_to_server(cls.ip, cls.port)
        cls.connect = True
        Thread(target=cls.__accept_messages, daemon=True).start()
        while True:
            msg = input()
            msg = cls.name + msg
            msg += ' ' * (1024 - len(msg))
            if "/exit" in msg or "/quit" in msg:
                cls.client.send(bytes(msg, "utf-8"))
                cls.connect = False
                print("Disconnect")
                cls.client.close()
                exit(0)
            msg = cls.aes.encrypt(msg)
            cls.client.send(bytes(msg, "utf-8"))

