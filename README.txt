Sebastian Jara 201573523-9
Gabriel Astorga 2015735??-?

Actividad 1:

-Se levanta el servidor con los comandos:
  docker-compose build
  docker-compose up

-Se levanta el cliente con los comandos:
  python client.py
  
-Se manda un mensaje


Actividad 2

-Para cada container correspondiente, en la base de ellos ver los logs en los txt 
con este comando:
  - docker ps -a (para ver las imagenes)
  - crear un snapshot del container
    docker commit <id> mysnapshot
  - para ver y navegar dentro del contenedor:
    docker run -t -i mysnapshot /bin/bash
    
*los containers al ser ejecutados imprimen lo que van recibiendo en la comunicación de mensajes
** el cliente manda por defectos mensajes (pre setados) esto debido a la confusión de la pregunta en moodle, pero se puede descomentar el que pida mensajes.
