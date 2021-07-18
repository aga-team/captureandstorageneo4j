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

Nacido en 1991 de la mano de Guido Van Rossum, Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje multiparadigma, pues soporta la programación orientada a objetos (OOP), imperativa y, en menor medida, funcional. 

Python es un lenguaje interpretado, dinámico y multiplataforma que actualmente es administrado por la Python Software Foundation (PSF). El mismo posee una licencia de código abierto, denominada Python Software Foundation License.

Las motivaciones principales a la hora de utilizar este lenguaje para nuestro desarrollo fueron su simplicidad de uso, combinada con su amplia adopción en los entornos de trabajo de Data Science y el enorme soporte brindado por la comunidad.

Para más información sobre Python, visite https://www.python.org/about/

### NEO4J

#### Introduccion

Neo4j es una base de datos abierta, NoSQL y con soporte de ACID que almacena la información en forma nativa utilizando una estructura basada en grafos. Su código fuente, escrito en Java y Scala, está disponible en forma gratuita en Github desde 2007. También se puede probar la misma bajando una aplicación de escritorio en su sitio web. 

Neo4j se define como una base de grafos nativa ya que implementa de forma eficiente las propiedades de los modelos de grafos a la hora de almacenar los datos. Esto quiere decir que los datos están almacenados siguiendo el mismo esquema que podemos plantear en un pizarron y la base de datos utiliza punteros para navegar y recorrer el grafo. A diferencia de los procesadores de grafos o las librerias en memoria, Neo4j tambien provee caracteristicas propias de las bases de datos convencionales, como ser el soporte transcaccional de tipo ACID, soporte para clusters y tolerancia a fallos, lo cual la convierte en candidata ideal para usar grafos en entornos productivos. 

Algunas de las prestaciones que vuelven popular a Neo4j entre desarrolladores, arquitectos y DBAs son: 

- Cypher, el lenguaje de consulta declaratio, similar a SQL pero optimizado para grafos.
- Tiempo de exploracion constantes en grafos grandes gracias a la representacion eficiente de nodos y relaciones que posibilita escalar a millones de nodos en hardware moderado.
- Esquema de modelo de grafos con propiedades flexible, lo cual posibilita la adaptacion con el paso del tiempo para agregar nuevas relaciones cuando las necesidades del proyecto cambian.
- Drivers para los lenguajes de programacion mas populares, incluyendo Java, JavaScript, .NET, Python, y muchos mas.

#### El modelo de grafos con propiedaes

El enfoque utilizado por Neo4j para manejar los componentes de la base de datos basada en grafos es el del **modelo de grafos con propiedades**, donde los datos están organizados como **nodos**, **relaciones** y **propiedades** (datos almacenados en los nodos o en las relaciones).

Los **nodos** son las entidades del grafo. Estos pueden guardar un número indefinido de atributos como pares llave:valor llamados **propiedades**. Los nodos pueden ser identificados mediante etiquetas, las cuales representan los diferentes roles en un dominio dado. Esta etiquetas también pueden utilizarse para añadir metadata (como índices o información sobre vínculos) a ciertos nodos.

Las **relaciones** proveen conexiones dirigidas, nombradas y semanticamente relevantes entre entidades nodales. (Por ejemplo _Empleado_ TRABAJA_PARA _Compañía_)



Para probar Neo4j, visite https://neo4j.com/try-neo4j/

### DOCKER

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

How to run the application to recommend a movie by user similarity (recommendation system based in collaborative filtering):

1) Go to the local direcotry in your computer where you will clone the git repository :

git clone https://github.com/aga-team/captureandstorageneo4j

2) Go to recommendation_by_user_similarity dir: 

cd captureandstorageneo4j/recommendation_movie_by_user_similarity 

3) Run the following command to build the docker image (-t specifies a name and version tag for the image, . specifies the "build context"   directory where Dockerfile ), it takes approximately 10 min  :

docker build -t neo4j-load:1 .

4) After the build is completed we should see our container in the list of Docker images on our machine: 

docker images

5) Running container (it takes approximately 13 min):

docker run -it --name neo1 neo4j-load:1 

6) Before runnig the following command open a new terminal to run it. We use Cpyher Query Language to extract data from neo4j database making the query that gives the 5 movies recommended to a gven user:

docker exec -ti neo1 cypher-shell -u neo4j -p test  -f movie_by_user_query.cql

------------------------------------------------------------------------------------------------------------

How to run the application to recommend a movie by movie similarity (recommendation system based in content):

1) Go to the local direcotry in your computer where you will clone the git repository :

git clone https://github.com/aga-team/captureandstorageneo4j

2) Go to recommendation_by_movie_similarity dir: 

cd captureandstorageneo4j/recommendation_movie_by_movie_similarity 

3) Run the following command to build the docker image (-t specifies a name and version tag for the image, . specifies the "build context"   directory where Dockerfile ) , it takes approximately 20 min  and the image size is 1.81 GB :

docker build -t neo4j-load-movie:1 .

4) After the build is completed we should see our container in the list of Docker images on our machine: 

docker images

5) Running containe takes approximately 15 min (it may require additional memory in docker configutation to run python script, I used 4 GB but it should be more than 1 GB at least, this might be a good reason to try to do all in cypher to check if it is more efficient) :

docker run -it --name neo4j1 neo4j-load-movie:1

6) Before runnig the following command open another terminal to run it. We will use Cpyher Query Language to extract data from neo4j database making the movie query that gives the 5 movies recommended to a gven user:

docker exec -ti neo4j1 cypher-shell -u neo4j -p test  -f movie_query.cql

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

-------------------------------------------------------------------------------------------------------------





------------------------------------------------------------------------------------------------------------




