import socket
import platform
import psutil
import shutil
from View import View

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("255.255.255.255", 5005))

dados = View.obter_dados_do_computador()
mensagem = str(dados)
cliente.send(mensagem.encode())

cliente.close()