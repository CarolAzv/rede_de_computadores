import socket
import platform
import psutil
import shutil

class View:
    def obter_dados_do_computador():
        total, usado, livre = shutil.disk_usage("C:\\") #memoria do disco | "C:\\" no Windows, "/home" no Linux

        ram = psutil.virtual_memory() #pegar ram

        interfaces = psutil.net_if_stats() #pegar desativadas
        desativadas = [nome for nome, stats in interfaces.items() if not stats.isup]

        conexoes = psutil.net_connections() #pegar as postars tcp e udp
        portas_tcp = set()
        portas_udp = set()

        for cone in conexoes:
            if cone.status == psutil.CONN_LISTEN:
                porta = cone.laddr.port
                if cone.type == socket.SOCK_STREAM:  # TCP
                    portas_tcp.add(porta)
                elif cone.type == socket.SOCK_DGRAM:  # UDP
                    portas_udp.add(porta)

        cpus_logicas = psutil.cpu_count(logical=True) # pegar cpu logica
        cpus_fisicas = psutil.cpu_count(logical=False) # pegar cpu fisica

        return {
            "nome": socket.gethostname(),
            "ip": socket.gethostbyname(socket.gethostname()),
            "RAM": ram,
            "disco": livre,
            "desativadas ": desativadas,
            "portas tcp": portas_tcp,
            "portas udp": portas_udp,
            "processadores logicos": cpus_logicas,
            "processadores fisicos": cpus_fisicas,
        }