import socket
import psutil
import shutil
from View import View

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 5005)) #'127.0.0.1', 5005 # '10.25.1.59', 5005

dados = View.obter_dados_do_computador()
mensagem = str(dados)
cliente.send(mensagem.encode())

cliente.close()