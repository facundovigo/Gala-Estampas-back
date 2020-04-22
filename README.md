# django-base
Este proyecto apunta a facilitarnos el trabajo de inicio de un proyecto, teniendo configuraciones básicas como la instalación de Django, Django REST, Notificaciones, JWT y todas las librerías que consideremos necesarias.
Es importante entender que va a requerir un mantenimiento y lo vamos a hacer entre todes.

## Cómo empiezo?

Clonas el proyecto:
``` 
$ git clone git@gitlab.com:gaia-software/django-base.git 
```

## Instalación
Hay dos formas de instalar esto:
- Con el script instalador.py
- Manualmente

#### Usando el script
Ejecuta el siguiente comando:
```
mv django-base/instalador.py instalador.py && python3 instalador.py  

```
Pedirá un Nombre de Proyecto y opcionalmente la url del repositorio de git que estamos queriendo crear.

Listo!

#### Manualmente

Cambias al directorio del proyecto:
```
cd baseproject/
```
Renombras la carpeta del proyecto:
```
mv baseproject/ mi_nuevo_proyecto
```

##### Modificamos los siguientes archivos para que apunten a nuestro nuevo nombre:
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

##### Modificamos el archivo mi_nuevo_proyecto/settings.py
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

Ahora, vamos a configurar git para que no se suban los cambios a ese repositorio
```
$ git remote set-url origin [url-de-mi-nuevo-proyecto]
```

## Con esto finaliza la configuración, a partir de ahora, es un proyecto regular de Django.

¿Pero que significa esto?
Quiere decir que tenes que crear un virtual-env con python3.8 para tu proyecto:

Primero tendrias que tener instalada dicha version de Python:
https://tecadmin.net/install-python-3-8-ubuntu/

Una vez que tenemos esto creamos el ambiente virtual:
```
$ python3.8 -m venv nombreDelProyecto-env
```
Luego lo activamos:
```
$ source bin/activate
```
Instalamos los requerimientos:
```
$ pip3 install -r requeriments.txt
```
Aplicamos las migraciones en la carpeta del proyecto:
```
$ python3.8 manage.py migrate
```
Y levantamos el server:
```
$ python3.8 manage.py  runserver
```

### Admin panel

Ingresando en localhost:8000/admin podemos entrar al panel de administrador pero antes necesitamos crear un superusuario:
```
$ python3.8 manage.py  createsuperuser
```


### Configurar el usuario de django
La funcionalidad que armamos permite decidir si los usuarios se van a autenticar con email o con nombre de usuario. Si se autentican con email, el nombre de usuario no será requerido. Esto se configura desde el archivo settings, con la key AUTH_WITH_EMAIL.


### Incluye
- Instalación de Django
- Instalación de DRF
- Modelo User personalizado
- Configuracion de CI (gitlab)
- Configuración de coverage (gitlab)
- Recuperacion de contraseña
- Modelo de ejemplo con campo imagen
- Media folder (para subir imagenes)

### Qué se puede agregar?
- Admin panel de Maistrenko
- Configuracion de la Base de Datos
- Login con JWT
- Notificaciones (fcm-django)


