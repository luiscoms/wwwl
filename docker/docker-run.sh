#!/bin/bash

CUR_DIR=$(dirname "$(readlink -f "$0")")
source ${CUR_DIR}/docker-config.sh

PJ_ROOT=$(dirname ${CUR_DIR})

docker run -d --name ${DOCKER_NAME} -p 80:8080 -v ${PJ_ROOT}:/app ${DOCKER_FULLTAG}
