#!/bin/bash -e

pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null

CMDS="Available commands:\n
django\n
django-cli\n
mysql\n
mysql-cli\n
pull\n
stopdb
"

case $1 in
    "django")
        docker-compose up
        ;;
    "django-cli")
        docker exec -it partex_web_1 /bin/bash
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
    "stopdb")
        docker stop mysql | sed 's/^/Stopped: /g'
        docker rm mysql | sed 's/^/Removed: /g'
        ;;
    *)
        echo -e $CMDS
        ;;
esac

popd > /dev/null
