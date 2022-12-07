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

    key = data["config"]["key"] or "12345"
    aes = AESCipher(key)
    ip = data["config"]["ip"] or "0.0.0.0"
    port = data["config"]["port"] or 4444
    name = data["config"]["name"] + ": " or "user" + ": "
    client = None
    connect = False

    @classmethod
    def init(cls):
        file = open("config.json", "r")
        data = json.load(file)
        file.close()

        cls.key = data["config"]["key"]
        cls.aes = AESCipher(cls.key)
        cls.ip = data["config"]["ip"]
        cls.port = data["config"]["port"]
        cls.name = data["config"]["name"] + ": "

    @classmethod
    def __connect_to_server(cls, ip, port):
        cls.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        cls.client.connect((ip, port))

    @classmethod
    def __accept_messages(cls, data=[]):
        while True:
            if not cls.connect:
                break
            else:
                msg = cls.client.recv(1024).decode("utf-8")
                if "/exit" not in msg and "/quit" not in msg:
                    try:
                        msg = cls.aes.decrypt(msg)
                    except UnicodeDecodeError:
                        print("Non valid key, cannot read the message")
                        continue
                if cls.name not in msg and not msg.isspace():
                    data.append(msg.strip())
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

