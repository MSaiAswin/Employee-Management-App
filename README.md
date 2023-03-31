# Task 2

## Steps
 - First pull a mysql image from dockerhub. command: "docker pull mysql:5.7"
 - Then run the following command to create our database container with the proper configuration: "docker run --name db -d --expose 3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=app -e MYSQL_USER=user -e MYSQL_PASSWORD=passsword --restart always --hostname db mysql:5.7"
 - Now to get the IP of the mysql container, we use the following command: ' docker inspect db | grep "IPAddress" '
 - Now in ./src/config, change the database.yml as per the database
 - In the host field of the database.yml, insert the IP Address of the database container
![Screenshot from 2023-04-01 04-08-28](https://user-images.githubusercontent.com/78261857/229244860-bc389701-4284-411d-baf9-9ebf9612cee6.png)
 - Now build the new rails image using the following command while in the src directory: "docker built -t empapp ."
 - Next we run the image in a container using the following command: "docker run --name empcontainer -p 8080:3000 empapp"
 - Open localhost:8080 on a browser and you will see the following output
 ![Screenshot from 2023-04-01 03-42-24](https://user-images.githubusercontent.com/78261857/229244400-85196cbd-7270-4f94-b281-a0207bbf2c97.png)
 - to resolve this error, click on the "Run pending migrations" button
![Screenshot from 2023-04-01 03-42-36](https://user-images.githubusercontent.com/78261857/229244514-db86307f-8ac3-493c-bb64-d9fa3c02c4fe.png)
 - This is what you will get as the output.
