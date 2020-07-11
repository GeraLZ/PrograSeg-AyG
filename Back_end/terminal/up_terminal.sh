#!/bin/bash

for var in $(ccrypt -d -c settings.env.cpt); do
    export "$var"
done

docker-compose up -d