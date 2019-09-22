import socket, struct, sys
class datanode:
    def __init__(self, id, ip = '', puerto = 4001):
        self.ip = ip
        self.puerto = puerto
        self.multicast_group_ip = "224.1.1.1"
        self.id = id

        self.multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.multicast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.multicast_socket.bind((ip, puerto))
        mreq = struct.pack("4sl", socket.inet_aton(self.multicast_group_ip), socket.INADDR_ANY)
        self.multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        # self.multicast_socket.listen(5)
    def listen(self):
        print("nodo conectado")
        while(True):            
            mensaje, address = self.multicast_socket.recvfrom(1024)
            print(mensaje.decode('utf-8'))
            self.multicast_socket.sendto(str(self.id).encode('utf-8'), address)
            # conexion, addr= self.multicast_socket.accept()
            # peticion=conexion.recv(1024)
            # print (peticion.decode('utf-8'))
            # conexion.sendall("si".encode('utf-8'))
            # conexion.close()

if __name__ == "__main__":
    id_datanode = sys.argv[1]
    DN = datanode(id_datanode)
    DN.listen()