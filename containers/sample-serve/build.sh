#!/usr/bin/env bash

set -e

image_name=sample-serve

env GOOS=linux GOARCH=amd64 go build -tags netgo sample-serve.go

account=$(aws sts get-caller-identity | jq -r ".Account")
docker_host="$account.dkr.ecr.eu-west-1.amazonaws.com"
docker build -t $docker_host/$image_name .
docker tag $docker_host/$image_name:latest $docker_host/$image_name:latest

$(aws ecr get-login --no-include-email --region eu-central-1)

docker push $docker_host/$image_name:latest

rm sample-serve
