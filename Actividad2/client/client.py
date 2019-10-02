
import socket, time, threading

class client:
    def __init__(self, ip = '172.16.238.2', puerto_server = 4000): #192.168.99.100
        self.ip = ip
        self.puerto_Server = puerto_server
        
        file = open("registro_cliente.txt", "w")
        file.write("#mensaje|datanode|\n")
        file.close()

        self.socket_client = socket.socket()
        self.socket_client.connect((self.ip, self.puerto_Server))

    def log(self):
        output="hi!"
        self.socket_client.sendall(output.encode('utf-8'))

        try:
            respuesta=self.socket_client.recv(1024)
        except socket.timeout:
            print('timed out, server unavailable')
        else:
            mensaje_resp = respuesta.decode("utf-8")
        print(respuesta.decode("utf-8"))
    def log_registro(self, datanode_number):
        file = open("registro_server.txt", "a")
        file.write("   "+ self.count + "    |    "+str(datanode_number) + "    |\n")
        file.close()
    
    def send_message(self,mensaje):
        self.socket_client.sendall(mensaje.encode('utf-8'))

        try:
            respuesta=self.socket_client.recv(1024)
        except socket.timeout:
            print('timed out, server unavailable')
        else:
            mensaje_resp = respuesta.decode("utf-8")
            if(mensaje_resp != ''):                      
                self.log_registro(mensaje_resp)

        print(respuesta.decode("utf-8"))

if __name__ == "__main__":
    C = client()
    C.log()
    client_input = ''
    client_input_list = ['omaewa', 'hola soy el cliente', 'lolito', 'juan luis guerra', 'este mensaje se autodestruira en 30 seg', 'exit()']
    count = 0
    while client_input != "exit()":
        # client_input = input("Ingrese un mensaje: ")
        client_input = client_input_list[count]
        if client_input!="exit()":
            C.send_message(client_input)
        count += 1
    C.socket_client.close()
