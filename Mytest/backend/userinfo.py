from django.contrib.auth import authenticate
from web01 import models

import time

class UserInfo(object):
    """堡垒机交互脚本"""
    def __init__(self,username):
        # self.argv_handler_interance = argv_handler_interance
        self.username = username

    def auth(self):
        """认证程序"""
        count = 0
        while count < 1:
            username = input("堡垒机账号：").strip()
            password = input("Password：").strip()
            # user = 'user'
            # password = '123456'
            user = authenticate(username=username,password=password)
            if user:
                self.user = user
                return True
            else:
                count += 1

    def host_list(self,username):
        user_nid = models.UserInfo.objects.get(username='user').nid
        host_list = models.Host.objects.filter(user_id=user_nid)
        # print(len(host_list))
        while True:
            host_dict = {}
            n = 1
            for host in host_list:
                print('序号%s 主机组 %s,主机IP%s'%(n,host.Host_group,host.in_ip))
                host_dict[n]=host
                n = n+1
            number = input("堡垒机序号：").strip()
            number = int(number)
            print(host_dict[number].in_ip,host_dict[number].port,host_dict[number].user,host_dict[number].password,self.user)
            hostinfo={}
            hostinfo['ip'] = host_dict[number].in_ip
            hostinfo['port'] = host_dict[number].port
            hostinfo['username'] = host_dict[number].host_user
            hostinfo['password'] = host_dict[number].password
            hostinfo['user']=self.user
            return hostinfo


    def interactive(self):
        """启动交互脚本"""
        if self.auth():
            print("堡垒机登录成功")
            hostinfo = self.host_list(self.username)
            return hostinfo



