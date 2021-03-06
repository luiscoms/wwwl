#!/bin/bash

CUR_DIR=$(dirname "$(readlink -f "$0")")
source ${CUR_DIR}/docker-config.sh

PJ_ROOT=$(dirname ${CUR_DIR})

docker run --rm -it -p 80:80 -v ${PJ_ROOT}:/app ${DOCKER_FULLTAG} sh
