from django.db import models
import django.utils.timezone as timezone
# Create your models here.



from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    """堡垒机账号"""
    nid = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    def __str__(self):
        return self.username




class Host_group(models.Model):
    nid = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.group_name

class IDC(models.Model):
    nid = models.AutoField(primary_key=True)
    idc = models.CharField(max_length=32)
    def __str__(self):
        return self.idc

class Host(models.Model):
    """存储主机列表"""
    host_name = models.CharField(max_length=64)
    in_ip = models.GenericIPAddressField(unique=True)		# 内IP
    out_ip = models.GenericIPAddressField(null=False)		# 外IP
    port = models.SmallIntegerField(default=22)				# 端口
    host_user = models.CharField(max_length=32)				# 主机用户
    password = models.CharField(max_length=32)	            # 密码
    idc = models.ForeignKey("IDC")							# 机房
    Host_group = models.ForeignKey("Host_group")	        # 主机组
    user = models.ForeignKey("UserInfo",null=True)        # 主机分配的堡垒机账户
    def __str__(self):
        return self.host_name	                            # 返回主机名

class CommandIog(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey("UserInfo")
    host = models.ForeignKey("Host")
    command = models.CharField(max_length=128)
    date = models.DateTimeField('保存日期',default = timezone.now)


# nid = models.AutoField(primary_key=True)
# user = models.ForeignKey("UserInfo")
# host = models.ForeignKey("Host")
# command = models.CharField(max_length=128)
# date = models.DateTimeField('保存日期',default = timezone.now)




