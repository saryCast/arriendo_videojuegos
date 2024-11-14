# Caso “Club Videojuegos (Fullstack Python)”


Creado por Sara Castillo Arenas



Paso para ejecutar el proyecto:
-------------------------------


1) Crear un ambiente virtual, activarla e instalar las dependencias usando:

    >    pip install -r requirements.txt


2) Crear una base de datos en Postgres llamada: 
    > club_videojuegos   ** Cambiar por el nombre que usted colocó

3) Cambiarse a la carpeta club_videojuegos


4) Ejecutar las migraciones:

    > python3 manage.py makemigrations
    >
    > python3 manage.py migrate



5) Ejecutar el proyecto:

    > python manage.py runserver



Datos de usuarios:
------------------

a) Super Usuario:


> usuario:       admin
>
> contraseña:    admin 


b) Usuarios:  (estos son ejemplos. Coloque los creados por usted)

Usuario Administrador

> usuario:        pedro@mail.com
>
> contraseña:     pedro12345

___________________________________

Otros Usuarios

> usuario:        maria@mail.com
>
> contraseña:     maria12345


> usuario:        claudia@mail.com
>
> contraseña:     claudia12345


_____________________________________________________________

Para este requerimiento:
El administrador debe tener acceso a la pantalla Reporte de Arriendos, donde puede ver el listado de los juegos arrendados.

RESOLUCION:

Genere una pestaña extra en la barra de navegación : Reporte de Arriendos
En donde el usuario administrador puede ver todos los arriendos.
En la misma ventana, agregue el requerimiento final, en donde se ven las multas por fecha ascendente.

en la ruta /reporte_arriendos


Rutas de acceso:
Ruta:/
Ruta Raiz con la tabla que entrega todos los video Juegos disponibles, que se puede filtrar por tipo de Plataforma

Ruta: /videojuego/<id>/arrendar/
Ruta para arrendar el juego donde viene la descripción del mismo

Ruta: /accounts/login/
Ruta para que el usuario ingrese al sistema

Ruta: /accounts/register/
Ruta para registrar nuevo usuario

Ruta: /accounts/logout/
Ruta para salir 

Ruta mis_arriendos/
Ruta que muestra todos los arriendos para un usuario

Ruta videojuego/<id>/arrendar/
Ruta para arrendar un juego
 
Ruta videojuegos/<int:id>/retornar/
Para pantalla de devolver un videojuego, seleccionando fecha de retorno

Ruta arriendos/<int:id>/devolver
Ruta que devuelve el videoJuego


Ruta reporte_arriendos/
Ruta del usuario administrador que puede ver todos los arriendos de todos los usuarios

