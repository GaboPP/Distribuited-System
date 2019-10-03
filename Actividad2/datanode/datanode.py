import socket, struct, sys, os, threading
class datanode:
    def __init__(self, id, ip = '',puerto_server = 4002, puerto = 4001):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.puerto = puerto
        self.multicast_group_ip = '224.1.1.1'
        self.id = id


        filename = "./datanode/"+"datanode"+ str(self.id) + "/" +"data.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as file:
            file.write("\n")
            file.close()

        self.server_socket = socket.socket()
        self.server_socket.bind((ip, puerto_server))
        self.server_socket.listen(5)

        self.multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.multicast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.multicast_socket.bind(('', puerto)) #by ip
        mreq = struct.pack("4sl", socket.inet_aton(self.multicast_group_ip), socket.INADDR_ANY)
        self.multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def save_message(self, message):
        # print(message)
        file = open("./datanode/"+"datanode"+ str(self.id) + "/" +"data.txt", "a")
        file.write(message + "\n")
        file.close()
    def listen_headnode(self):
        while True:
            conexion, addr= self.server_socket.accept()
            # print (addr)
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

if __name__ == "__main__":
    id_datanode = sys.argv[1]
    DN = datanode(id_datanode)
    
    thread_server = threading.Thread(target=DN.listen_headnode)
    thread_heartbeat = threading.Thread(target=DN.listen)
    thread_server.start()
    thread_heartbeat.start()