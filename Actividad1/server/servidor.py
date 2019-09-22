import socket

mi_socket= socket.socket()
mi_socket.bind(('0.0.0.0',80))
mi_socket.listen(5)
while True:
    conexion, addr= mi_socket.accept()
    file = open("log.txt", "a")
    print ("nueva conexion establecida")
    print (addr)
    peticion=conexion.recv(1024)
    print (peticion.decode('utf-8'))
    file.write(peticion.decode('utf-8')+","+str(addr[0])+"\n")
    output="se ha recibido correctamente"
    conexion.sendall(output.encode('utf-8'))
    conexion.close()
    file.close()