# Task 5

## Steps
 - First create to directories ./data/db and ./web/nginx
 - Then remove and delete the nginx and mysql containers
 - Then run the command "docker run --name db -d --expose 3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=app -e MYSQL_USER=user -e MYSQL_PASSWORD=passsword --restart always --hostname db -v ./data/db:/var/lib/mysql  mysql:5.7" to create the mysql container and associate it with the the created directory to persist the db data
 - Then run the command "docker run --name nginx-cont -d -p 8080:80 -v ./web/nginx:/etc/nginx/conf.d nginx-r-proxy" to create the nginx container and associate it with the the created directory to persist the config files.
 - Then run the containers and we will see that the Employee Management page is up and runninng.
