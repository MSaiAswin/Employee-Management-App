# Task 3

## Steps
 - First make a new directory /web in the main directory
 - Create a file called default.conf and populate it with /etc/nginx/conf.d/default.conf file of a default nginx container.
 - To make it a reverse proxy, remove the default text under "location /" in the "server" component and add "proxy_pass http://[IP]:3000" where <IP> is the IP of the application container. We can get the container IP by running the command ' docker inspect [app-container-name] | grep "IPAddress" '.
 - Create a Docker file in /web to create a nginx reverse-proxy image.
 - Now stop the application container and remove it and recreate it without publishing the ports and run it.
 - Now create the nginx reverse-proxy image using docker build command in /web.
 - Now create a reverse proxy container using the docker run command and publish port 80 of this container to 8080 of the host machine.
 - Next open up localhost:8080 in a web browser and you will see the following output
 ![Screenshot from 2023-04-01 03-42-36](https://user-images.githubusercontent.com/78261857/229302046-1066bd10-bc94-4c4c-8623-c86876772e7d.png)
