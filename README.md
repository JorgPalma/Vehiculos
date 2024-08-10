# Justificación del proyecto

He decidido utilizar Django como framework principal para el desarrollo de este proyecto debido a mi experiencia previa con él. Django es un framework robusto y probado que ofrece una estructura clara y eficiente para el desarrollo de aplicaciones web. Mi familiaridad con Django me permite aprovechar al máximo sus características, lo que garantiza un desarrollo más rápido y una implementación eficiente.

### Vistas del frontend
Las vistas del frontend en este proyecto están diseñadas para interactuar directamente con la base de datos, consumiendo los datos en tiempo real. Este enfoque permite una mayor coherencia y consistencia en la presentación de la información al usuario, además de simplificar el flujo de datos entre el frontend y el backend.


### Uso de SQLite
He optado por utilizar SQLite como motor de base de datos para este proyecto. SQLite es la base de datos por defecto en Django y es ideal para proyectos pequeños o en etapas iniciales de desarrollo. Su simplicidad y facilidad de uso permiten un desarrollo rápido sin la necesidad de configurar una base de datos externa. Sin embargo, si el proyecto requiere mayor escalabilidad o robustez en el futuro, se puede migrar fácilmente a un sistema de base de datos más avanzado.

### Django REST Framework
La API del proyecto ha sido desarrollada utilizando Django REST Framework. Es una herramienta poderosa que facilita la creación de APIs RESTful de manera eficiente, permitiendo el uso directo de los formularios de los modelos de Django para la creación de endpoints. Esta integración simplifica considerablemente el desarrollo y mantenimiento de la API, asegurando que los datos se gestionen de forma segura y coherente.

### Diseño del Frontend
El frontend de la aplicación se ha diseñado con un enfoque minimalista e intuitivo, priorizando la usabilidad y la experiencia del usuario. Se ha prestado especial atención a la simplicidad del diseño para garantizar que los usuarios puedan interactuar con la aplicación de manera eficiente y sin complicaciones, lo que mejora la accesibilidad y la satisfacción del usuario.

# Instrucciones de instalación de manera local

* Clona el repositorio en tu equipo utilizando la siguiente ruta:
```
git clone https://github.com/JorgPalma/Vehiculos.git
```
* Navega hacia el directorio donde se clonó el repositorio

* Crea un entorno virtual:
```
python -m venv venv
```

* Activa el entorno virtual:
```
venv\Scripts\activate
```

* Instala las dependencias especificadas en el archivo requirements.txt:
```
pip install -r requirements.txt
```

* Ejecuta las migraciones necesarias para terminar de ajustar la base de datos:
```
python manage.py migrate
```

* Crea el Superuser que te permitirá ingresar como administrador en el sistema, una vez ejecutado el código, sigue las instrucciones que aparecen en la consola:
```
python manage.py createsuperuser
```

* Pobla la base de datos con los vehículos facilitados utilizando el siguiente comando en la consola:
```
python manage.py insertar
```

* Ejecuta el servidor y visualiza la aplicación web
```
python manage.py runserver
```

# API

##### Se puede acceder a la api agregando **/api/vehicles** a la URL donde se esté alojando el servidor web.

En esta vista se puede ver un listado de todos los vehículos registrados en el sistema, permitiendo alternan entre el formato API o Json. Además en la parte inferior se puede realizar un POST de un nuevo vehículo, rellenando los campos del formulario


---



##### Se puede filtrar tanto por VIN o por patente agregando **api/vehicles/?vin=...** o **api/vehicles/?patente=...**

Por ejemplo, si queremos buscar un vehículo con el VIN "JM7BN3273J1146657", nos 


quedaría una URL así: 
```
api/vehicles/?vin=JM7BN3273J1146657
```
En caso de no existir coincidencias no se desplegará nada.


---



##### Se puede acceder a la documentación de la API agragando **/docs** a la URL donde se esté alojando el servidor.




