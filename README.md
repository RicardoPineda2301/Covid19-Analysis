# Proyecto Dashboards de Covid-19 con Streamlit, Airflow, MySQL y Docker

Streamlit             |  Airflow  | MySQL
:-------------------------:|:-------------------------:|:-------------------------:|
![Streamlit](https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e181828ba9f9e92b6ebc6e7_RGB_Logomark_Color_Light_Bg.png) |   ![Airflow](https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png) |  ![MySQL](https://www.gibranjacobo.com/img/language/mysql.png)
## Descripción

El proyecto consiste en un ETL que toma tres archivos en formato CSV, los inserta en la base de datos de MySQL, y utilizando las tablas generadas, se hace un Dashboard en Streamlit que permite la correcta visualización e interpretación de la data.
Todo es realizado en un docker-compose para facilitar la comunicación entre los distintos servicios.

## Herramientas


### Instalación | Herramientas


### Uso | Herramientas


## Instrucciones

Hacer cd a la carpeta frontend

```cd frontend```

Luego crear la imagen 
```docker build -f Dockerfile -t app:latest . ```

Después volver a la carpeta original
``` cd .. ```

Y allí hacer el docker-compose
``` docker-compose up ```
