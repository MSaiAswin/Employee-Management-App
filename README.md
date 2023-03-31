# Task 1

## Steps
 - Add a Dockerfile in the src directory
 - In the src run the command : "docker build -t empapp ." to build an image of the application
 - To the image write the command : "docker run -p 8080:3000 --name empcontainer empapp"
 - Open localhost:8080 on a browser and you will see the following output
 ![task_1](https://user-images.githubusercontent.com/78261857/229221543-d3281c56-322d-47af-8d7d-4c70b80819f6.png)
 - to resolve this issue, we need to setup the database
