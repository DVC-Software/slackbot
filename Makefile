DOCKER_IMAGE ?= dvc-software/slackbot
DOCKER_CONTAINER ?= slackbot
HIDE ?= @
PORT ?= 8000
HOSTPORT ?= 8000
NETWORK ?= bridge


build:
	$(HIDE)docker build -f Dockerfile -t $(DOCKER_IMAGE) $(PWD)

start:
	$(HIDE)docker-compose -f docker/docker-compose.yml up --build $(DOCKER_CONTAINER)

daemon:
	$(HIDE)docker-compose -f docker/docker-compose.yml up -d --build $(DOCKER_CONTAINER)

stop: 
	$(HIDE)docker stop $(DOCKER_CONTAINER)
	$(HIDE)docker container rm $(DOCKER_CONTAINER)

rm:
	$(HIDE)docker rm $(docker ps -a -q)

rm-all:
	$(HIDE)docker system prune
