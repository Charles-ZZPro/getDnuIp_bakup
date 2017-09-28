#-*-coding:utf-8-*-

###
# ver:     1.0
# date:    2017-09-13
# author:  Charles.Z
# change log:
#     fix bugs;
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

printhelp = ""
printhelp = "========= 欢迎您使用device model查询命令 =========\r\n"
printhelp = printhelp + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r\n"
printhelp = printhelp + "                   _ooOoo_\r\n"
printhelp = printhelp + "                  o8888888o\r\n"
printhelp = printhelp + '                  88" . "88\r\n'
printhelp = printhelp + "                  (| -_- |)\r\n"
printhelp = printhelp + "                  O\  =  /O\r\n"
printhelp = printhelp + "               ____/`---'\____\r\n"
printhelp = printhelp + "              '  \\\|     |//  `.\r\n"
printhelp = printhelp + "            /  \\\|||  :  |||//  \\\n"
printhelp = printhelp + "           /  _||||| -:- |||||-  \\\n"
printhelp = printhelp + "           |   | \\\\  -  /// |   |\r\n"
printhelp = printhelp + "           | \_|  ''\---/''  |   |\r\n"
printhelp = printhelp + "           \  .-\__  `-`  ___/-. /\r\n"
printhelp = printhelp + "         ___`. .'  /--.--\  `. . __\r\n"
printhelp = printhelp + "      .'' '<  `.___\_<|>_/___.'  >'''.\r\n"
printhelp = printhelp + "     | | :  `- \`.;`\ _ /`;.`/ - ` : | |\r\n"
printhelp = printhelp + "     \  \ `-.   \_ __\ /__ _/   .-` /  /\r\n"
printhelp = printhelp + "======`-.____`-.___\_____/___.-`____.-'======\r\n"
printhelp = printhelp + "                   `=---='\r\n"
printhelp = printhelp + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r\n"
printhelp = printhelp + "====== 介首锅作为约定,今后路我们一起走 ======\r\n"

if sys.argv[1] == 'help':
    printhelp = printhelp + "\r\n"
    printhelp = printhelp + "Arguments Instruction :::\r\n"
    printhelp = printhelp + "argument 1 : project ID\r\n"
    printhelp = printhelp + "argument 2 : apk ver\r\n"
    printhelp = printhelp + "argument 3 : start date\r\n"
    printhelp = printhelp + "argument 4 : end date\r\n"
    print(printhelp)
    sys.exit(0)

print(printhelp)
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

proj_id = sys.argv[1]
apk_ver = sys.argv[2]
# du_w = sys.argv[2]

ahour_for_st = datetime.timedelta(hours=-8)
date_from = (datetime.datetime.strptime(sys.argv[3]+" 00:00:00", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')
date_to = (datetime.datetime.strptime(sys.argv[4]+" 23:59:59", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')

cql_get_updateAt = "select objectId, createdAt, requestObj from StatLog where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') limit 99999999"
# print(cql_get_updateAt)    
# cql_get_updateAt = "select * from StatDAU where createdAt < date('2022-08-20T02:06:57.931Z')"
todo_query_updateAt = leancloud.Query.do_cloud_query(cql_get_updateAt)
todo_list_updateAt = todo_query_updateAt.results # 返回符合条件的 todo list 

res_col = []
model_col = []
for each_log in todo_list_updateAt:
    requestObj = each_log.get('requestObj')
    pid = requestObj['headerRequest']['projectId']
    if requestObj.has_key('apkVer'):
        aver = requestObj['apkVer']
    else:
        aver = 'nonenone'
    model = requestObj['headerRequest']['deviceModel']
    if pid != proj_id or aver != apk_ver:
        continue

    if model in model_col:
        # print(model_col.index(model)
        res_col[model_col.index(model)]['cnt'] += 1
    else:
        dic_new = {}
        dic_new['model'] = model
        dic_new['cnt'] = 1
        model_col.append(dic_new['model'])
        res_col.append(dic_new)

print('-------------------------')
for each_res in res_col:
    print(each_res['model'].ljust(18) + str(each_res['cnt']).rjust(7))
    print('-------------------------')
# print(res_col)
    
