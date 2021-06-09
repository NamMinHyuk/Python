# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
test = client.test
score = test.score

res01 = score.delete_one({'name':'???'})
print(res01.deleted_count)

# test field가 존재하는 모든 document를 삭제하자.
res02 = score.delete_many({'test':{'$exists':True}})
print(res02.deleted_count)

# 모든 document들을 삭제하자.
score.delete_many({})