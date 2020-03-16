## Datos cocinados para hacer mapas y series temporales
### covid-19

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
* value_density (float)
* ccaa (string)
* source (string)
* source_url (string)
* date (timestamp)

La diferencia fundamental entre estos datasets y los de Datadista es como se han estructurado los datos en funcion del tiempo. Mientras que en los datos de Datadista cada columna es una fecha y cada columna es una comunidad, en estos datasets cada fila es el dato de una comunidad en una fecha. 

### Metodologia

Los datasets se actualizan diariamente corriendo el script `run.py`. 

Si quieres correrlo en tu ordenador sigue los siguientes pasos:
1. Clona este repositorio.
2. Deberas [crearte una cuenta en CARTO](www.carto.com/signup).
3. Crea un archivo en esta carpeta llamado `creds.json` con la siguiente estructura:

```json
{
    "username": "TU_USERNAME",
    "api_key": "TU_API_KEY"
}
```

4. Crea un virtual environment:

```bash
$ virtualenv -p python 3 env
```

5. Activalo:

```bash
$ source env/bin/activate
```

6. Instala las dependencias:

```bash
$ pip install -r requirements.txt
```

7. Por ultimo, corre el script:

```bash
$ python run.py
```

### Datasets

* Casos:
    * [Raw](https://ramiroaznar.carto.com/dataset/casos)
    * [Poligonos](https://ramiroaznar.carto.com/dataset/unnested_casos)
    * [Centroides](https://ramiroaznar.carto.com/dataset/centroids_casos)
* Fallecidos:
    * [Raw](https://ramiroaznar.carto.com/dataset/fallecidos)
    * [Poligonos](https://ramiroaznar.carto.com/dataset/unnested_fallecidos)
    * [Centroides](https://ramiroaznar.carto.com/dataset/centroids_fallecidos)
