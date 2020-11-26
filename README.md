# DockerCompose × (Airflow + MySQl + Streamlit)
El proyecto que consiste en realizar un ETL en Airflow, que almacenará los datos en una base de datos MySQL que posteriormente será leída por Python para realizar un dashboard interactivo en Streamlit sobre los casos de Coronavirus.

Streamlit             |  Airflow  | MySQL
:-------------------------:|:-------------------------:|:-------------------------:|
![Streamlit](https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e181828ba9f9e92b6ebc6e7_RGB_Logomark_Color_Light_Bg.png) |   ![Airflow](https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png) |  ![MySQL](https://www.gibranjacobo.com/img/language/mysql.png)
## Descripción

El proyecto consiste en un ETL que toma tres archivos en formato CSV, los inserta en la base de datos de MySQL, y utilizando las tablas generadas, se hace un Dashboard en Streamlit que permite la correcta visualización e interpretación de la data.
Todo es realizado en un docker-compose para facilitar la comunicación entre los distintos servicios.

## Herramientas


### Instalación | Herramientas


### Uso | Herramientas


# Instrucciones para correr el código

Primero, descarga este código. Recuerda que el proyecto fue hecho en Docker Toolbox, así que ten en mente esto al tratar temas de compatibilidad.

## Docker

Hacer cd a la carpeta frontend
> cd frontend

Luego crear la imagen 
> docker build -f Dockerfile -t app:latest .

Después volver a la carpeta original
> cd ..

Y allí hacer el docker-compose
> docker-compose up

## Airflow

Tras levantar los servicios espera unos instantes y aparecerá el dashboard principal.
![](imagenes_procedimiento/dashboard.PNG)

Luego, deberás de crear las conexiones respectivas, para ello ve a la pestaña correspondiente en *Administración* y haz clic en crear una conexión.

![](imagenes_procedimiento/Crear_conexion.PNG)

Haz las dos conexiones respectivas usando los siguientes datos: 
### Monitor File
Sirve para verificar cuando un archivo se pone en la carpeta de destino.

![](imagenes_procedimiento/Monitor_File.PNG)

### SQL Connection
Sirve para conectar Airflow con MySQL.

![](imagenes_procedimiento/Crear_mysql.PNG)



Con esto ya podrás dar inicio a las tareas *DAG* para que hagan su trabajo.

![](imagenes_procedimiento/Tareas.PNG)


Al terminar su trabajo mostrarán un cículo verde oscuro.

![](imagenes_procedimiento/terminado.PNG)


## Streamlit
![](imagenes_procedimiento/streamlit.PNG)

En el Dashboard se pueden apreciar las imágenes de mapas a los que se les puede aplicar filtros.
![](imagenes_procedimiento/mapa.PNG)


El proceso puede tardar, para ello muestra un icóno así en la parte superior
![](imagenes_procedimiento/cargando.PNG)


Luego de interactuar con filtros podemos ver que el mapa se actualizará.
![](imagenes_procedimiento/filtros.PNG)


También habrá una tendencia para comparar los países seleccionados.
![](imagenes_procedimiento/tendencia.PNG)


Por último hay un mapa que muestra la relación de recuperados contra fallecidos usando esferas.
![](imagenes_procedimiento/muertes.PNG)



## ¿Qué sucede si hay un error con mis DAGS?
Si no se ejecutan ve y revisa las conexiones probablmente aparezca un error así.
![](imagenes_procedimiento/Error.PNG)

Para solucionarlo ve a conexiones, bórrala y vuelvela a crear.
![](imagenes_procedimiento/eliminar.PNG)
