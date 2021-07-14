MATCH    (b:Users)-[r:WATCHED]->(m:Movies), (b)-[s:SIMILARITY]-(a:Users {userId:'4'})
WHERE    NOT((a)-[:WATCHED]->(m))
WITH     m, s.similarity AS similarity, toFloat(r.rating) AS rating
ORDER BY m.title, similarity DESC
WITH     m.title AS themovie, COLLECT(rating)[0..3] AS ratings
WITH     themovie, REDUCE(s = 0.0, c IN ratings | s+c)/size(ratings) AS reco 
ORDER BY reco DESC
LIMIT 5
RETURN   themovie AS movie, reco AS Recommendation ;

// ------ these are some queries from preliminary versions -------------------
//MATCH (u:Users {userId:"7"})-[:WATCHED]->(m:Movies)
//RETURN u.userId , m.title;
//
//MATCH (u:Users)-[:WATCHED]->(m:Movies {title:'Top Gun (1986)'})
//RETURN m.title, u.userId ;
//
// Collaborative Filtering: Use the ratings other users in the network to find items to recommend. 
// "Users who bought this thing, also bought that other thing."
//MATCH (m:Movies {title: 'Top Gun (1986)'})<-[:WATCHED]-(u:Users)-[:WATCHED]->(rec:Movies)
//RETURN rec.title AS recommendation, COUNT(*) AS usersWhoAlsoWatched
//ORDER BY usersWhoAlsoWatched DESC LIMIT 25 ;
//
// The cosine similarity of two users will tell us how similar two users' preferences for movies are. 
// Users with a high cosine similarity will have similar preferences
// Create a [:SIMILARITY] relationship between each user in the graph, where their cosine similarity is a property of the relationship. 
// The query that accomplishes this is:
//
//MATCH (p1:Users)-[x:WATCHED]->(m:Movies)<-[y:WATCHED]-(p2:Users)
//WITH  SUM( toFloat(x.rating) * toFloat(y.rating) ) AS xyDotProduct,
//      SQRT(REDUCE(xDot = 0.0, a IN COLLECT(toFloat(x.rating)) | xDot + a^2)) AS xLength,
//      SQRT(REDUCE(yDot = 0.0, b IN COLLECT(toFloat(y.rating)) | yDot + b^2)) AS yLength,
//      p1, p2
//MERGE (p1)-[s:SIMILARITY]-(p2)
//SET   s.similarity = xyDotProduct / (xLength * yLength) ;
//------------------------------------------------------------------
