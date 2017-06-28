#!/bin/bash

echo "Entrando al proceso de docker-entrypoint"

echo "Crea archivos de logs para gunicorn y access.log"
mkdir /home/logs
touch /home/logs/gunicorn.log
touch /home/logs/access.log
tail -n 0 -f /home/logs/*.log &

echo "Entra al directorio admintae"
cd /www/site

echo "Ejecutando migraciones de base de datos"
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable cache_records
python manage.py collectstatic --noinput


# Start app with gunicorn
echo "Iniciando app con Gunicorn"
exec gunicorn -c ./gunicorn_conf.py adel.wsgi:application \
    --name admintae \
    --log-level=info \
    --log-file=/home/logs/gunicorn.log \
    --access-logfile=/home/logs/access.log \
    "$@"