import socket
import platform
import psutil
import shutil

try:
    serveridor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveridor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    serveridor.bind(("0.0.0.0", 5005))
    serveridor.listen()

    while True:
        conn, addr = serveridor.accept()
        print(f"\nConexão de {addr}")

        data = serveridor.recvfrom(1024).decode()
        print("Dados recebidos:", data)
except KeyboardInterrupt:
    print("Fechando...")
    conn.close()