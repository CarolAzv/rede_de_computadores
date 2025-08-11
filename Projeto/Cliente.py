import socket
import platform

def obter_dados_do_computador():
    return {
        "nome": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "sistema": platform.system(),
        "versao": platform.version()
    }

# Cria socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor (altere 'localhost' para o IP do servidor)
client.connect(("255.255.255.255", 5005))

# Coleta dados do computador
dados = obter_dados_do_computador()

# Envia os dados como string
mensagem = str(dados)
client.send(mensagem.encode())

# Encerra conexão
client.close()