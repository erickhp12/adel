#!/bin/bash

echo "Entrando al proceso de docker-entrypoint"

echo "Crea archivos de logs para gunicorn y access.log"
mkdir /logs
touch /logs/gunicorn.log
touch /logs/access.log
tail -n 0 -f /logs/*.log &

echo "Entra al directorio admintae"
cd /www/adel

echo "Ejecutando migraciones de base de datos"
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable cache_records
python manage.py collectstatic --noinput


# Start app with gunicorn
echo "Iniciando app con Gunicorn"
exec gunicorn -c ./gunicorn_conf.py ADEL.wsgi:application \
    --name adel \
    --log-level=info \
    --log-file=/logs/gunicorn.log \
    --access-logfile=/logs/access.log \
    "$@"
