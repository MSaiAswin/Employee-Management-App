# Task 2

## Steps
 - First edit /src/cofig/environments/development.rb and add the line config.hosts << "loadbalance"
 - Here "loadbalance" indicates the hostname that we use as the name for our upstream element in the /web/default.conf file
 - Next stop, remove the app container and the app image. Now rebuild the app image and create 3 app containers.
 - Next note down the IP Addresses of all the three containers.
 - Now add the upstream element with the name "loadbalance" and define the three servers and their IPs with the ports as following.
 ![image](https://user-images.githubusercontent.com/78261857/229306515-3e62e3f7-9984-4d24-b88b-41ce6c70ec3a.png)
 - Now rebuild the nginx images and containers and run.
 - When we open localhost:8080 we should get the same output as before.
 ![Screenshot from 2023-04-01 03-42-36](https://user-images.githubusercontent.com/78261857/229302046-1066bd10-bc94-4c4c-8623-c86876772e7d.png)
