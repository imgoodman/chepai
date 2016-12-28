import pandas as pd
import os
from collections import defaultdict
import sys
from operator import itemgetter

def loadDataSet():
    ratings_filename=os.path.join("D:\python\ml-20m\ml-20m","ratings.csv")
    #print(ratings_filename)
    all_ratings = pd.read_csv(ratings_filename)
    all_ratings["timestamp"]=pd.to_datetime(all_ratings["timestamp"],unit='s')
    #print(all_ratings[:5])
    all_ratings["favorable"] = all_ratings["rating"] > 3
    #print(all_ratings[10:15])#返回第10到15行
    # print(all_ratings['userId'])#返回userId列
    # print(all_ratings["userId"].isin(range(200)))#判断userId是否在0-200这个list中
    ratings = all_ratings[all_ratings["userId"].isin(range(200))]#返回userId在0-200之间的所有数据
    # print(ratings)
    favorable_ratings=ratings[ratings["favorable"]==True]#评分超过3分的算喜爱  的所有数据
    # print(favorable_ratings.groupby('userId')['movieId'])
    # for k,v in favorable_ratings.groupby('userId')['movieId']:
    #     print(k,v)
    favorable_reviews_by_users=dict((k,frozenset(v.values)) for k,v in favorable_ratings.groupby("userId")["movieId"] )
    # print(favorable_reviews_by_users)#用户：喜爱的电影集合
    num_favorable_by_movie = ratings[["movieId","favorable"]].groupby("movieId").sum()
    # print(num_favorable_by_movie)#每部电影的总得分  电影：总得分
    #print(num_favorable_by_movie.sort("favorable",ascending=False)[:5])#以总得分降序排列
    frequent_itemsets={}
    min_support=50
    # for movie_id,row in num_favorable_by_movie.iterrows():
    #     print(movie_id,row)
    frequent_itemsets[1]=dict( (frozenset((movie_id,)),row["favorable"]) for movie_id,row in num_favorable_by_movie.iterrows() if row["favorable"] > min_support  )
    # print(frequent_itemsets[1])

    for k in range(2,20):
        cur_frequent_itemsets = find_frequent_itemsets(favorable_reviews_by_users, frequent_itemsets[k-1],min_support)
        frequent_itemsets[k]=cur_frequent_itemsets
        if len(cur_frequent_itemsets)==0:
            print('did not find any frequent itemsets of length {0}'.format(k))
            sys.stdout.flush()
            break
        else:
            print('Found {0} frequent itemsets of length {1}'.format(len(cur_frequent_itemsets),k))
            sys.stdout.flush()
    del frequent_itemsets[1]
    print(frequent_itemsets)

    candidate_rules=[]
    for itemset_length,itemset_counts in frequent_itemsets.items():
        for itemset in itemset_counts.keys():
            for conclusion in itemset:
                premise = itemset - set((conclusion,))
                candidate_rules.append((premise,conclusion))
    print(candidate_rules)

    correct_counts = defaultdict(int)
    incorrect_counts = defaultdict(int)
    for user,reviews in favorable_reviews_by_users.items():
        for candidate_rule in candidate_rules:
            premise,conclusion=candidate_rule
            if premise.issubset(reviews):
                if conclusion in reviews:
                    correct_counts[candidate_rule] +=1
                else:
                    incorrect_counts[candidate_rule]+=1
    rule_confidence = {candidate_rule:correct_counts[candidate_rule]/float( correct_counts[candidate_rule]+incorrect_counts[candidate_rule] ) for candidate_rule in candidate_rules }

    sorted_confidence = sorted( rule_confidence.items(), key=itemgetter(1), reverse=True  )


    movie_name_data = loadMovieData()
    #print(movie_name_data[movie_name_data['movieId']=="1"]['title'].values[0])

    for index in range(5):
        print('Rule #{0}'.format(index+1))
        premise,conclusion = sorted_confidence[index][0]
        premise_names =', '.join([get_movie_name(idx,movie_name_data) for idx in premise])
        conclusion_name=get_movie_name(conclusion,movie_name_data)
        print('Rule: IF a person recommends {0}, THEN they will also recommend {1}'.format(premise_names,conclusion_name))
        print(' -- Confidence: {0:.3f}'.format(rule_confidence[(premise,conclusion)]))
        print("")
    

    test_dataset = all_ratings[~all_ratings['userId'].isin(range(200))]
    test_favorable = test_dataset[test_dataset['favorable']]
    test_favorable_by_users = dict( (k,frozenset(v.values,))  for k,v in test_favorable.groupby('userId')["movieId"] )
    test_correct_counts=defaultdict(int)
    test_incorrect_counts=defaultdict(int)
    for user,reviews in test_favorable_by_users.items():
        for candidate_rule in candidate_rules:
            premise,conclusion=candidate_rule
            if premise.issubset(reviews):
                if conclusion in reviews:
                    test_correct_counts[candidate_rule]+=1
                else:
                    test_incorrect_counts[candidate_rule]+=1
    test_rule_confidence ={ candidate_rule: test_correct_counts[candidate_rule]/float(test_correct_counts[candidate_rule]+test_incorrect_counts[candidate_rule])   for candidate_rule in candidate_rules }

    # test_sorted_confidence = sorted(test_rule_confidence.items(), key=itemgetter(1),reverse=True)
    for index in range(5):
        print('Rule #{0}'.format(index+1))
        premise,conclusion = sorted_confidence[index][0]
        premise_names= ', '.join([get_movie_name(idx,movie_name_data) for idx in premise])
        conclusion_name = get_movie_name(conclusion,movie_name_data)
        print('Rule: IF a person recommends {0}, THEN they will also recommend {1}'.format(premise_names,conclusion_name))
        print(' -- Train confidence:{0:.3f}'.format(rule_confidence[(premise,conclusion)]))
        print(' -- Test confidence:{0:.3f}'.format(test_rule_confidence[(premise,conclusion)]))



def loadMovieData():
    movie_name_data = pd.read_csv(os.path.join("D:\python\ml-20m\ml-20m","movies.csv"),names=["movieId",'title','genres'])
    return movie_name_data

def get_movie_name(movie_id,movie_name_data):
    title= movie_name_data[movie_name_data['movieId']==str(movie_id)]['title'].values[0]
    return title

def find_frequent_itemsets(favorable_reviews_by_users, k_1_itemsets, min_support):
    counts=defaultdict(int)

    for user,reviews in favorable_reviews_by_users.items():
        for itemset in k_1_itemsets:
            if itemset.issubset(reviews):
                for other_reviewed_movie in reviews-itemset:
                    current_superset=itemset | frozenset((other_reviewed_movie,))
                    counts[current_superset]+=1
    return dict( [ (itemset,frequency)  for itemset,frequency in counts.items() if frequency>=min_support ]  )

if __name__=="__main__":
    loadDataSet()