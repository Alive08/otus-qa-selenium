#!/bin/bash

name=opencart
ip=$(grep ${name} /etc/hosts| cut -f1)
artifacts=artifacts

rm -rf ${artifacts}
mkdir -p ${artifacts}

docker run \
	--add-host ${name}:${ip} \
	--name tests tests \
	--executor=${name} \
	--base-url=http://${name}:8081 \
	--myip=${name} \
	$@

docker cp tests:/tests/testrun.log ${artifacts}
docker cp tests:/tests/screenshots ${artifacts}
docker cp tests:/tests/allure-results ${artifacts}
docker rm tests
