## captureandstorageneo4j

How to run the application to recommend a movie by user similarity (recommendation system based in collaborative filtering):
1) Go to the local direcotry in your computer where you will clone the git repository :
git clone https://github.com/aga-team/captureandstorageneo4j
2) Go to recommendation_by_user_similarity dir: 
cd captureandstorageneo4j/recommendation_by_user_similarity 
3) Run the following command to build the docker image (-t specifies a name and version tag for the image, . specifies the "build context"   directory where Dockerfile ), it takes approximately 10 min  :
docker build -t neo4j-load:1 .
4) After the build is completed we should see our container in the list of Docker images on our machine: 
docker images
5) Running container (it takes approximately 13 min):
docker run -it --name neo1 neo4j-load:1 
6) We use Cpyher Query Language to extract data from neo4j database: we make the movie query that gives the movies recommended to a gven user:
docker exec -ti neo1 cypher-shell -u neo4j -p test  -f movie_by_user_query.cql
------------------------------------------------------------------------------------------------------------
How to run the application to recommend a movie by movie similarity (recommendation system based in content):
1) Go to the local direcotry in your computer where you will clone the git repository :
git clone https://github.com/aga-team/captureandstorageneo4j
2) Go to recommendation_by_movie_similarity dir: 
cd captureandstorageneo4j/recommendation_by_movie_similarity 
3) Run the following command to build the docker image (-t specifies a name and version tag for the image, . specifies the "build context"   directory where Dockerfile ) , it takes approximately 30 min  :
docker build -t neo4j-load-movie:1 .
4) After the build is completed we should see our container in the list of Docker images on our machine: 
docker images
5) Running container (it takes approximately 30 min):
docker run -it --name neo4j1 neo4j-load-movie:1
6) Run other cypher commands to check nodes loaded in graph database:
docker exec -ti neo4j1 -u neo4j -p test "CALL  db.labels();" 
7) Run other cypher commands to check relationships loaded in graph database:
docker exec -ti neo4j1 -u neo4j -p test "CALL db.relationshipTypes();"
9) We use Cpyher Query Language to extract data from neo4j database:we make the movie query that gives the movies recoomended to a gven user:
docker exec -ti neo4j1 cypher-shell -u neo4j -p test  -f movie_query.cql

------------------------------------------------------------------------------------------------------------

#Recommender systems

Recommender systems can be broadly divided into two categories : content based and collaborative filtering based.

Content based recommender systems try to guess the features or behavior of a user given the movie’s features, the user 
reacted positively to. They focus on the properties of the content to recommend movies to a user. 
In this work, we focus on the property of the “similarity” with the assumption that 
if a user likes a certain item like a movie, he may like similar movies in the future.
These assumption holds to a certain extent. For example, if I like to watch movies like Lord of the Rings, Pirates of the Caribbean, it’s likely that I’ll like other fantasy/adventure based movies like The The Hobbit or Stardust.

To find similar movies, one can use K-nearest neighbor(KNN). K-nearest neighbor finds the k most similar items to a particular instance based on a given distance metric like euclidean, jaccard similarity , minkowsky or custom distance measures.
In an unsupervised setting such as this context one can simply find the neighbors and use them to recommend similar items. 
In rough words, to suggest similar movies we first find k-similar movies’s and recommend them to user. 
In this case we have retrieved top 5 most similar movies’s to a given query.
For example, if I query “Naruto” to the recommender system, it will return me top 5 movies’s similar to Naruto.
One can use genre, tags, rating as features.

If we know what movies a user has watched, we can use this information to recommend similar movies:
Recommend movies similar to those the user has already watched. 
Content recommendation by overlapping genres: given these genres, we can know which users like which genre, as a result, we can obtain 
features corresponding to that particular user, depending on how he reacts to movies of that genre. 
Once we know the likings of the user we can embed him in an embedding space using the feature vector generated 
and recommend him/her according to his choice. 
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

The cosine similarity of two users will tell us how similar two users' preferences for movies are. Users with a high cosine similarity will have similar preferences
We want to create a [:SIMILARITY] relationship between each user in the graph, where their cosine similarity 
is a property of the relationship. 
Find the users with the most similar preferences to user with id=4, according to cosine similarity function.
Who are the 10 users with tastes in movies most similar to mine? 
What movies have they rated highly that I haven’t seen yet?"
With the similarities added to the graph, it is easy to view your k-nearest neighbors. 
Let’s view the user's (with id=4) graph of 5-nearest neighbors:
These users, in descending order, rated movies most similarly to user with id = 4.

----------------------------------------------------------------------------------------------------------------------------------






