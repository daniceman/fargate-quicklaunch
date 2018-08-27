#!/usr/bin/env bash

set -e

REGION="eu-central-1"

IMAGE_NAME=sample-serve

env GOOS=linux GOARCH=amd64 go build -tags netgo sample-serve.go

ACCOUNT=$(aws sts get-caller-identity | jq -r ".Account")
DOCKER_HOST="${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com"
docker build -t ${DOCKER_HOST}/${IMAGE_NAME} .
docker tag ${DOCKER_HOST}/${IMAGE_NAME}:latest ${DOCKER_HOST}/${IMAGE_NAME}:latest

$(aws ecr get-login --no-include-email --region ${REGION})

docker push ${DOCKER_HOST}/${IMAGE_NAME}:latest

rm sample-serve
