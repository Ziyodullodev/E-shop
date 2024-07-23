#!/bin/sh

echo 'Waiting for postgres...'

while ! nc -z $DB_HOSTNAME $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input
# birinchi ishga tushurganda pastdagi commentdagi kodni yoqib ishga tushurish kerak

# echo 'rebuild elastic search data'
# while ! nc -z $ELASTIC_HOSTNAME $ELASTIC_PORT; do
#     sleep 0.1
# done
# yes | python manage.py search_index --rebuild
exec "$@"