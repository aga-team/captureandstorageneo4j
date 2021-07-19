import pandas as pd
import numpy as np
import datetime
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv("import/movies.csv")
genome_scores_data = pd.read_csv("import/genome-scores.csv")
ratings_data = pd.read_csv("import/ratings.csv")

scores_pivot = genome_scores_data.pivot_table(index =["movieId"],columns = ["tagId"],values = "relevance").reset_index()
mov_tag_df = movies_data.merge(scores_pivot, left_on="movieId",right_on="movieId", how="left")
mov_tag_df = mov_tag_df.fillna(0)
mov_tag_df = mov_tag_df.drop(['title','genres'], axis = 1)
mov_tag_df.drop(mov_tag_df.tail(18).index,inplace=True)

def set_genres(genres,col):
    if genres in col.split('|'): 
        return 1
    else: return 0

mov_genres_df_Action=movies_data.apply(lambda x:set_genres("Action",x['genres']),axis=1)
mov_genres_df1=mov_genres_df_Action.to_frame()
mov_genres_df1=mov_genres_df1.rename(columns={0: 'Action'})

mov_genres_df_Adventure=movies_data.apply(lambda x:set_genres("Adventure",x['genres']),axis=1)
mov_genres_df2=mov_genres_df_Adventure.to_frame()
mov_genres_df2=mov_genres_df2.rename(columns={0: 'Adventure'})

mov_genres_df_Animation=movies_data.apply(lambda x:set_genres("Animation",x['genres']),axis=1)
mov_genres_df3=mov_genres_df_Animation.to_frame()
mov_genres_df3=mov_genres_df3.rename(columns={0: 'Animation'})

mov_genres_df_Children=movies_data.apply(lambda x:set_genres("Children",x['genres']),axis=1)
mov_genres_df4=mov_genres_df_Children.to_frame()
mov_genres_df4=mov_genres_df4.rename(columns={0: 'Children'})

mov_genres_df_Comedy=movies_data.apply(lambda x:set_genres("Comedy",x['genres']),axis=1)
mov_genres_df5=mov_genres_df_Comedy.to_frame()
mov_genres_df5=mov_genres_df5.rename(columns={0: 'Comedy'})

mov_genres_df_Crime=movies_data.apply(lambda x:set_genres("Crime",x['genres']),axis=1)
mov_genres_df6=mov_genres_df_Crime.to_frame()
mov_genres_df6=mov_genres_df6.rename(columns={0: 'Crime'})

mov_genres_df_Documentary=movies_data.apply(lambda x:set_genres("Documentary",x['genres']),axis=1)
mov_genres_df7=mov_genres_df_Documentary.to_frame()
mov_genres_df7=mov_genres_df7.rename(columns={0: 'Documentary'})

mov_genres_df_Drama=movies_data.apply(lambda x:set_genres("Drama",x['genres']),axis=1)
mov_genres_df8=mov_genres_df_Drama.to_frame()
mov_genres_df8=mov_genres_df8.rename(columns={0: 'Drama'})

mov_genres_df_Fantasy=movies_data.apply(lambda x:set_genres("Fantasy",x['genres']),axis=1)
mov_genres_df9=mov_genres_df_Fantasy.to_frame()
mov_genres_df9=mov_genres_df9.rename(columns={0: 'Fantasy'})

mov_genres_df_Film_Noir=movies_data.apply(lambda x:set_genres("Film-Noir",x['genres']),axis=1)
mov_genres_df10=mov_genres_df_Film_Noir.to_frame()
mov_genres_df10=mov_genres_df10.rename(columns={0: 'Film-Noir'})

mov_genres_df_Horror=movies_data.apply(lambda x:set_genres("Horror",x['genres']),axis=1)
mov_genres_df11=mov_genres_df_Horror.to_frame()
mov_genres_df11=mov_genres_df11.rename(columns={0: 'Horror'})

mov_genres_df_Musical=movies_data.apply(lambda x:set_genres("Musical",x['genres']),axis=1)
mov_genres_df12=mov_genres_df_Musical.to_frame()
mov_genres_df12=mov_genres_df12.rename(columns={0: 'Musical'})

mov_genres_df_Mystery=movies_data.apply(lambda x:set_genres("Mystery",x['genres']),axis=1)
mov_genres_df13=mov_genres_df_Mystery.to_frame()
mov_genres_df13=mov_genres_df13.rename(columns={0: 'Mystery'})

mov_genres_df_Romance=movies_data.apply(lambda x:set_genres("Romance",x['genres']),axis=1)
mov_genres_df14=mov_genres_df_Romance.to_frame()
mov_genres_df14=mov_genres_df14.rename(columns={0: 'Romance'})

mov_genres_df_Sci_Fi=movies_data.apply(lambda x:set_genres("Sci-Fi",x['genres']),axis=1)
mov_genres_df15=mov_genres_df_Sci_Fi.to_frame()
mov_genres_df15=mov_genres_df15.rename(columns={0: 'Sci-Fi'})


mov_genres_df_Thriller=movies_data.apply(lambda x:set_genres("Thriller",x['genres']),axis=1)
mov_genres_df16=mov_genres_df_Thriller.to_frame()
mov_genres_df16=mov_genres_df16.rename(columns={0: 'Thriller'})

mov_genres_df_War=movies_data.apply(lambda x:set_genres("War",x['genres']),axis=1)
mov_genres_df17=mov_genres_df_War.to_frame()
mov_genres_df17=mov_genres_df17.rename(columns={0: 'War'})

mov_genres_df_Western=movies_data.apply(lambda x:set_genres("Western",x['genres']),axis=1)
mov_genres_df18=mov_genres_df_Western.to_frame()
mov_genres_df18=mov_genres_df18.rename(columns={0: 'Western'})

mov_genres_df_no_genres_listed=movies_data.apply(lambda x:set_genres("(no genres listed)",x['genres']),axis=1)
mov_genres_df19=mov_genres_df_no_genres_listed.to_frame()
mov_genres_df19=mov_genres_df19.rename(columns={0: 'no genres listed'})

Prueba=pd.concat([movies_data["movieId"],
                  mov_genres_df1["Action"],
                  mov_genres_df2["Adventure"],
                  mov_genres_df3["Animation"],
                 mov_genres_df4["Children"],
                 mov_genres_df5["Comedy"],
                 mov_genres_df6["Crime"],
                 mov_genres_df7["Documentary"],
                 mov_genres_df8["Drama"],
                 mov_genres_df9["Fantasy"],
                 mov_genres_df10["Film-Noir"],
                 mov_genres_df11["Horror"],
                 mov_genres_df12["Musical"],
                 mov_genres_df13["Mystery"],
                 mov_genres_df14["Romance"],
                 mov_genres_df15["Sci-Fi"],
                 mov_genres_df16["Thriller"],
                 mov_genres_df17["War"],
                 mov_genres_df18["Western"],
                 mov_genres_df19["no genres listed"]],axis=1)

Prueba.drop(Prueba.tail(18).index,inplace=True)
mov_genres_df=Prueba

def set_year(title):
    year = title.strip()[-5:-1]
    if year.isnumeric() == True: return int(year)
    else: return 1800
    
eje = movies_data.apply(lambda x: set_year(x['title']),axis=1)
movies_years = movies_data.apply(lambda x: set_year(x['title']),axis=1)
movies_years = movies_years.to_frame()
movies_years = movies_years.rename(columns={0: 'year'})

def set_year_group(year):
    if (year < 1900): return 0
    elif (1900 <= year <= 1975): return 1
    elif (1976 <= year <= 1995): return 2
    elif (1996 <= year <= 2003): return 3
    elif (2004 <= year <= 2009): return 4
    elif (2010 <= year): return 5
    else: return 0

movies_year_group = movies_years[["year"]].apply(lambda x:set_year_group(x['year']), axis=1)
movies_year_group = movies_year_group.to_frame()
movies_year_group = movies_year_group.rename(columns={0: 'year_group'})

movies_rat_mean = ratings_data[["movieId","rating"]].groupby(['movieId']).mean()
movies_rat_mean = movies_rat_mean.rename(columns={"rating": 'rating_mean'}).reset_index()

movies_rat_count = ratings_data[["movieId","rating"]].groupby(['movieId']).count()
movies_rat_count = movies_rat_count.rename(columns={"rating": 'rating_counts'}).reset_index()

movieId_year_group_rating_count_mean=pd.concat([movies_rat_count[["movieId"]],
                                     movies_year_group[["year_group"]],
                                     movies_rat_mean[["rating_mean"]],   
                                     movies_rat_count[["rating_counts"]],
                                    ],axis=1)

movieId_year_group_rating_count_mean.dropna(subset = ["movieId"], inplace=True)
mov_rating_df = movieId_year_group_rating_count_mean

mov_tag_df = mov_tag_df.set_index('movieId')
mov_rating_df = mov_rating_df.set_index('movieId')
mov_genres_df = mov_genres_df.set_index('movieId')

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
vec1 = np.array([[1,1,0,1,1]])
vec2 = np.array([[0,1,0,1,1]])

cos_tag = cosine_similarity(mov_tag_df.values)*0.5

cos_genres = cosine_similarity(mov_genres_df.values)*0.25
cos_rating = cosine_similarity(mov_rating_df.values)*0.25
cos = cos_tag+cos_genres+cos_rating

cols = mov_tag_df.index.values
inx = mov_tag_df.index

movies_sim = pd.DataFrame(cos, columns=cols, index=inx)

movies_sim.loc[movies_sim.index == 9].reset_index(). \
  melt(id_vars='movieId', var_name='sim_moveId',
  value_name='relevance')

movies_sim.loc[movies_sim.index == 9].reset_index(). \
  melt(id_vars='movieId', var_name='sim_moveId',
  value_name='relevance') .\
  sort_values('relevance', axis=0, ascending=False)[1:6]

def get_similar(movieId):
  df = movies_sim.loc[movies_sim.index == movieId].reset_index(). \
  melt(id_vars='movieId', var_name='sim_moveId',
  value_name='relevance'). \
  sort_values('relevance', axis=0, ascending=False)[1:6]
  return df

movies_similarity = pd.DataFrame(columns=['movieId','sim_moveId','relevance'])

for x in movies_sim.index.tolist():
  movies_similarity = movies_similarity.append(get_similar(x))

def movie_recommender(movieId):
    df = movies_sim.loc[movies_sim.index == movieId].reset_index(). \
            melt(id_vars='movieId', var_name='sim_moveId', value_name='relevance'). \
            sort_values('relevance', axis=0, ascending=False)[1:6]
    df['sim_moveId'] = df['sim_moveId'].astype(int)
    sim_df = movies_data.merge(df, left_on='movieId', right_on='sim_moveId', how='inner'). \
                sort_values('relevance', axis=0, ascending=False). \
                loc[: , ['movieId_y','title','genres']]. \
                rename(columns={ 'movieId_y': "movieId" })
    return sim_df


users_df = pd.DataFrame(ratings_data['userId'].unique(), columns=['userId'])
movies_df = movies_data.drop('genres', axis = 1)

agg_rating_avg = ratings_data.groupby(['movieId']).agg({'rating': np.mean}).reset_index()
agg_rating_avg.columns = ['movieId', 'rating_mean']

movies_df = movies_df.merge(agg_rating_avg, left_on='movieId', right_on='movieId', how='left')

genres = [
    "Action",
    "Adventure",
    "Animation",
    "Children",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western",
    "(no genres listed)"]


genres_df = pd.DataFrame(genres, columns=['genres'])

users_movies_df = ratings_data.drop('timestamp', axis = 1)
movies_genres_df = movies_data.drop('title', axis = 1)

def get_movie_genres(movieId):
    movie = movies_genres_df[movies_genres_df['movieId']==movieId]
    genres = movie['genres'].tolist()
    df = pd.DataFrame([b for a in [i.split('|') for i in genres] for b in a], columns=['genres'])
    df.insert(loc=0, column='movieId', value=movieId)
    return df

movies_genres=pd.DataFrame(columns=['movieId','genres'])
for x in movies_genres_df['movieId'].tolist():
    movies_genres=movies_genres.append(get_movie_genres(x))

user_genres_df = ratings_data.merge(movies_data, left_on='movieId', right_on='movieId', how='left')
user_genres_df.drop(['movieId','rating','timestamp','title'], axis = 1, inplace=True)

def get_favorite_genre(userId):
    user = user_genres_df[user_genres_df['userId']==userId]
    genres = user['genres'].tolist()
    movie_list = [b for a in [i.split('|') for i in genres] for b in a]
    counter = Counter(movie_list)
    return counter.most_common(1)[0][0]

users_genres = pd.DataFrame(columns=['userId','genre'])
for x in users_df['userId'].tolist():
    users_genres = users_genres.append(pd.DataFrame([[x,get_favorite_genre(x)]], columns=['userId','genre']))

    
users_df.to_csv('import/users.csv', sep='|', header=True, index=False)
movies_df.to_csv('import/movies_new.csv', sep='|', header=True, index=False)
genres_df.to_csv('import/genres.csv', sep='|', header=True, index=False)
users_movies_df.to_csv('import/users_movies.csv', sep='|', header=True, index=False)
movies_genres.to_csv('import/movies_genres.csv', sep='|', header=True, index=False)
users_genres.to_csv('import/users_genres.csv', sep='|', header=True, index=False)
movies_similarity.to_csv('import/movies_similarity.csv', sep='|', header=True, index=False)

