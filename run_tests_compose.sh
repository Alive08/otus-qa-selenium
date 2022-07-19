#!/bin/bash

usage()
{
    cat << USAGE >&2
Usage:
    ${0##*/} <path[s] to tests to be executed>
USAGE
    exit 1
}

if [ -z $@ ]; then
    usage
fi

docker network create --driver bridge test_net || true

export TESTS=$@

docker-compose up --abort-on-container-exit

docker-compose down

docker network rm test_net
