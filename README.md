## Datos cocinados para hacer mapas de 

* Autor: Ramiro Aznar
* Ultima actualizacion: 2020-03-15
* Fuente de datos: Datadista

### Esquemas

Los datasets tienen el siguiente esquema:
* the_geom (geom)
* latitude (int) [solo en los datasets de centroides]
* longitude (int) [solo en los datasets de centroides]
* value (int)
* population (int)
* value_density (int)
* ccaa (string)
* source (string)
* source_url (string)
* date (timestamp)

La diferencia fundamental entre estos datasets y los de Datadista es como se han estructurado los datos en funcion del tiempo. Mientras que en los datos de Datadista cada columna es una fecha y cada columna es una comunidad, en estos datasets cada fila es el dato de una comunidad en una fecha. 

### Metodologia

Las queries utilizadas para hacer esta agregacion se pueden ver en [este (collaboratory) notebook](/prepare_covid19_data_spain.ipynb).

### Datasets

* Casos:
    * [Poligonos](https://ramiroaznar.carto.com/dataset/casos_df)
    * [Centroides](https://ramiroaznar.carto.com/dataset/casos_centroids)
* Fallecidos:
    * [Poligonos](https://ramiroaznar.carto.com/dataset/fallecidos_df)
    * [Centroides](https://ramiroaznar.carto.com/dataset/fallecidos_centroids)
