CREATE CONSTRAINT ON (u:Users) ASSERT u.userId IS UNIQUE;
CREATE CONSTRAINT ON (m:Movies) ASSERT m.movieId IS UNIQUE;
CREATE CONSTRAINT ON (g:Genres) ASSERT g.genres IS UNIQUE;

LOAD CSV WITH HEADERS FROM "file:///users.csv" AS row
MERGE (:Users {userId: toInteger(row.userId)});

LOAD CSV WITH HEADERS FROM "file:///movies_new.csv" AS row
FIELDTERMINATOR '|'
WITH row WHERE row.rating_mean IS NOT NULL
MERGE (:Movies {movieId: toInteger(row.movieId),title:row.title, rating_mean:toFloat(row.rating_mean)});

LOAD CSV WITH HEADERS FROM "file:///genres.csv" AS row
MERGE (:Genres {genres: row.genres});

LOAD CSV WITH HEADERS FROM "file:///users_movies.csv" AS row 
FIELDTERMINATOR '|'
WITH row WHERE row.rating IS NOT NULL
MATCH (user:Users {userId: toInteger(row.userId) }), (movie:Movies {movieId: toInteger(row.movieId)}) 
MERGE (user)-[r:WATCHED {rating: toFloat(row.rating)}]->(movie) ;

LOAD CSV WITH HEADERS FROM "file:///users_genres.csv" AS row
FIELDTERMINATOR '|'
MATCH (user:Users {userId:  toInteger(row.userId) }),(genres:Genres {genres: row.genre} )
MERGE (user)-[f:FAVORITE]->(genres) ;

LOAD CSV WITH HEADERS FROM "file:///movies_genres.csv" AS row
FIELDTERMINATOR '|'
WITH row WHERE row.genres IS NOT NULL
MATCH (movie:Movies {movieId: toInteger(row.movieId) }), (genres:Genres {genres: row.genres})
MERGE (movie)-[:GENRES]->(genres);

LOAD CSV WITH HEADERS FROM "file:///movies_similarity.csv" AS row
FIELDTERMINATOR '|'
MATCH (movie1:Movies {movieId: toInteger(row.movieId)})
MATCH (movie2:Movies {movieId: toInteger(row.sim_moveId)})
MERGE (movie1)-[:SIMILAR {relevance: row.relevance}]->(movie2);

