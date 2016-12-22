import pandas as pd
import os

def loadDataSet():
    ratings_filename=os.path.join("D:\python\ml-20m\ml-20m","ratings.csv")
    #print(ratings_filename)
    all_ratings = pd.read_csv(ratings_filename)
    all_ratings["timestamp"]=pd.to_datetime(all_ratings["timestamp"],unit='s')
    #print(all_ratings[:5])
    all_ratings["favorable"] = all_ratings["rating"] > 3
    #print(all_ratings[10:15])
    ratings = all_ratings[all_ratings["userId"].isin(range(200))]
    #print(ratings)
    favorable_ratings=ratings[ratings["favorable"]==True]
    #print(favorable_ratings)
    favorable_reviews_by_users=dict((k,frozenset(v.values)) for k,v in favorable_ratings.groupby("userId")["movieId"] )
    #print(favorable_reviews_by_users)
    num_favorable_by_movie = ratings[["movieId","favorable"]].groupby("movieId").sum()
    #print(num_favorable_by_movie.sort("favorable",ascending=False)[:5])
    frequent_itemsets={}
    min_support=50
    frequent_itemsets[1]=dict( (frozenset((movie_id,)),row["favorable"]) for movie_id,row in num_favorable_by_movie.iterrows() if row["favorable"] > min_support  )


if __name__=="__main__":
    loadDataSet()