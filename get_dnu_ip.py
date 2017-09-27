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
printhelp = "========= 欢迎您使用user ip查询命令 =========\r\n"
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
    printhelp = printhelp + "argument 2 : user type (DAU/DNU)\r\n"
    printhelp = printhelp + "argument 3 : start date\r\n"
    printhelp = printhelp + "argument 4 : end date\r\n"
    printhelp = printhelp + "argument 5 : DAU type (true/false/total. Needed when arg2 is DAU, true for default)"
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
du_w = sys.argv[2]

ahour_for_st = datetime.timedelta(hours=-8)
date_from = (datetime.datetime.strptime(sys.argv[3]+" 00:00:00", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')
date_to = (datetime.datetime.strptime(sys.argv[4]+" 23:59:59", "%Y-%m-%d %H:%M:%S")+ahour_for_st).strftime('%Y-%m-%dT%H:%M:%S.000Z')
# print(date_from)
# print(date_to)
# date_from = sys.argv[3]+"T00:00:00.000Z"
# date_to = sys.argv[4]+"T23:59:59.999Z"
ip_col_final = []
ip_col_dnu = []
user_id_col = []
ip_col = []
ip_all_col = []
exp_ip_col = []
aid_col = []

cql_get_exp_ip = "select objectId, androidId from StatInternalUser limit 99999999"
todo_query_exp_ip = leancloud.Query.do_cloud_query(cql_get_exp_ip)
todo_list_exp_ip = todo_query_exp_ip.results # 返回符合条件的 todo list 
if todo_list_exp_ip != []:
    for each_exp_ip in todo_list_exp_ip:
        exp_ip_col.append(each_exp_ip.get('androidId'))

if du_w == "DAU":
    if len(sys.argv) == 6 and sys.argv[5] == "total":
        cql_get_updateAt = "select objectId, updatedAt, userId from StatDAU where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') and projectId = '"+proj_id+"' limit 99999999"
    elif len(sys.argv) == 6 and sys.argv[5] == "false":
        cql_get_updateAt = "select objectId, updatedAt, userId from StatDAU where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') and projectId = '"+proj_id+"'  and verified = false limit 99999999"
    else:
        cql_get_updateAt = "select objectId, updatedAt, userId from StatDAU where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') and projectId = '"+proj_id+"'  and verified = true limit 99999999"
    # print(cql_get_updateAt)    
    # cql_get_updateAt = "select * from StatDAU where createdAt < date('2022-08-20T02:06:57.931Z')"
    todo_query_updateAt = leancloud.Query.do_cloud_query(cql_get_updateAt)
    todo_list_updateAt = todo_query_updateAt.results # 返回符合条件的 todo list 
    # print(todo_list_updateAt)
    # if [1] != []:
    if todo_list_updateAt == [] and du_w == "DAU":
        # print("Sorry")
        # exit(0)
        ip_all_col = []
    else:
        if len(sys.argv) == 6 and sys.argv[5] == "total" and 1!=1:
            cql_get_ip = "select objectId, requestIP, requestObj ,updatedAt from StatLog where updatedAt >= date('"+date_from+"') and updatedAt <= date('"+date_to+"') limit 99999999"
            # todo_query_get_ip = leancloud.Query.do_cloud_query(cql_get_ip)
            # todo_list_get_ip = todo_query_get_ip.results # 返回符合条件的 todo list
        else :
            cql_get_ip = "select objectId, requestIP, requestObj ,updatedAt  from StatLog where  "
            # j = 0
            for each in todo_list_updateAt:
                # j=j+1
                # if j>100:
                #     break
                # time_col = ()
                if each.get('userId') not in user_id_col:
                    user_id_col.append(each.get('userId'))
                # aHour = datetime.timedelta(hours=8)
                time_now = (each.get('updatedAt')).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                aSec = datetime.timedelta(seconds=2)
                dSec = datetime.timedelta(seconds=-2)
                # aSec_1 = datetime.timedelta(seconds=1)
                # dSec_1 = datetime.timedelta(seconds=-1)                
                time_utc_to = (each.get('updatedAt')+aSec).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                time_utc_from = (each.get('updatedAt')+dSec).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                # time_utc_to_1 = (each.get('updatedAt')+aSec_1).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                # time_utc_from_1 = (each.get('updatedAt')+dSec_1).strftime('%Y-%m-%dT%H:%M:%S.000Z')   
                # time_col.append(time_now) 
                # time_col.append(time_utc_to) 
                # time_col.append(time_utc_from) 
                # time_col.append(time_utc_to_1) 
                # time_col.append(time_utc_from_1) 
                # cql_get_ip = cql_get_ip + time_now + ","+time_utc_to+ "," + time_utc_from+ "," + time_utc_to_1+ "," + time_utc_from_1+ ","
                # cql_get_ip = cql_get_ip + "date('"+time_now + "'),date('"+time_utc_to+ "'),date('" + time_utc_from+ "'),date('" + time_utc_to_1+ "'),date('" + time_utc_from_1+ "'),"

                cql_get_ip = cql_get_ip + " (updatedAt >= date('" + time_utc_from + "') and updatedAt <= date('" + time_utc_to +"')) or "
            cql_get_ip = cql_get_ip + "updatedAt = date('2087-08-01T00:00:00.000Z') limit 99999999"            
            # cql_get_ip = cql_get_ip[:-1] + ") limit 99999999"
        # print(cql_get_ip)
        
        try:
            todo_query_get_ip = leancloud.Query.do_cloud_query(cql_get_ip)
            todo_list_get_ip = todo_query_get_ip.results # 返回符合条件的 todo list 
        except Exception, e:  
            print('Sql too long !!! :::')
            print(cql_get_ip)
            sys.exit(1)
        # print(todo_list_get_ip)
        i = 0
        for each in todo_list_get_ip:
            i= i+1
            if each.get('requestObj')['headerRequest']['projectId'] != proj_id:
                continue       
            # imei = each.get('requestObj')['headerRequest']['imei']
            # print(each.get('requestObj')['headerRequest'])
            if 'androidId' in each.get('requestObj')['headerRequest']:
                aid = each.get('requestObj')['headerRequest']['androidId']
            else:
                aid = ""
            ip_g = each.get('requestIP')
            # if ip_g not in ip_col:
            if ip_g == None:
                ip_g = "None"
            ip_col.append(ip_g)
            dic = {}
            # dic['imei'] = imei
            # if dic['imei'] == "UNKNOWN_IMEI":
            #     dic['imei'] = "UNKNOWN_IMEI   "        
            dic['aid'] = aid
            if dic['aid'] in aid_col:
                continue
            else:
                aid_col.append(dic['aid'])
                dic['ip'] = ip_g
                aHour = datetime.timedelta(hours=8)
                dic['time'] = (each.get('updatedAt')+aHour).strftime('%Y-%m-%d %H:%M:%S')
                ip_all_col.append(dic)

    # ip_col_final = ip_all_col

if du_w == "DNU":
    # for each_ip in ip_col:
    #     cql_get_ip_dnu = "select objectId from StatLog where requestIP = ? and updateAt < ?"
    #     todo_query_get_ip_dnu = leancloud.Query.do_cloud_query(cql_get_ip_dnu, each_ip, date_from)
    #     todo_list_get_ip_dnu = todo_query_get_ip_dnu.results # 返回符合条件的 todo list 
    #     if todo_list_get_ip_dnu == []:
    #         ip_col_dnu.append(each_ip)
    cql_get_ip_dnu = "select objectId ,imei, androidId ,createdAt ,updatedAt from StatUser where createdAt >= date('"+date_from+"') and createdAt <= date('"+date_to+"') and projectId = '"+proj_id+"' limit 99999999"
    todo_query_get_ip_dnu = leancloud.Query.do_cloud_query(cql_get_ip_dnu, date_from, date_to)
    todo_list_get_ip_dnu = todo_query_get_ip_dnu.results # 返回符合条件的 todo list 
    
    i = 0
    for each_dnu in todo_list_get_ip_dnu:
        i=i+1
        # print(i)
        aid_dnu = each_dnu.get('androidId')
        # imei_dnu = each_dnu.get('imei')
        dic_c = {}
        # dic_c['imei'] = imei_dnu
        # if dic_c['imei'] == "UNKNOWN_IMEI":
        #     dic_c['imei'] = "UNKNOWN_IMEI   "
        dic_c['aid'] = aid_dnu
        dic_c['ip'] = "::ffff:888.88.88.888"
        aHour = datetime.timedelta(hours=8)
        dic_c['time'] = (each_dnu.get('createdAt')+aHour).strftime('%Y-%m-%d %H:%M:%S')

        # for each_all_ip in ip_all_col:
        #     if aid_dnu == each_all_ip['aid']:
        #             dic_c['ip'] = each_all_ip['ip']

        if dic_c['ip'] == "::ffff:888.88.88.888":
            cql_get_ip_dnu_888 = "select objectId, requestIP  ,requestObj from StatLog where  "
            aSec_888 = datetime.timedelta(seconds=2)
            dSec_888 = datetime.timedelta(seconds=-2)
            time_utc_to_888 = (each_dnu.get('createdAt')+aSec_888).strftime('%Y-%m-%dT%H:%M:%S.000Z')
            time_utc_from_888 = (each_dnu.get('createdAt')+dSec_888).strftime('%Y-%m-%dT%H:%M:%S.000Z')
            cql_get_ip_dnu_888 = cql_get_ip_dnu_888 + " (createdAt >= date('" + time_utc_from_888 + "') and createdAt <= date('" + time_utc_to_888 +"')) limit 99999999"
            # print(cql_get_ip_dnu_888)
            todo_query_get_ip_dnu_888 = leancloud.Query.do_cloud_query(cql_get_ip_dnu_888)
            todo_list_get_ip_dnu_888 = todo_query_get_ip_dnu_888.results # 返回符合条件的 todo list         
            # if todo_list_get_ip_dnu_888 != [] and todo_list_get_ip_dnu_888[0].get('requestObj')['headerRequest']['projectId'] == proj_id:
            if todo_list_get_ip_dnu_888 != []:
                for each_getting_ip in todo_list_get_ip_dnu_888:
                    if each_getting_ip.get('requestObj')['headerRequest']['projectId'] != proj_id:
                        continue
                    else:                       
                        if todo_list_get_ip_dnu_888[0].get('requestIP') != None:
                            dic_c['ip'] = each_getting_ip.get('requestIP')
                        else:
                            dic_c['ip'] = "None"

        ### Duplicate removal
        cql_get_ip_dnu_checkaid = "select objectId from StatUser where createdAt < date('"+date_from+"') and androidId = '" + dic_c['aid'] +"'"
        todo_query_get_ip_dnu_checkaid = leancloud.Query.do_cloud_query(cql_get_ip_dnu_checkaid)
        todo_list_get_ip_dnu_checkaid = todo_query_get_ip_dnu_checkaid.results # 返回符合条件的 todo list         
        if todo_list_get_ip_dnu_checkaid != [] and dic_c['aid'] not in exp_ip_col:
            # dic = {}
            # dic['imei'] = imei
            # if dic['imei'] == "UNKNOWN_IMEI":
            #     dic['imei'] = "UNKNOWN_IMEI   "        
            # dic['aid'] = aid
            # dic['ip'] = ip_g
            # aHour = datetime.timedelta(hours=8)
            # dic['time'] = (each.get('updatedAt')+aHour).strftime('%Y-%m-%d %H:%M:%S')   
            ip_all_col.append(dic_c) 
            # print("ff")        
            continue
        ###
        ip_col_dnu.append(dic_c)

if du_w == "DAU":
    ip_col_final = ip_all_col
elif du_w == "DNU":
    ip_col_final = ip_col_dnu

if ip_col_final == []:
    print("No records for selected date range !!!")
else:
    # print("Request ip adresses : ")
    print("===========IP===========================AID===========================TIME===========")
    for each_ip_final in ip_col_final:
        ip_now = each_ip_final['ip'][7:]
        if each_ip_final['ip'][7:].count("|") != 0 :
            ip_now = each_ip_final['ip'][7:][:each_ip_final['ip'][7:].find("|")]
        # printls = "ip : "+each_ip_final['ip']+"     androidID : "+each_ip_final['aid']+"     imei : "+each_ip_final['imei']+"     time : "+each_ip_final['time']
        # print(each_ip_final['ip'][7:].ljust(30))
        # print(each_ip_final['aid'].ljust(16))
        # print(each_ip_final['time'])
        printls = "ip : "+ip_now.ljust(16)+"     androidID : "+each_ip_final['aid'].ljust(16)+"     time : "+each_ip_final['time'] + "\r\n-------------------------------------------------------------------------------------"
        print(printls)
