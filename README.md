# django-base
Este proyecto apunta a facilitarnos el trabajo de inicio de un proyecto, teniendo configuraciones básicas como la instalación de Django, Django REST, Notificaciones, JWT y todas las librerías que consideremos necesarias.
Es importante entender que va a requerir un mantenimiento y lo vamos a hacer entre todes.

## Cómo empiezo?
**Prerequisito: Tener un virtual env para el proyecto, ya activado.**

Clonas el proyecto:
``` 
$ git clone git@gitlab.com:gaia-software/django-base.git 
``` 
Cambias al directorio del proyecto:
```
cd django-base
```
Renombras la carpeta del proyecto:
```
mv baseproject/ mi_nuevo_proyecto
```

### Modificamos los siguientes archivos para que apunten a nuestro nuevo nombre:
- manage.py 
- mi_nuevo_proyecto/asgi.py 
- mi_nuevo_proyecto/wsgi.py 

La linea que dice
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baseproject.settings')
```

Debería decir
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_nuevo_proyecto.settings')
```

### Modificamos el archivo mi_nuevo_proyecto/settings.py
La linea que dice:
```
ROOT_URLCONF = 'baseproject.urls'
```

Debería decir:
```
ROOT_URLCONF = 'mi_nuevo_proyecto.urls'
```
La linea que dice:
```
WSGI_APPLICATION = 'baseproject.wsgi.application'
```

Debería decir:
```
WSGI_APPLICATION = 'mi_nuevo_proyecto.wsgi.application'
```
### Llegaste al final de la configuración, a partir de ahora, es un proyecto regular de Django.



### Incluye
- Instalación de Django
- Instalación de DRF

### Qué se puede agregar?
- Modelo User personalizado
- Admin panel de Maistrenko
- Configuracion de la Base de Datos
- Login con JWT
- Notificaciones (fcm-django)


