import socket
file=open("respuestas.txt","a")
mi_socket=socket.socket()
mi_socket.connect(('192.168.99.100',4000))
output="hola desde el cliente"
mi_socket.sendall(output.encode('utf-8'))
respuesta=mi_socket.recv(1024)
file.write(respuesta.decode("utf-8")+"\n")
print(respuesta.decode("utf-8"))
mi_socket.close()
file.close()