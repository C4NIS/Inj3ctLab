
docker run --name mysql_inj3ctlab -e MYSQL_ROOT_PASSWORD=your_root_password -e MYSQL_DATABASE=inj3ctlab_db -e MYSQL_USER=inj3ctlab_user -e MYSQL_PASSWORD=your_password -p 3306:3306 -v /my/own/datadir:/var/lib/mysql -d mysql:latest
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql_inj3ctlab
docker exec -it mysql_inj3ctlab mysql -u inj3ctlab_user -p inj3ctlab_db
