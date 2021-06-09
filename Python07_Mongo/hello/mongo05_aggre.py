# -*- coding:utf-8 -*-

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
test = client.test
score = test.score

# math 점수가 70보다 큰 document들의
# math 평균을 구해서, {'_id':'math', 'average': 평균}을 출력
aggre = score.aggregate(
        [
            {'$match':{'math':{'$gt':70}}},
            {'$group':{'_id':'math','average':{'$avg':'$math'}}}
        ]
    )
print(aggre)
pprint(list(aggre)[0]) # list에 담아서 출력