#!/bin/bash

# Defina suas variáveis
DOCKER_USERNAME="seu_usuario_dockerhub"
DOCKER_PASSWORD="sua_senha_dockerhub"
DOCKER_HUB_URI="seu_dockerhub_uri"
IMAGE_NAME="netuno-receiver-microservice"
TAG="latest"

# Build da imagem
docker build -t $IMAGE_NAME:$TAG -f $DOCKER_HUB_URI/IMAGE_NAME:$TAG .

# Login no Docker Hub
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin

# Push da imagem
docker push $IMAGE_NAME:$TAG

# Logout do Docker Hub
docker logout