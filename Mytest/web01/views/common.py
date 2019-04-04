from django.shortcuts import render, redirect,HttpResponse
from django.contrib import auth
from  django.views import View
from django import forms
from django.forms import widgets
from web01 import models
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


class Login(View):
    def get(self,request):
        return render(request,'login2.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request,username=username,password=password)
        print(user)
        if user:
            print(user.username)
            auth.login(request,user)
            return redirect('/host/')
        else:
            return redirect('/login/')


from django.contrib.auth.decorators import login_required
@login_required
def logout(request):
    print('logout')
    auth.logout(request)
    return redirect('/login/')


class RegForms(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, label='用户名',
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),
                           error_messages={'max_length': '太长了', 'min_length': '太短了'}
                           )
    pwd = forms.CharField(max_length=20, min_length=2, label='密码',
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                          error_messages={'max_length': '太长了', 'min_length': '太短了'}
                          )
    re_pwd = forms.CharField(max_length=20, min_length=2, label='确认密码',
                             widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                             error_messages={'max_length': '太长了', 'min_length': '太短了'}
                             )
    email = forms.EmailField(label='邮箱',
                             widget=widgets.EmailInput(attrs={'class': 'form-control'}),
                             )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        user = models.UserInfo.objects.filter(username=name).first()
        if user:
            raise ValidationError('用户已经存在')
        else:
            return name

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            # __all__
            raise ValidationError('两次密码不一致')