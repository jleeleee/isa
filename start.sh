#!/bin/bash -e

pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null

APP=partex

case $1 in
    "django")
        docker-compose up
        ;;
    "django-cli")
        docker exec -it web /bin/bash
        ;;
    "mysql")
        docker run --name mysql -d --env-file db/vars.env -v db:/var/lib/mysql mysql:5.7.23
        ;;
    "mysql-cli")
        docker run -it --name mysql-cmdline --link mysql:db mysql:5.7.23 bash
        ;;
    "pull")
        docker pull tp33/django
        ;;
    *)
        echo "Help"
        ;;
esac

popd > /dev/null
