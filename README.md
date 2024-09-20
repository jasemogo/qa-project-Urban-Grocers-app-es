# Proyecto Urban Grocers
## **Descripción:**
Urban Grocers es una aplicación en la que pueden hacer pedidos de productos alimenticios. 

Descrita como entrega de productos por catálogo y kits preparados. Donde el usuario/a pueden crear sus propios kits personalizados

### Este proyecto
- Conjunto de ejecucción de pruebas para comprobar la funcionalidad del parámetro "name" del cuerpo de la solicitud para crear un kit para un usuario o usuaria
- - Se envían solicitud para crea un usuario/a y guardar el authToken
- - Con su token de autorización se prueban las creaciones de kit iterando el parámetro "name"


- La documentación de la API se encuentra en con la dirección en terminación: 
- **/docs/**

### Recursos adicionales:
#### Pytest
Pytest es un framework que te ayuda a la ejecución y determinación de los resultados de pruebas de software con el lenguaje Python.

#### Requests
Requests es una librería de simple y fácil de usar que te permite envíar solicitudes HTTP/1.1 (GET, PUT, POST, DELETE). También te permite usar método JSON para las estructuras de las solicitudes enviadas.

- Necesitas tener instalados los paquetes "pytest" y "requests" para ejecutar las pruebas.
- Se ejecutan todas las pruebas con el comando pytest. (pytest create_kit_name_kit_test.py)

### **EJECUCIÓN**
- Para ejecutar las pruebas se recomienda user el siguiente comando:
- - pytest ./create_kit_name_kit_test.py
- Donde **"pytest"** es la palabra clave para llamar y usar el paquete Pytest.
- **"./"** es el directorio donde se encuentra la carpeta del proyecto "qa-project-Urban-Grocers-app-es"
- *create_kit_name_kit_test.py* es el archivo Python donde se encuentran las diferentes pruebas para la creacion del kit de usuario/a