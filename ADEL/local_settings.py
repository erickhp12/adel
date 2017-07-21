# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adel',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

# API_COADSY = 'http://127.0.0.1:8080/'

# Web Service Admin
# Prueba
# WS_URL = "http://10.10.10.82:9090/service.asmx?wsdl"
# Produccion
# WS_URL = "http://10.10.10.82:9091/service.asmx?wsdl"

# # El Web Service de TAE se configura en el admin(Ventas)
# # http://10.10.10.82:9092/service.asmx?wsdl

# SITE_DOMAIN = "http://nuevo.eventamovil.mx/"
