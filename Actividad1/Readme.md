
1: docker-compose up --build -d 
2: encontrar el id del contenedor con: docker ps
3: crear una imagen (snapshot) desde el  container filesystem con: docker commit <\id> mysnapshot
4: explorar el filesystem como bash con: docker run -t -i mysnapshot /bin/bash
5: ls y vim para ver los logs
6: docker rmi mysnapshot (--force) para borrar el snapshot

