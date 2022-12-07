import socket
import threading
import sys


def send_every(msg):
    for cl in client_list:
        cl.send(bytes(msg, "utf-8"))


def handle_client(client):
    while True:
        if client not in client_list:
            break
        msg = client.recv(1024).decode("utf-8")
        if "/quit" in msg or "/exit" in msg:
            client_list.remove(client)
            client.close()
        print(msg.strip())
        send_every(msg)


if __name__ == "__main__":
    params = sys.argv[1:]
    if "-ip" in params and "-port" in params:
        ip = params[params.index("-ip") + 1]
        port = int(params[params.index("-port") + 1])
    else:
        ip, port = None, None

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip or "0.0.0.0", port or 4444))
    server.listen(5)
    header_size = 10
    client_list = []

    print(ip, port)
    try:
        while True:
            client, address = server.accept()
            print(address[0], "is connected")
            client_list.append(client)
            threading.Thread(target=handle_client, args=(client,), daemon=True).start()
    except KeyboardInterrupt:
        print("\nShutdown the server")
        exit(0)

