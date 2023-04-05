# Task 7

## Steps
 - First "docker compose down" to stop all the containers.
 - Then in the /web/nginx/default.conf file add the following
 - Above the server component, add "limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;". This defines our rate limiter.
 - Then above the proxy_pass statement,  add "limit_req zone=mylimit". This statement is so that the proxy uses the above defined rate limiter.
 - Next "docker compose up -d" to re-run all the containers.
 - Now we can see that the Employee Management App Home Window renders onto the screen as usual.
