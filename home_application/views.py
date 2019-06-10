# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from home_application.models import *


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')
def helloworld(request):
    return render(request, 'home_application/helloworld.html')

@csrf_exempt
def HelloBlueking(request):

    if request.POST and request.POST.get('inputid'):
        print(request.POST.get('inputid'))
        if request.POST.get('inputid')=='Hello Blueking':
            dis = 'Congratulation！'
        else:
            dis = '请输入正确的内容：'
        return JsonResponse({'data':dis})
    return render(request,'home_application/HelloBlueking.html')

@csrf_exempt
def addhost(request):
    if request.method=='GET':

        return render(request,'home_application/addhost.html')
    if request.method=='POST':
        try:
            addinfo = HostInfo(ip=request.POST.get('ip',None),
                     osname=request.POST.get('os',None),
                     prartition=request.POST.get('part',None),
                     )
            addinfo.save()
            msg = {"msg":"data is save"}
        except Exception as e:
            msg = {"msg": "error "+e[1]}
        return JsonResponse(msg)


def api_data(request):
    fieldlist = ['ip','osname','prartition']
    qs = HostInfo.objects.all()
    prelist = [[getattr(i,x) for x in fieldlist]  for i in qs]
    jsondata = {"data":prelist}
    return JsonResponse(jsondata)