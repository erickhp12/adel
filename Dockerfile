##########################################################
# Dockerfile para correr la aplicacion sitae (ventas TAE Ventamovil)
# Basada en la imagen oficial (python:2.7.12)
############################################################

# Se establece la imagen base
FROM python:2.7
ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/www/site

# Se establece el creador 
MAINTAINER Roberto Urita - @robertuj - roberto.urita@ventamovil.com.mx

# Create folder to work
RUN mkdir -p $WEBAPP_DIR && cd $WEBAPP_DIR
WORKDIR $WEBAPP_DIR

# Install Python dependencies
RUN apt-get update -y && apt-get install libmemcached-dev -y

ADD requirements.txt $WEBAPP_DIR/
RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["./docker-entrypoint.sh"]