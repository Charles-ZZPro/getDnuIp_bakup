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

ahour_for_st = datetime.timedelta(hours=-8)
ahour_for_oneday = datetime.timedelta(hours=24)

date_from = (datetime.datetime.strptime("2017-09-13"+" 00:00:00", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')
date_to = (datetime.datetime.strptime("2017-09-13"+" 23:59:59", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.999Z')

cql_get_updateAt = "select objectId from StatUser where createdAt >= date('"+date_from+"') and createdAt <= date('"+date_to+"') and projectId='fanzhuo_S004' limit 99999999"
todo_query_updateAt = leancloud.Query.do_cloud_query(cql_get_updateAt)
todo_list_updateAt = todo_query_updateAt.results # 返回符合条件的 todo list 

date_start_day= datetime.datetime.strptime("2017-09-01"+" 00:00:00", "%Y-%m-%d %H:%M:%S")+ahour_for_st

cnt_all = 0
print(len(todo_list_updateAt))
for each_dnu in todo_list_updateAt:
    date_over_day = date_start_day+ahour_for_oneday
    dnu_id = each_dnu.get('objectId')
    # cql_get_updateAt = "select objectId as cnt_day from StatDAU where createdAt >= date('"+date_start_day.strftime('%Y-%m-%dT%H:%M:%S.000Z')+"') and createdAt < date('"+date_over_day.strftime('%Y-%m-%dT%H:%M:%S.000Z')+"')"
    cql_get_updateAt_fz = "select objectId from StatDAU where userId='"+dnu_id+"'"
    todo_query_updateAt_fz = leancloud.Query.do_cloud_query(cql_get_updateAt_fz)
    todo_list_updateAt_fz = todo_query_updateAt_fz.results # 返回符合条件的 todo list     
    # print(cql_get_updateAt_fz)
    # print(len(todo_list_updateAt_fz))
    # exit(0)

    if len(todo_list_updateAt_fz) >= 5:
        cnt_all+=1

print("cnt:    " + str(cnt_all))


