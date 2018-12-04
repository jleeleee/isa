#!/bin/bash -e

pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null

CMDS="Available commands:\n
up\n
models-cli\n
exp-cli\n
web-cli\n
makemigrations\n
mysql\n
mysql-cli\n
pull\n
test\n
stopdb\n
stopserver\n
dropdbuser\n
dropdb\n
makedb\n
"

ROOTPASS="\$3cureUS"

DROPDB="drop database cs4501;"
CREATEDB="create database cs4501 character set utf8;
grant all on cs4501.* to 'www'@'%';
grant all on test_cs4501.* to 'www'@'%';"
CREATEUSER="create user 'www'@'%' identified by '\$3cureUS';"
DROPUSER="drop user 'www'@'%';"

case $1 in
    "up")
        docker-compose build
        docker-compose up
        ;;
    "models-cli")
        docker-compose exec models /bin/bash
        ;;
    "exp-cli")
        docker-compose exec exp /bin/bash
        ;;
    "web-cli")
        docker-compose exec web /bin/bash
        ;;
    "makemigrations")
        docker-compose exec models /bin/bash -c \
            "python manage.py makemigrations"
        ;;
	"initindex")
		docker-compose exec models /bin/bash -c \
			"python manage.py initindex"
		;;
    "dropdbuser")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'$ROOTPASS' -h localhost -e\"$DROPUSER\""
        ;;
    "makedbuser")
        echo "!!! WARNING This does not work"
        echo "Do it yourself with mysql-cli"
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'$ROOTPASS' -h localhost -e\"$CREATEUSER\""
        ;;
    "dropdb")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'$ROOTPASS' -h localhost -e\"$DROPDB\""
        ;;
    "makedb")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'$ROOTPASS' -h localhost -e\"$CREATEDB\""
        ;;
    "mysql")
        docker run --name mysql -d -e MYSQL_ROOT_PASSWORD=$ROOTPASS -v $PWD/db:/var/lib/mysql mysql:5.7.23
        ;;
    "mysql-cli")
        docker exec -it mysql /bin/bash -c \
            "mysql -uroot -p'$ROOTPASS' -h localhost"
        ;;
    "pull")
        docker pull tp33/django
        ;;
    "test")
        docker exec -it models /bin/bash -c \
            "python manage.py test partex.apps"
        ;;
    "stopserver")
        docker-compose rm models
        docker-compose rm exp
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
