### Configuración

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
$ pip3 install -r requirements.txt
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




