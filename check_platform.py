#-*-coding:utf-8-*-

###
# ver:     0.01
# date:    2017-08-17
# author:  Charles.Z
###

from __future__ import print_function
from __future__ import unicode_literals
from leancloud import Object
from leancloud import Query
from leancloud.errors import LeanCloudError
import leancloud
import time
import datetime
import hashlib
from random import Random
import sys

# leancloud.init("Fhdcn0x7iznoVTkg6kzthl6w-gzGzoHsz", "cTNJGjdsCK6snzqmNhTsumjp")

leancloud.init("Fhdcn0x7iznoVTkg6kzthl6w-gzGzoHsz", master_key="usMoq9bILw9Yp39lL2K89sjq")



class _File(Object):
    pass

class Todo(Object):
    pass

class _User(Object):
    pass

class Project(Object):
    pass

class ProjectDate(Object):
    pass

class StatDAU(Object):
    pass

class StatLog(Object):
    pass

class StatUser(Object):
    pass

class UserProjectMap(Object):
    pass

class StatInternalUser(Object):
    pass    

stat_col = []

# proj_id = sys.argv[1]
# du_w = sys.argv[2]

ahour_for_st = datetime.timedelta(hours=-8)
date_from = (datetime.datetime.strptime(sys.argv[1]+" 00:00:00", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')
date_to = (datetime.datetime.strptime(sys.argv[2]+" 23:59:59", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')

cql_get_updateAt = "select objectId, requestObj ,updatedAt from StatLog where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') limit 99999999"
# cql_get_updateAt = "select objectId, loginObj, lastObj from StatUser where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') limit 99999999"
# print(cql_get_updateAt)    
# cql_get_updateAt = "select * from StatDAU where createdAt < date('2022-08-20T02:06:57.931Z')"
todo_query_updateAt = leancloud.Query.do_cloud_query(cql_get_updateAt)
todo_list_updateAt = todo_query_updateAt.results # 返回符合条件的 todo list 

i = 0
for each in todo_list_updateAt:
    platId = 8
    aid = "kkkkkkk"
    if 'platformVersionId' in each.get('requestObj')['headerRequest']:
        platId = each.get('requestObj')['headerRequest']['platformVersionId']
    if 'androidId' in each.get('requestObj')['headerRequest']:
        aid = each.get('requestObj')['headerRequest']['androidId']
   
    if platId == 23:
        # i=i+1
        # print(i)
        cql_get_verify = "select objectId, requestObj from StatUser where androidId = '"+aid+"'  and projectId='ota_002'"
        todo_query_verify = leancloud.Query.do_cloud_query(cql_get_verify)
        todo_list_verify = todo_query_verify.results # 返回符合条件的 todo list      
        if todo_list_verify != []:
            dic = {}
            dic['req_obj'] = each.get('requestObj')['headerRequest']
            dic['time'] = each.get('updatedAt').strftime('%Y-%m-%d %H:%M:%S')
            # print(each.get('requestObj')['headerRequest']['platformVersionId'])
            # print(todo_list_verify[0].get('objectId'))
            # print(aid)
            stat_col.append(dic)


# cql_get_updateAt = "select objectId, projectId, loginObj, lastObj from StatUser where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') and projectId = 'ota_002' limit 99999999"
# # print(cql_get_updateAt)    
# # cql_get_updateAt = "select * from StatDAU where createdAt < date('2022-08-20T02:06:57.931Z')"
# todo_query_updateAt = leancloud.Query.do_cloud_query(cql_get_updateAt)
# todo_list_updateAt = todo_query_updateAt.results # 返回符合条件的 todo list 

# i = 0
# for each in todo_list_updateAt:
#     print(each.get('loginObj')['action'])
#     # if each.get('lastObj') != None:
#         # print(each.get('lastObj')['action'])
#     if each.get('loginObj')['action'] != 'STAT_LOGIN' or (each.get('lastObj') != None and each.get('lastObj')['action'] != 'STAT_LOGIN'):

#         # print(each.get('lastObj')['action'])
#         i=i+1
#         print(i)
        
#         stat_col.append(each.get('objectId'))

print(stat_col)

