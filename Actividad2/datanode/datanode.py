import socket, struct, sys
class datanode:
    def __init__(self, id, ip = 'localhost',puerto_server = 4002, puerto = 4001):
        self.ip = ip
        self.puerto = puerto
        self.multicast_group_ip = "224.1.1.1"
        self.id = id

        self.server_socket = socket.socket()
        self.server_socket.bind((ip, puerto_server))
        self.server_socket.listen(5)

        self.multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.multicast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.multicast_socket.bind((self.multicast_group_ip, puerto)) #by ip
        mreq = struct.pack("4sl", socket.inet_aton(self.multicast_group_ip), socket.INADDR_ANY)
        self.multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def save_message(self, message):
        print(message)
    def listen_headnode(self):
        while True:
            conexion, addr= self.server_socket.accept()
            print (addr)
            headnode_input=conexion.recv(1024).decode('utf-8')
            print (headnode_input)
            if headnode_input == "hi!":
                output="conection established"
            else:
                self.save_message(headnode_input)
                output = "done"
            conexion.sendall(output.encode('utf-8'))
            conexion.close()
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