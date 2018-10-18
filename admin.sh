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

DROPDB="drop database cs4501;"
CREATEDB="create database cs4501 character set utf8;
grant all on cs4501.* to 'www'@'%';"
CREATEUSER="create user 'www'@'%' identified by '\$3cureUS';"

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
    "makedbuser")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'\$3cureUS' -h localhost -e\"$CREATEUSER\""
        ;;
    "dropdb")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'\$3cureUS' -h localhost -e\"$DROPDB\""
        ;;
    "makedb")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'\$3cureUS' -h localhost -e\"$CREATEDB\""
        ;;
    "mysql")
        docker run --name mysql -d --env-file app-models/partex/db/vars.env -v ~/cs4501/db:/var/lib/mysql mysql:5.7.23
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
