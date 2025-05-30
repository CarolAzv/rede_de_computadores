import re

class IPAddress:
    def __init__(self, address: str):
        if re.match(r'^[01]{32}$', address):
            self.bits = address
        elif re.match(r'^(\d{1,3}\.){3}\d{1,3}$', address):
            parts = list(map(int, address.split('.')))
            if any(p < 0 or p > 255 for p in parts):
                raise ValueError("Invalid IPv4 address range")
            self.bits = ''.join(f'{p:08b}' for p in parts)
        else:
            raise ValueError("Invalid IP format")

    def toBits(self) -> str:
        return self.bits

    def toIPv4(self) -> str:
        return '.'.join(str(int(self.bits[i:i+8], 2)) for i in range(0, 32, 8))

    def isMask(self) -> bool:
        return re.fullmatch(r'1*0*', self.bits) is not None

    def maskBits(self) -> int:
        if not self.isMask():
            raise ValueError("Not a valid subnet mask")
        return self.bits.count('1')

class IPToolIF:
    @staticmethod
    def isValid(ip: IPAddress) -> bool:
        try:
            _ = ip.toBits()
            return True
        except Exception:
            return False

    @staticmethod
    def areSameNet(ip1: IPAddress, ip2: IPAddress, mask: IPAddress) -> bool:
        net1 = IPToolIF.network(ip1, mask).toBits()
        net2 = IPToolIF.network(ip2, mask).toBits()
        return net1 == net2

    @staticmethod
    def broadcast(ip: IPAddress, mask: IPAddress) -> IPAddress:
        ip_bits = ip.toBits()
        mask_bits = mask.toBits()
        broadcast_bits = ''.join(
            ip_bits[i] if mask_bits[i] == '1' else '1'
            for i in range(32)
        )
        return IPAddress(broadcast_bits)

    @staticmethod
    def network(ip: IPAddress, mask: IPAddress) -> IPAddress:
        ip_bits = ip.toBits()
        mask_bits = mask.toBits()
        network_bits = ''.join(
            '1' if ip_bits[i] == '1' and mask_bits[i] == '1' else '0'
            for i in range(32)
        )
        return IPAddress(network_bits)
    
ip1 = IPAddress("192.168.1.10")
ip2 = IPAddress("192.168.1.20")
mask = IPAddress("255.255.255.0")

print("IP1:", ip1.toIPv4())
print("IP2:", ip2.toIPv4())
print("Same network?", IPToolIF.areSameNet(ip1, ip2, mask))
print("Broadcast:", IPToolIF.broadcast(ip1, mask).toIPv4())
print("Network:", IPToolIF.network(ip1, mask).toIPv4())
print("Mask bits:", mask.maskBits())