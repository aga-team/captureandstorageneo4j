# CAPTURA Y ALMACENAMIENTO DE DATOS USANDO NEO4J

## INTRODUCCION

El código almacenado en este repositorio constituye el entregable final para la materia "Captura y almacenamiento de la información" de la "Especialización en Inteligencia de Datos orientada a Big Data" dictada en la Facultad de Informática de la Universidad Nacional de La Plata.

https://www.info.unlp.edu.ar/especializacion-en-inteligencia-de-datos-orientada-a-big-data/

Alumnos: 

- Dra. Analisa Mariazzi (analisam@gmail.com)
- Dr. Gastón Giordano (gaston2031@gmail.com)
- Lic. Alejo Hernandez (homocuadratus@gmail.com)

## OBJETIVO

Estudiar las fases de captura y almacenamiento de la información implementando un prototipo de recomendador de películas basado en Python y Neo4j.

## DESCRIPCION DE LAS HERRAMIENTAS UTILIZADAS

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

Captura de la información (via wget en el dockerfile)

### PREPROCESAMIENTO
 
Preprocesamiento (via script python)

Definicion del algoritmo para calcular la similitud entre dos películas (via script python)

Fase 1: Armamos una matriz  de movies vs tags con la relevancia del tag en la celda

Fase 2: Armamos una matriz películas vs generos con el flag si esta presente el genero en cada celda

Fase 3: Defino una segmentación por años de las distintas películas (categorica ordinal del 1 al 5) y calculo un rating promedio dentro de cada una de esas categorías

Fase 4: Calculo la similitud entre dos películas como combinación lineal de las cosine similarity entre tag relevance, genres y ratings.

Fase 5: Generacion de contenido a ser cargado en neo4j

### ALMACENAMIENTO

Carga de nodos y relaciones en Neo4j leyendo el output anterior

Nodos: 

-	Usuarios
o	User id
-	Movies
o	Titulo
o	Rating_mean
-	Genres
o	Genre_id

Relaciones:

-	Watched (user-movie)
o	Rating
-	Favorite (user-genre)
-	Genres (Movie-genre)
-	Similar (Movie-Movie)
o	relevance

### CONSUMO

Consulta de la ddbb para obtener las 5 peliculas mas relevantes para un usuario dado

## INSTRUCCIONES DE USO

Para poder correr estos comandos en forma local, se asume que el usuario tiene instalados `git` y `docker`.

### Recomendador de películas por similitud de usuarios

1. Crear un directorio para bajar el contenido de este repositorio. Una vez hecho eso, posicionarse dentro del mismo y ejecutar

```
git clone https://github.com/aga-team/captureandstorageneo4j
```
2. Acceder al directorio `recommendation_by_user_similarity` y construir el container de Docker usando la imágen `neo4j-load:1`:

```
cd captureandstorageneo4j/recommendation_movie_by_user_similarity 

docker build -t neo4j-load:1
```
La opción `-t` especifica el nombre y tag de la versión de la imágen, `.` especifica el contexto de construcción donde reside el `Dockerfile`

El proceso construcción del container demora aproximadamente 10 minutos.

4. Una vez finalizado el proceso, corremos el comando 

```docker images```

para verificar que nuestro container fue correctamente creado en nuestra máquina.

5. Ejecutar el container usando:

```docker run -it --name neo1 neo4j-load:1```

Este proceso demora unos 15 minutos.

6. Al finalizar el proceso de ejecución, se abre una terminal interna que nos permite ejecutar una consulta de Cypher para encontrar las 5 películas para ser romendadas a un cierto usuario. El comandos a emplear es:

```
docker exec -ti neo1 cypher-shell -u neo4j -p test  -f movie_by_user_query.cql
```

### Recomendador de películas por similitud de contenido

1. Idem anterior
2. Ir al directorio `recommendation_by_movie_similarity` y ejecutar el comando para construir el container:

```
cd captureandstorageneo4j/recommendation_movie_by_movie_similarity 

docker build -t neo4j-load-movie:1
```

Este proceso demora aproximadamente 20 minutos, produciendo un container de 1.81 GB

3. Idem anterior
4. Ejecutamos el container usando:

```docker run -it --name neo4j1 neo4j-load-movie:1```

Este proceso demora unos 15 minutos. Se recomienda configurar la memoria RAM asignada a Docker para que tenga un valor de al menos 4 Gb para evitar inconvenientes con la corrida.

5. Finalmente, ejecutamos el comando

```
docker exec -ti neo4j1 cypher-shell -u neo4j -p test  -f movie_query.cql
```

El mismo abre una consola nueva y ejecuta una consulta de Cypher para obtener las 5 peliculas recomendadas usando este criterio alternativo.


------------------------------------------------------------------------------------------------------------

Recommender systems


Recommender systems can be broadly divided into two categories : content based and collaborative filtering based.

Content based recommender systems try to guess the features or behavior of a user given the movie’s features, the user 
reacted positively to. They focus on the properties of the content to recommend movies to a user. 
In this work, we focus on the property of the “similarity” with the assumption that 
if a user likes a certain item like a movie, he may like similar movies in the future.
These assumption holds to a certain extent. For example, if I like to watch movies like Lord of the Rings, Pirates of the Caribbean, it’s likely that I’ll like other fantasy/adventure based movies like The The Hobbit or Stardust.

To find similar movies, one can find the most similar items to a particular instance based on a given distance metric like euclidean, jaccard similarity , minkowsky or custom distance measures.
One can simply find the most similar similar movies and recommend them to user. 
In this case we have retrieved top 5 most similar movies’s to a given query.
For example, if I query “The Matrix” to the recommender system, it will return me top 5 movies’s similar to "The Matrix".
One can use genre, tags, rating as features.

So if we know what movies a user has watched, we can use this information to recommend similar movies:
recommending movies similar to those the user has already watched. 

Content recommendation by overlapping genres:

Given the genres, one can know which users like which genre, as a result, we can obtain 
features corresponding to that particular user, depending on how he reacts to movies of that genre. 
Once we know the likings of the user we can embed him in an embedding space using the feature vector generated 
and recommend him according to his choice. 
During recommendation, the similarity metrics are calculated from the item’s feature vectors and the user’s preferred feature vectors from his
previous records. Then, the top few are recommended.
Similarity metrics are mathematical measures which are used to determine how similar is a vector to a given vector.
Here, we will use as similarity metrics the cosine similarity (the Cosine angle between the vectors).

Content-based filtering does not require other users' data during recommendations to one user.

Collaborative filtering:

Collaborative filtering does not need the features of the items to be given. 
Every user and item is described by a feature vector or embedding.
It creates embedding for both users and items on its own. It embeds both users and items in the same embedding space.
It considers other user’s reactions while recommending a particular user. 
It notes which items a particular user likes and also the items that the users with behavior and likings like him likes, to 
recommend items to that user. It collects user feedbacks on different items and uses them for recommendations.
One can use the ratings of other users in the network to find movies to recommend.
"Users who watched and like this movie, also watched and looked that other movie."

The cosine similarity of two users will tell us how similar two users' preferences for movies are. 
Users with a high cosine similarity will have similar preferences.
One can create a [:SIMILARITY] relationship between each user in the graph, where their cosine similarity 
is a property of the relationship to find the users with the most similar preferences to a given user, 
according to cosine similarity function.
Answering questions like: 
- Who are the 10 users with tastes in movies most similar to mine? 
- What movies have they rated highly that I haven’t seen yet?

With the similarities added to the graph, it is easy to make a cypher query that let us
view the user's (with id=4) graph of 5-nearest neighbors in descending order, that 
rated movies most similarly to user (with id = 4).




