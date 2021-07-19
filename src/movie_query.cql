MATCH (u1:Users)-[:WATCHED]->(m3:Movies)
WHERE u1.userId=8
WITH [i in m3.movieId | i] as movies
MATCH path = (u:Users)-[:WATCHED]->(m1:Movies)-[s:SIMILAR]->(m2:Movies),
(m2)-[:GENRES]->(g:Genres),
(u)-[:FAVORITE]->(g)
WHERE u.userId =8 and not m2.movieId in movies
RETURN distinct u.userId as userId, g.genres as genres,
m2.title as title, m2.rating_mean as rating
ORDER BY m2.rating_mean descending
LIMIT 5 ;
//
// ------ These are some tests queries of preliminary version -----------
//MATCH path = (u:Users)-[:WATCHED]->(m1:Movies)
//WHERE u.userId=4
//RETURN u.userId, m1.title, m1.rating_mean
//
//MATCH path = (u:Users)-[:FAVORITE]->(g:Genres)
//WHERE u.userId=4
//RETURN u.userId, g.genres
//
//MATCH path = (u:Users)-[:WATCHED]->(m1:Movies)-[s:SIMILAR]->(m2:Movies)
//WHERE u.userId=4
//RETURN u.userId, m1.title, m2.title, m2.rating_mean
//
//MATCH path = (u:Users)-[:WATCHED]->(m1:Movies)-[s:SIMILAR]->
(m2:Movies),
//(m2)-[:GENRES]->(g:Genres),
//(u)-[:FAVORITE]->(g)
//WHERE  u.userId=4
//RETURN u.userId, g.genres, m1.title, m2.title, m2.rating_mean
//
//MATCH path = (u:Users)-[:WATCHED]->(m1:Movies)
//WHERE u.userId=8
// // WHERE u1.userId=4
//RETURN u.userId, m1.title, m1.rating_mean
//
// -----------------------------------------------------------------------------


