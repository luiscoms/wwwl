#!/bin/bash

BIN_DOCKER=$(which docker)

if [ $? != 0 ]; then
    echo "Unable to find docker"
    exit 1
fi

export DOCKER_REPO='luiscoms'
export DOCKER_PROJ='flask'
export DOCKER_TAG='alpine-py3'
export DOCKER_FULLTAG=${DOCKER_REPO}/${DOCKER_PROJ}:${DOCKER_TAG}
# container name
export DOCKER_NAME=${DOCKER_TAG}

