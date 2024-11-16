#!/bin/bash

export JOB_NAME="onemt-v25"
export IMAGE="onemt/onemtv25"
export TAG="latest"
export PYTHON_ENV="development"
export API_PORT=8084
export WORKERS=2
export TIMEOUT=300
export LOG_FOLDER=log/onemt-v25

echo ${IMAGE}:${TAG}

# Create log folder if not exists
if [ ! -d ${LOG_FOLDER} ]; then
     mkdir ${LOG_FOLDER}
fi

# Add your authentication command for the docker image registry here

# force pull and update the image, use this in remote host only
#docker pull ${IMAGE}:${TAG}

# stop running container with same job name, if any
if [ "$(docker ps -a | grep $JOB_NAME)" ]; then
  docker stop ${JOB_NAME} && docker rm ${JOB_NAME}
fi

# start docker container
docker run \
  --rm \
  --gpus all \
  -p ${API_PORT}:8084 \
  -e "WORKERS=${WORKERS}" \
  -e "TIMEOUT=${TIMEOUT}" \
  -e "PYTHON_ENV=${PYTHON_ENV}" \
  -v "logs:/onemtv25/" \
  -t ${IMAGE}:${TAG}
