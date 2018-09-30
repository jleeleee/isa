#!/bin/bash -e

pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null

APP=partex

case $1 in
    "django")
        docker run -it --name web -p 8000:8000 --link mysql:db -v $PWD/app:/app tp33/django \
            mod_wsgi-express start-server --reload-on-changes --working-directory /app/$APP /app/$APP/$APP/wsgi.py
        ;;
    "django-cli")
        docker exec -it --name web /bin/bash
        ;;
    "mysql")
        docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='$3cureUS' -v db:/var/lib/mysql mysql:5.7.23
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
