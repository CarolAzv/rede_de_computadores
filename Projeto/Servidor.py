import socket

# Cria socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga ao IP e porta
server.bind(("0.0.0.0", 5005))
server.listen()

print("Servidor pronto para receber dados...")

while True:
    conn, addr = server.accept()
    print(f"\nConexão de {addr}")

    dados = conn.recv(2048).decode()
    print("Dados recebidos:", dados)

    conn.close()