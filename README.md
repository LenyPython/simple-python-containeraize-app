### Conteneraized Python3 flask app

Just a training in creating dev environment with Docker.


## Build prod 

$ docker build -t python-api:prod .

run a container: 
$ docker run --name python-app-prod -d -p8080:8080 --mount type=bind,src=$(pwd)/src,target=/app/src python-api:prod
or run a docker-compose app


## Build dev environment

$ docker build -t python-api:dev -f Dockerfile.dev .

run a container

$ docker run --name python-app-dev -d -p8080:8080 --mount type=bind,src=$(pwd)/src,target=/app/src python-api:dev
or run a docker-compose-dev app
