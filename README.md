# Task 6

## Steps
 - First create the docker-compose.yml and add all the necessary details to run the containers.
 - To avoid IP Address Issues, add hostname properties to all the containers, and add the depends-on property to containers that depend on each other.
 - For the employee-management containers, you can also add environment variables to store the db username, password and root password.
 - Then run "docker compose up -d" to run all the containers at once.
 - Now the app should work as usual, and the employee management screen is loaded.
