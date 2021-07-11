LOAD CSV WITH HEADERS FROM 'file:///movies.csv' AS row
MERGE  (movie:Movies {movieId: row.movieId,title: row.title} ) ;

LOAD CSV WITH HEADERS FROM 'file:///ratings.csv' AS row
MERGE (user:Users {userId: row.userId} );

LOAD CSV WITH HEADERS FROM 'file:///ratings.csv' AS row
MATCH (user:Users {userId: row.userId})
MATCH (movie:Movies {movieId: row.movieId})
MERGE (user)-[:WATCHED {rating: row.rating}]->(movie);

MATCH (p1:Users)-[x:WATCHED]->(m:Movies)<-[y:WATCHED]-(p2:Users)
WITH  SUM( toFloat(x.rating) * toFloat(y.rating) ) AS xyDotProduct,
      SQRT(REDUCE(xDot = 0.0, a IN COLLECT(toFloat(x.rating)) | xDot + a^2)) AS xLength,
      SQRT(REDUCE(yDot = 0.0, b IN COLLECT(toFloat(y.rating)) | yDot + b^2)) AS yLength,
      p1, p2
MERGE (p1)-[s:SIMILARITY]-(p2)
SET   s.similarity = xyDotProduct / (xLength * yLength) ;





