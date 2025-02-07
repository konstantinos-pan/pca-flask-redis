## Flask-app that uses redis server with docker compose

This is a Flask-app that performs Principal Components Analysis and outputs the variance explained by each principal component in a json file using redis server.
The project includes the Dockerfile of the app, the python script and docker-compose.yaml in order to orchestrate the app container and redis server container.

## How to run the app

1) Clone the repository
   '''bash
   $git clone https://github.com/konstantinos-pan/pca-flask-redis.git

2) Go the directory of the repository folder
   '''bash
   $cd ~/pca-flask-redis

3) Run the app using docker-compose
   '''bash
   $sudo docker-compose up

4) Get the output
   open a web browser and go to: http://localhost:5000/pca

5) Don't forget to execute docker-compose down
   '''bash
   $sudo docker-compose down


## Troubleshoot

If during step 3 you get an error "for redis Cannot start server redis", you may have redis-server already running.
In this case, run the command "$ /etc/init.d/redis-server stop"
