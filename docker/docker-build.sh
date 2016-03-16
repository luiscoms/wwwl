#!/bin/bash

CUR_DIR=$(dirname "$(readlink -f "$0")")
source ${CUR_DIR}/docker-config.sh

PJ_ROOT=$(dirname ${CUR_DIR})

docker build --force-rm -t ${DOCKER_FULLTAG} -f ${CUR_DIR}/Dockerfile ${PJ_ROOT}
