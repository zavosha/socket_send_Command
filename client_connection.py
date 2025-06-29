import socket

def send_message():
    host='127.0.0.1'
    port = 9999
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((host, port))
    try:
        while True:
            cmd = input("what is your command\n")
            if cmd.lower() == 'exit':
                break
            socket_client.send(cmd.encode())
            response = socket_client.recv(1024)
            print(response.decode())
    finally:
        socket_client.close()
    
send_message()