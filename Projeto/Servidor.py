import socket
import psutil
import shutil

try:
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 5005))
    servidor.listen()

    while True:
        conn, addr = servidor.accept()
        print(f"\nConexão de {addr}")

        data = conn.recv(1024).decode()
        print("Dados recebidos:", data)
except KeyboardInterrupt:
    print("Fechando...")
    if conn:
        conn.close()
    servidor.close()