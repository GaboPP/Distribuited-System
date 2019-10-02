import socket, time, threading, random

class headnode:
    def __init__(self, ip = '172.16.238.2',puerto_server = 4000, puerto_datanode = 4002, 
                ip_multicast = "224.1.1.1", puerto_multicast = 4001, MULTICAST_TTL = 1):
        self.ip_headnode_list = ['172.16.238.3','172.16.238.4','172.16.238.5']
        # self.ip_headnode_list = ['localhost','localhost','localhost']
        self.ip = ip
        self.puerto_multicast = puerto_multicast
        self.puerto_server = puerto_server
        self.ip_multicast = ip_multicast
        self.puerto_datanode = puerto_datanode
        self.MULTICAST_TTL = MULTICAST_TTL  #reintentos para reenvio
        
        file = open("registro_server.txt", "w")
        file.write("  Address  |datanode|\n")
        file.close()

        file = open("hearbeat_server.txt", "w")
        file.write("Heartbeat|datanode1|datanode2|datanode3|\n")
        file.close()
        self.count_log = 0

        #socket server headnode
        self.server_socket = socket.socket()
        self.server_socket.bind((ip, puerto_server))
        self.server_socket.listen(5)
        
        #socket server datanodes:
        self.list_sockets_datanodes = list()
        for i in range(3):
            self.list_sockets_datanodes.append(socket.socket().connect((self.ip_headnode_list[i], self.puerto_datanode)))
        
        #socket multicast
        self.multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        self.multicast_socket.settimeout(0.2) # tiempo de espera por una respuesta

        print("headnode initialized")

    def check_alive(self):
        while 1:
            self.multicast_socket.sendto("estas?".encode('utf-8'), (self.ip_multicast, self.puerto_multicast))

            datanode_count = 0
            mensajes = [0,0,0,0]
            while True:
                try:
                    respuesta= self.multicast_socket.recv(1024)
                except socket.timeout:
                    print('timed out, no more responses')
                    break
                else:
                    mensaje_resp = respuesta.decode("utf-8")
                    if(mensaje_resp != ''):
                        mensajes[int(mensaje_resp)] = 1 # si responde el datanode i se guarda su ack en el campo [i]
                        datanode_count += 1
                        
                        print(mensaje_resp)
                if(datanode_count == 3): #break cuando lleguen todas las respuestas(3)
                    break
            
            self.log_hearbeat(mensajes)
            time.sleep(5)
    
    def log_hearbeat(self, respuestas):
        self.count_log += 1

        file = open("hearbeat_server.txt", "a")
        file.write("____" + str(self.count_log) + "____|    "+ str(respuestas[1]) + "    |    " + str(respuestas[2]) + "    |    " + str(respuestas[3]) + "    |\n")
        file.close()
    def send_message_datanode(self, mensaje, socket_target_datanode):
        self.socket_target_datanode.sendall(mensaje.encode('utf-8'))
        try:
            respuesta=self.socket_client.recv(1024)
        except socket.timeout:
            print('timed out, server unavailable')
            return False # guardar en otro nodo
        else:
            mensaje_resp = respuesta.decode("utf-8")
            if(mensaje_resp != ''):                      
                return mensaje_resp

        print(respuesta.decode("utf-8"))
    def log_registro(self, addr, datanode_number):
        file = open("registro_server.txt", "a")
        file.write(addr + " |    "+str(datanode_number) + "    |\n")
        file.close()
    def listen_client(self):
        while True:
            conexion, addr= self.server_socket.accept()
            print (addr)
            client_input=conexion.recv(1024).decode('utf-8')
            print (client_input)
            if client_input == "hi!":
                output="conection established"
            else:
                datanode_number = random.randint(1,3)
                if(self.send_message_datanode(self, client_input, self.list_sockets_datanodes[datanode_number-1])):
                    output = str(datanode_number)
                elif(self.send_message_datanode(self, client_input, self.list_sockets_datanodes[0])):
                    output = str(1)
                elif(self.send_message_datanode(self, client_input, self.list_sockets_datanodes[1])):
                    output = str(2)
                elif(self.send_message_datanode(self, client_input, self.list_sockets_datanodes[2])):
                    output = str(3)
                else:
                    output = 'error service unavailable'                    
                self.log_registro(addr, output)
            conexion.sendall(output.encode('utf-8'))
            conexion.close()
    def shotdown(self):
        self.server_socket.close()
        self.multicast_socket.close()


if __name__ == "__main__":
    #id_datanode = sys.argv[1]
    H = headnode()
    
    thread_server = threading.Thread(target=H.listen_client)
    thread_heartbeat = threading.Thread(target=H.check_alive)
    thread_server.start()
    thread_heartbeat.start()