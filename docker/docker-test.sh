#!/bin/bash

CUR_DIR=$(dirname "$(readlink -f "$0")")
source ${CUR_DIR}/docker-config.sh

PJ_ROOT=$(dirname ${CUR_DIR})

echo ${DOCKER_FULLTAG}
docker run --rm -it -v ${PJ_ROOT}:/app ${DOCKER_FULLTAG} py.test -v
