#!/bin/bash -e

pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null

CMDS="Available commands:\n
django\n
django-cli\n
makemigrations\n
mysql\n
mysql-cli\n
pull\n
stopdb
stopweb
"

RESETDB="drop database cs4501;
create database cs4501 character set utf8;
grant all on cs4501.* to 'www'@'%';
"

case $1 in
    "django")
        docker-compose up
        ;;
    "django-cli")
        docker-compose exec web /bin/bash
        ;;
    "makemigrations")
        docker-compose exec web /bin/bash -c \
            "python manage.py makemigrations"
        ;;
    "makedb")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'\$3cureUS' -h localhost -e\"create user 'www'@'%' identified by '\$3cureUS';\""
        ;;
    "resetdb")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'\$3cureUS' -h localhost -e\"$RESETDB\""
        ;;
    "mysql")
        docker run --name mysql -d --env-file app/partex/db/vars.env -v db:/var/lib/mysql mysql:5.7.23
        ;;
    "mysql-cli")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'\$3cureUS' -h localhost"
        ;;
    "pull")
        docker pull tp33/django
        ;;
    "stopweb")
        docker-compose rm web
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
