## captureandstorageneo4j

How to run the application to recommend a movie by user similarity:
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
6) Making the movie query that gives the movies recoomended to a gven user:
docker exec -ti neo1 cypher-shell -u neo4j -p test  -f movie_by_user_query.cql
------------------------------------------------------------------------------------------------------------
How to run the application to recommend a movie by movie similarity:
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
9) Making the movie query that gives the movies recoomended to a gven user:
docker exec -ti neo4j1 cypher-shell -u neo4j -p test  -f movie_query.cql

------------------------------------------------------------------------------------------------------------

Why neo4j ?


