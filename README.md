# CAPTURA Y ALMACENAMIENTO DE DATOS USANDO NEO4J

## INTRODUCCION

El código almacenado en este repositorio constituye el entregable final para la materia "Captura y almacenamiento de la información" de la "Especialización en Inteligencia de Datos orientada a Big Data" dictada en la Facultad de Informática de la Universidad Nacional de La Plata.

https://www.info.unlp.edu.ar/especializacion-en-inteligencia-de-datos-orientada-a-big-data/

Alumnos: 

- Dra. Analisa Mariazzi (analisam@gmail.com)
- Dr. Gastón Giordano (gaston2031@gmail.com)
- Lic. Alejo Hernandez (homocuadratus@gmail.com)

## OBJETIVO

Estudiar las fases de captura y almacenamiento de la información implementando un prototipo de recomendador de películas basado en Python, Neo4j y Docker.

## DESCRIPCION DE LAS HERRAMIENTAS UTILIZADAS

### MOTIVACION

Antes de comenzar con la descripción de cada una de las herramientas empleadas para desarrollar el prototipo, resulta necesario escribir unas líneas que ayuden a comprender el porqué de la elección. En primer lugar, seleccionamos como lenguaje de scripting a `Python`, pues hoy por hoy es el lenguaje natural de las tareas de un Data Scientist, además de tener una sintaxis sencilla y un amplio soporte. En segundo lugar, teniendo en cuenta la estructuración natural de los datos con los que se pensaba trabajar (peliculas con sus respectivos ratings dados por usuarios que las hubieran visto) se decidió emplear `Neo4j`, una base de datos basada en grafos, que permite explotar al máximo las relaciones existentes entre los usuarios bajo análisis y entre ellos con las peliculas consumidas. Finalmente, para disponibilizar el prototipo, se decidió encapsular al mismo dentro de un container de `Docker`, puesto que esta es la manera standard en la actualidad para efectuar ese proceso.

### PYTHON

<img src="/images/python.png" alt="drawing" width="20%"/>

Nacido en 1991 de la mano de Guido Van Rossum, Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje multiparadigma, pues soporta la programación orientada a objetos (OOP), imperativa y, en menor medida, funcional. 

Python es un lenguaje interpretado, dinámico y multiplataforma que actualmente es administrado por la Python Software Foundation (PSF). El mismo posee una licencia de código abierto, denominada Python Software Foundation License.

Las motivaciones principales a la hora de utilizar este lenguaje para nuestro desarrollo fueron su simplicidad de uso, combinada con su amplia adopción en los entornos de trabajo de Data Science y el enorme soporte brindado por la comunidad.

Para más información sobre Python, visite https://www.python.org/about/


### NEO4J

<img src="/images/Neo4j-logo_color.png" alt="drawing" width="20%"/>

#### Introduccion

Neo4j es una base de datos abierta, NoSQL y con soporte de ACID que almacena la información en forma nativa utilizando una estructura basada en grafos. Su código fuente, escrito en Java y Scala, está disponible en forma gratuita en Github desde 2007. También se puede probar la misma bajando una aplicación de escritorio en su sitio web https://neo4j.com/try-neo4j/. 

Neo4j se define como una base de grafos nativa ya que implementa de forma eficiente las propiedades de los modelos de grafos a la hora de almacenar los datos. Esto quiere decir que los datos están almacenados siguiendo el mismo esquema que podemos plantear en un pizarron y la base de datos utiliza punteros para navegar y recorrer el grafo. A diferencia de los procesadores de grafos o las librerias en memoria, Neo4j tambien provee caracteristicas propias de las bases de datos convencionales, como ser el soporte transcaccional de tipo ACID, soporte para clusters y tolerancia a fallos, lo cual la convierte en candidata ideal para usar grafos en entornos productivos. 

Algunas de las prestaciones que vuelven popular a Neo4j entre desarrolladores, arquitectos y DBAs son: 

- Cypher, un lenguaje de consulta declarativo basado en SQL que permite explotar la estructura de grafo de Neo4j. 
- Tiempo de exploracion constante en bases con millones de nodos y relaciones, lo cual posibilita escalar la base en hardware moderado.
- Esquema flexible de modelo de grafos con propiedades, lo cual permite la rapida adaptacion de la base para satisfacer nuevas necesidades de negocio.
- Drivers para los lenguajes de programacion mas populares, incluyendo Java, JavaScript, .NET, Python, y muchos mas.

#### El modelo de grafos con propiedaes

El enfoque utilizado por Neo4j para manejar los componentes de la base de datos basada en grafos es el del **modelo de grafos con propiedades**, donde los datos están organizados como **nodos**, **relaciones** y **propiedades** (datos almacenados en los nodos o en las relaciones).

- **Nodos** 
Los nodos son las entidades del grafo. Estos pueden guardar un número indefinido de atributos como pares `{llave: valor}` llamados **propiedades**. Los nodos pueden ser identificados mediante etiquetas, las cuales representan los diferentes roles en un dominio dado. Las mismas, pueden utilizarse también para añadir metadata, como índices o información sobre vínculos.

- **Relaciones** 
Las relaciones proveen conexiones dirigidas, nombradas y semanticamente relevantes entre entidades nodales (Por ejemplo _Empleado_ TRABAJA_PARA _Compañía_). Una relación siempre tiene una dirección, un tipo, un nodo de incio y un nodo de fin. Al igual que los nodos, las relaciones también pueden tener propiedades, las cuales, en la mayoría de los casos, suelen ser cuantitativas: pesos, costos, distancias, ratings, intervalos temporales, fuerzas, etc. Puesto que las relaciones se guardan de forma eficiente, dos nodos pueden compartir cualquier número de relaciones sin sacrificar performance y las mismas se pueden recorrer en forma eficiente en cualquier dirección.

El siguiente esquema permite entender de forma más acabada el modelo de grafos con propiedades que acabamos de describir.

<img src="/images/property_graph_elements.jpg" alt="drawing" width="90%"/>

#### Lenguaje de consulta Cypher

Cypher es un lenguaje de consulta declarativo que permite consultar, actualizar y administrar la base de datos basada en grafos de manera simple y eficiente. 

El mismo toma prestada su estructura de SQL, en el sentido de que las consultas se construyen en base a cláusulas que pueden concatenarse entre si y pasar los resultados de una a otra. 

Algunos de las comandos de **consulta** más importantes son: 

- `MATCH`, que expresa el patrón de grafo a evaluar (equivalente a un `SELECT`).
- `WHERE` usualmente vinculada con las clásulas `MATCH`, `OPTIONAL MATCH` y `WITH`.
- `RETURN` que expresa el resultado a mostrar.

Por otro lado, aquellos comandos más relevantes relacionados con la **actualización** son

- `CREATE` (y `DELETE`), permite crear (eliminar) nodos y relaciones.
- `SET` (y `REMOVE`), permite asignar (quitar) valores a las propiedades o bien crear (remover) etiquetas en los nodos.
- `MERGE`, Matchea con los existentes o crea nuevos nodos y patrones. Se usa principalmente en combinación con vínculos únicos.

Para entender mejor el funcionamiento, analicemos un ejemplo sencillo. Primero creamos una pequeña base de datos, que consiste en 5 nodos de tipo `Person` y 2 relaciones de tipo `FRIEND`, respectivamente:

```
CREATE (john:Person {name: 'John'})
CREATE (joe:Person {name: 'Joe'})
CREATE (steve:Person {name: 'Steve'})
CREATE (sara:Person {name: 'Sara'})
CREATE (maria:Person {name: 'Maria'})
CREATE (john)-[:FRIEND]->(joe)-[:FRIEND]->(steve)
CREATE (john)-[:FRIEND]->(sara)-[:FRIEND]->(maria)
```
Esta base presenta la siguiente estructura:

<img src="/images/dummy_db_structure.svg" alt="drawing" width="20%"/>

Sobre la misma, podemos realizar una consulta que muestre los amigos de amigos (friends of friends or fof) del usuario `John` escribiendo

```
MATCH (john {name: 'John'})-[:FRIEND]->()-[:FRIEND]->(fof)
RETURN john.name, fof.name
```
El resultado es el siguiente

```
+----------------------+
| john.name | fof.name |
+----------------------+
| "John"    | "Maria"  |
| "John"    | "Steve"  |
+----------------------+
2 rows
```

Para ver cuestiones que hacen al filtrado, escribamos ahora una consulta que muestre aquellos usuarios que tengan algún otro usuario como amigo directo (`follower`) cuyo nombre (propiedad) empiece con la letra `S`:

```
MATCH (user)-[:FRIEND]->(follower)
WHERE user.name IN ['Joe', 'John', 'Sara', 'Maria', 'Steve'] AND follower.name =~ 'S.*'
RETURN user.name, follower.name
```
Ahora el resultado obtenido es,

```
+---------------------------+
| user.name | follower.name |
+---------------------------+
| "John"    | "Sara"        |
| "Joe"     | "Steve"       |
+---------------------------+
2 rows
```

Para conocer más sobre Cypher, visite https://neo4j.com/docs/cypher-manual/current/introduction/#cypher-intro

### DOCKER
<img src="/images/docker.png" alt="drawing" width="20%"/>

#### Introducción

Docker es una plataforma abierta para desarrollar, transportar y correr aplicaciones que nació de la mano de Solomon Hykes en 2013. El mismo permite separar las aplicaciones de la infrastructura, posibilitando una entrega de software rápida.

Docker provee la habilidad de empaquetar y correr una aplicación en un entorno "aislado" llamado container. El aislamiento y la seguridad permite que puedan correrse varios containers al mismo tiempo en un host dado. Los containers son livianos y contienen todo lo necesario para correr la aplicación, evitando así la necesidad de tener que confiar en los paquetes instalados en el host. Los containers se emplean principalmente para compartir desarrollos y garantizarse de que cada destinatario recibe el mismo entorno y que todo funciona de la misma manera. Este último punto fue el que motivó la elección del mismo como medio para distribuir nuestro trabajo.

#### Arquitectura

<img src="/images/docker_architecture.svg" alt="drawing" width="70%"/>

Docker utiliza una arquitectura de tipo cliente-servidor. El cliente de Docker client se comunica con el demonio para que este último contruya, corra y distribuya los contenedores. Tanto el cliente como el demonio pueden residir en el mismo sistema, como asi también podemos tener un cliente local y un demonio remoto. Los mismos utilizan una API REST sobre sockets de UNIX o una interfaz de red para comunicarse. 

Otro cliente de Docker es el llamado Docker Compose, el cual permite trabajar con aplicaciones que involucran más de un container.

- El demonio de Docker

El demonio de Docker `dockerd` escucha los pedidos de la API y administra los objetos de Docker, como imagenes, containers, redes y volumenes. Un dmeonio puede comunicarse con otros para adminitrar servicios de Docker.

- El cliente de Docker

El cliente de Docker `docker` es la vía principal que los distintos usuarios utilizan para interactuar con Docker. Cuando utilizamos comandos como `docker run`, el cliente envía los mismos vía API al demonio `dockerd`, el cual los ejecuta. Un cliente puede comunicarse con varios demonios a la vez.

- Registros de Docker

Un registro de Docker almacena imágenes. Docker Hub is un registro público que cualquiera puede usar. Docker está configurado por default para buscar imágenes en ese registro y descargarla si no las tiene.

Cuando se hace un `docker pull` o `docker run`, las imágenes son descargadas desde el registro configurado. Cuando se usa el comando `docker push`, la imágen es sincronizada con el registro configurado.

- Objetos de Docker

Al utilizar Docker, se crean y utilizan imágenes, containers, redes, volúmenes, plugins y otros objetos. A continuación se describen algunos de ellos:

**Images**

Una imagen es una plantilla de solo lectura con instrucciones para crear un container de Docker. Usualmente, una imágen está basada en otra, con alguna reforma adicional. Por ejemplo, en el trabajo se utilizó una imágen de Ubunto con Neo4j a la que se adicionaron Python y diversas librerías e instrucciones para que pudiera correr la aplicación correctamente.

Para construir una imágen, es necesario crear un `Dockerfile`, el cual, mediante una sintaxis sencilla, define los pasos a emplear. Cada instrucción en el `Dockerfile` crea una capa en la imágen. En caso de establecer cambiso en el mismo, sólo aquellas capas afectadas son reconstruidas cuando se vuelve a crear la imágen. Esto es lo que posibilita que las imágenes pueden ser tan livianas, pequeñas y rápidas comparadas con otras tecnologías de virtualización.

**Containers**

Un container es una instancia ejecutable de una imágen. Se puede crear, iniciar, detener, mover o borrar un container usando la API de Docker o la interfaz de línea de comandos (CLI). A su vez, un container puede conectarse a una o más redes, se le pueden asignar unidades de almacenamiento e incluso se puede crear una imágen basada en su estado en ese momento.

Por defecto, un container está relativamente bien aislado de otros containers y de su host. De hecho, se pueden controlar cuán aisladas están sus redes, sus unidades de almacenamiento u otros subsistemas de interés.

Un container está definido por su imágen, así como también por las opciones de configuración que se proveyeron cuando se creó o se inició. Cuando un container es removido, cualquier cambio de estado que haya sufrido se pierde a menos que se haya persistido en alguna unidad de almacenamiento permanente fuera del mismo.

## ETAPAS DEL PROCESO DE IMPLEMENTACION

### CAPTURA

El proceso de captura de la información se procesa dentro del Dockerfile, ejecutando los comandos 

```
wget -r --no-check-certificate https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
wget -r --no-check-certificate https://files.grouplens.org/datasets/movielens/ml-25m.zip 
```

Unan vez descargados, estos dataset zippeados se descomprimen y los archivos `movies.csv`, `genome-scores.csv` y `ratings.csv` que estan en su interior se mueven a la carpeta `/var/lib/neo4j/import` desde la cual seran tomados por el script de python que realizara las tareas de preprocesamiento.

### PREPROCESAMIENTO

Durante esta etapa, los archivos csv mencionados en el apartado anterior se convierten en dataframes de Python y se les realizan varias transformaciones con el objeto de establecer un criterio de similitud de peliculas. 

En líneas generales, el proceso es como sigue:

1. Se conforma un dataset en el que constan la relevancia de ciertos tags definidos para cada pelicula. Por ejemplo, si tuvieramos una pelicula con id1 y 3 tags T1, T2, T3 con relevancias R1, R2, R3, respectivamente, una fila de esa matriz seria (id1, R1, R2,R3)

2. Se conforma un dataset en el que constan los distintos generos que se le asignan a una dada pelicula. Por ejemplo, si tuvieramos una pelicula con id1 y 3 generos G1, G2, G3, una fila de esa matriz podría ser (id1, 0, 1, 1) en el caso de que sólo estuvieran presentes G2 y G3 para esa película.

3. Se conforma un dataset en el que consta el rating promedio otorgado en distintos periodos de tiempo a una dada pelicula. Por ejemplo, si tuvieramos una pelicula con id1 y 3 intervalos temporales t1, t2, t3, con ratings promedio r1, r2, r3 respectivamente, una fila de esa matriz sería (id1, r1, r2, r3).

4. Sobre la base de cada uno de estos datasets, se calcula la similitud entre peliculas en base a la relevancia de sus tags, sus generos y sus ratings promedio, respectivamente. La documentación sobre la función que calcula la similitud, `cosine similarity`, puede consultarse aqui https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html. Finalmente, las tres similitudes se combinan linealmente para producir un unico valor que es el que finalmente alimenta el recomendador.
 
5. Por último, usando toda esta información, se generan los nodos y las estructuras de relaciones a ser cargadas en `Neo4j` y se guardan como archivos csv en la carpeta `/var/lib/neo4j/import`. Dichos archivos son, para los nodos, `users.csv`, `movies_new.csv` y `genres.csv`, respectivamente, mientras que para las relaciones tenemos `users_movies.csv`, `users_genres.csv`, `movies_genres.csv` y `movies_similarity.csv`

### ALMACENAMIENTO

El almacenamiento se produce a partir del insert en Neo4j de los nodos y relaciones codificado en la query `load_data.cql` que se encuentra almacenada en la carpeta `/var/lib/neo4j/import`. Este proceso es la instancia final de ejecución del Dockerfile. Una vez realizado el mismo, tenemos una instancia de Neo4j con los datos cargados, lista para ser utilizada.

Nodos: 

-	Usuarios con la propiedad: User id
-	Movies con la propiedades:  Titulo, Rating_mean
-	Genres  con la propiedad: Genre_id

Relaciones:

-	Watched (user-movie) con la propiedad: Rating
-	Favorite (user-genre)
-	Genres (Movie-genre)
-	Similar (Movie-Movie) con la propiedad : relevance

### CONSUMO

Por último, a fin de testear el funcionamiento de la ddbb, se ejecuta manualmente la query `movie_query.cql` para obtener las 5 primers peliculas que se le recomiendan al usuario con id = 4. Más precisamente, esta query busca para el usuario con id = 4, las peliculas que haya mirado con ranking más alto y genero más común y luego se trae todas las peliculas que son similares a estas, ordena por ranking y genero y finalmente devuelve las primeras 5 de ese listado como remcomendación para el usuario de id = 4. 

## INSTRUCCIONES DE USO

Para poder correr estos comandos en forma local, se asume que el usuario tiene instalados `git` y `docker`.

### Recomendador de películas por similitud de peliculas

1. Crear un directorio para bajar el contenido de este repositorio. Una vez hecho eso, posicionarse dentro del mismo y ejecutar

```
git clone https://github.com/aga-team/captureandstorageneo4j
```
2. Ir al directorio `src` y ejecutar el comando para construir el container usando la imagen `neo4j-load-movie:1`:

```
cd captureandstorageneo4j/src 

docker build -t neo4j-load-movie:1 .
```
Obs.: agregar al comando anterior la opción `--platform=linux/amd64` en caso de usar una Macbook com chip M1

La opción `-t` especifica el nombre y tag de la versión de la imágen, `.` especifica el contexto de construcción donde reside el `Dockerfile`

El proceso construcción del container demora aproximadamente 10 minutos.

4. Una vez finalizado el proceso, corremos el comando 

```docker images```

para verificar que nuestro container fue correctamente creado en nuestra máquina.

5. Ejecutar el container usando:

```docker run -it --name neo4j1 neo4j-load-movie:1```

Obs.: agregar al comando anterior la opción `--platform=linux/amd64` en caso de usar una Macbook com chip M1

Se recomienda configurar la memoria RAM asignada a Docker para que tenga un valor de al menos 4 Gb para evitar inconvenientes con la corrida. Este proceso demora unos 15 minutos y deja un prompt en una CLI interna al container que no debemos cerrar.

6. Al finalizar el paso anterior, abrimos una consola nueva y ejecutamos:

```
docker exec -ti neo4j1 cypher-shell -u neo4j -p test  -f movie_query.cql
```

Esto nos devuelve un listado con las 5 peliculas recomendadas.


