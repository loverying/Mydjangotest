from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from web01 import models
from django.http import QueryDict
from  django.views import View

import json
# Create your views here.

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



@method_decorator(login_required, name='dispatch')
class Host_group(View):

    def get(self, request):
        host_group = models.Host_group.objects.all()
        return render(request, 'super/host_group.html', {"host_group": host_group})

    def post(self, request):
        response = {'status': True, 'message': None, 'data': None}
        try:
            u = request.POST.get('username')
            obj = models.Host_group.objects.create(
                    group_name=u
            )
            print(obj.nid)
            response['data'] = obj.nid
        except Exception as e:
            response['status'] = False
            response['message'] = '用户输入错误,可能主机组重复'
        result = json.dumps(response, ensure_ascii=False)
        return HttpResponse(result)

    def put(self, request):
        response = {'status': True, 'message': None, 'data': None}
        body = QueryDict(request.body)
        try:
            u = body.get('user')
            nid = body.get('nid')
            print(u, nid)
            obj = models.Host_group.objects.filter(nid=nid).update(
                    group_name=u
            )
            response['data'] = nid
        except Exception as e:
            response['status'] = False
            response['message'] = '用户输入错误,可能主机组重复'
        result = json.dumps(response, ensure_ascii=False)
        print(result)
        return HttpResponse(result)

    def delete(self, request):
        response = {'status': True, 'message': None, 'data': None}
        body = QueryDict(request.body)
        try:
            u = body.get('user')
            nid = body.get('nid')
            models.Host_group.objects.filter(nid=nid).delete()
            response['data'] = nid
        except Exception as e:
            response['status'] = False
            response['message'] = '删除错误'
        result = json.dumps(response, ensure_ascii=False)
        return HttpResponse(result)


@method_decorator(login_required, name='dispatch')
class Idc(View):
    def get(self, request):
        if request.user.is_staff:   # 判断权限
            host_group = models.IDC.objects.all()
            return render(request, 'super/idc.html', {"host_group": host_group})

    def post(self, request):
        response = {'status': True, 'message': None, 'data': None}
        try:
            u = request.POST.get('username')
            obj = models.IDC.objects.create(
                    idc=u
            )
            print(obj.nid)
            response['data'] = obj.nid
        except Exception as e:
            response['status'] = False
            response['message'] = '用户输入错误,可能主机组重复'
        result = json.dumps(response, ensure_ascii=False)
        return HttpResponse(result)

    def put(self, request):
        response = {'status': True, 'message': None, 'data': None}
        body = QueryDict(request.body)
        try:
            u = body.get('user')
            nid = body.get('nid')
            print(u, nid)
            obj = models.IDC.objects.filter(nid=nid).update(
                    idc=u
            )
            response['data'] = nid
        except Exception as e:
            response['status'] = False
            response['message'] = '用户输入错误,可能主机组重复'
        result = json.dumps(response, ensure_ascii=False)
        print(result)
        return HttpResponse(result)

    def delete(self, request):
        response = {'status': True, 'message': None, 'data': None}
        body = QueryDict(request.body)
        try:
            u = body.get('user')
            nid = body.get('nid')
            models.IDC.objects.filter(nid=nid).delete()
            response['data'] = nid
        except Exception as e:
            response['status'] = False
            response['message'] = '删除错误'
        result = json.dumps(response, ensure_ascii=False)
        return HttpResponse(result)


@method_decorator(login_required, name='dispatch')
class Host(View):
    def get(self, request):
        if request.user.is_staff:
            host_list = models.Host.objects.all()
            return render(request, 'super/host.html', {"host_list": host_list})
        else:
            user_nid = models.UserInfo.objects.get(username=request.user).nid
            host_list = models.Host.objects.filter(user_id=user_nid)
            return render(request, 'user/host.html', {"host_list": host_list})

    def delete(self, request):
        print('delete')
        response = {'status': True, 'message': None, 'data': None}
        body = QueryDict(request.body)
        try:
            nid = body.get('nid')
            print(nid)
            models.Host.objects.filter(id=nid).delete()
            response['data'] = nid
        except Exception as e:
            response['status'] = False
            response['message'] = '删除错误'
        result = json.dumps(response, ensure_ascii=False)
        return HttpResponse(result)


@method_decorator(login_required, name='dispatch')
class Add_host(View):
    def get(self, request):
        idc_list = models.IDC.objects.all()
        host_group_list = models.Host_group.objects.all()
        user_list = models.UserInfo.objects.all()
        return render(request, 'add_host.html', {"idc_list": idc_list,
                                                 "host_group_list": host_group_list,
                                                 "user_list":user_list})

    def post(self, request):
        host_name = request.POST.get('host_name')
        in_ip = request.POST.get('in_ip')
        out_ip = request.POST.get('out_ip')
        port = request.POST.get('port')
        host_user = request.POST.get('host_user')
        password = request.POST.get('password')
        idc = request.POST.get('idc')
        Host_group = request.POST.get('Host_group')
        user = request.POST.get('user')
        models.Host.objects.create(host_name=host_name,
                                   in_ip=in_ip,
                                   out_ip=out_ip,
                                   port=port,
                                   host_user=host_user,
                                   password=password,
                                   Host_group_id=Host_group,
                                   user_id=user,
                                   idc_id=idc)
        return redirect('/host/')


@method_decorator(login_required, name='dispatch')
class HostDetails(View):
    def get(self, request, id):
        details_host = models.Host.objects.filter(id=id).first()
        idc_list = models.IDC.objects.all()
        host_group_list = models.Host_group.objects.all()
        user_list = models.UserInfo.objects.all()
        return render(request, 'edit_host.html', locals())

    def post(self, request, id):
        host_name = request.POST.get('host_name')
        in_ip = request.POST.get('in_ip')
        out_ip = request.POST.get('out_ip')
        print(out_ip)
        port = request.POST.get('port')
        host_user = request.POST.get('host_user')
        password = request.POST.get('password')
        idc = request.POST.get('idc')
        Host_group = request.POST.get('Host_group')
        user = request.POST.get('user')
        models.Host.objects.filter(id=id).update(host_name=host_name, in_ip=in_ip, out_ip=out_ip, port=port,
                                                 host_user=host_user, password=password,
                                                 Host_group_id=Host_group,
                                                 idc_id=idc,
                                                 user_id=user
                                                 )
        print('dasb')
        return redirect('/host/')


class User(View):
    def get(self,request):
        user_list = models.UserInfo.objects.all()
        return render(request, 'user.html',{"user_list":user_list})

from web01.views.common import RegForms
def adduser(request):
    form_obj = RegForms()
    back_msg = {}
    if request.is_ajax():
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        form_obj = RegForms(request.POST)
        if form_obj.is_valid():
            user = models.UserInfo.objects.create_user(username=name, password=pwd, email=email)
            back_msg['user'] = name
            back_msg['msg'] = '注册成功'
        else:
            back_msg['msg'] = form_obj.errors
            # print(form_obj.errors)
            # print(type(form_obj.errors))
        return JsonResponse(back_msg)
    return render(request, 'adduser.html', {'form_obj': form_obj})


class Log(View):
    def get(self,request):
        log_list = models.CommandIog.objects.all()
        return render(request,'super/log.html',{"log_list":log_list})

    def delete(self,request):
        print('delete')
        response = {'status': True, 'message': None, 'data': None}
        body = QueryDict(request.body)
        try:
            nid = body.get('nid')
            print(nid)
            models.CommandIog.objects.filter(nid=nid).delete()
            response['data'] = nid
        except Exception as e:
            response['status'] = False
            response['message'] = '删除错误'
        result = json.dumps(response, ensure_ascii=False)
        return HttpResponse(result)


# def test(request):
#     host_list = models.Host.objects.all()
#     return render(request,'user/host.html', {"host_list": host_list})

