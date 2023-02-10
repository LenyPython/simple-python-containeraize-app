### Conteneraized Python3 flask app

Just a training in creating dev environment with Docker.


## Build prod 

docker build -t fast-api:prod .

run a container

docker run --name Production-fast-api -d -p8080:8080 -v ${pwd}/src:/src fast-api:dev
## Build dev environment

docker build -t fast-api:dev -f Dockerfile.dev .

run a container

docker run --name dev-env -d -p8080:8080 --mount type=bind,src="$(pwd)"/src,target=/app/src fast-api:dev
