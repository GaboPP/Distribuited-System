import socket, time

class headnode:
    def __init__(self, ip = 'localhost',puerto_server = 4000, ip_multicast = "224.1.1.1", puerto_multicast = 4001, MULTICAST_TTL = 1):
        self.ip = ip
        self.puerto_multicast = puerto_multicast
        self.puerto_server = puerto_server
        self.ip_multicast = ip_multicast
        self.MULTICAST_TTL = MULTICAST_TTL  #reintentos para reenvio
        
        file = open("hearbeat_server.txt", "w")
        file.write("Heartbeat|datanode1|datanode2|datanode3|\n")
        file.close()
        self.count_log = 0

        self.server_socket = socket.socket()
        self.server_socket.bind((ip, puerto_server))
        self.server_socket.listen(5)
        
        self.multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        self.multicast_socket.settimeout(0.2) # tiempo de espera por una respuesta

        print("headnode initialized")

    def check_alive(self):
        
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

    def log_hearbeat(self, respuestas):
        self.count_log += 1

        file = open("hearbeat_server.txt", "a")
        file.write("____" + str(self.count_log) + "____|    "+ str(respuestas[1]) + "    |    " + str(respuestas[2]) + "    |    " + str(respuestas[3]) + "    |\n")
        file.close()

    def log_registro(self):
        print(1)
    def shotdown(self):
        self.server_socket.close()
        self.multicast_socket.close()

H = headnode()
H.check_alive()
H.check_alive()
