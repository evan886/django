from django.shortcuts import render
# -*- coding: utf-8 -*-
from django_web.models import Event, Guest
from django.http import JsonResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
import json
from django.core import serializers
import time


# JsonResponse 默认传入参数是字典格式，如果不是，则报错。


# 添加发布会接口
def add_event(request):
    # POST请求
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')
    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        # ensure_ascii 禁用ascii码
        return JsonResponse({'status': 10021, 'message': '参数错误'}, json_dumps_params={'ensure_ascii': False})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': '发布会id已存在'}, json_dumps_params={'ensure_ascii': False})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': '发布会名称已存在'}, json_dumps_params={'ensure_ascii': False})

    if status == '':
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit, status=int(status), address=address, start_time=start_time)
    except ValidationError:
        error = '开始日期格式错误，必须是:YYYY-MM-DD HH:MM:SS'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': '添加成功'})


# 发布会查询接口
def get_event_list(request):
    # GET请求
    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')
    if eid == '' and name == '':
        return JsonResponse({'status': 10021, 'message': '参数错误'})
    if eid != '':
        event = {}
        # 方法一：
        # filter返回由对象组成的列表，特点：返回对象列表不存在，不报错，[].

        # if result.exists():
        #     print("查询的发布会id是:%s"%result[0].id)
        #     print(type(result))
        #     # 序列化对象，转成类型字符串
        #     datas = serializers.serialize('json',result)
        #     # 字符串转成字典，就没有'\'
        #     new_datas = json.loads(datas)
        #     return JsonResponse({'status': 10022, 'message':new_datas})
        # else:
        #     return JsonResponse({'status':10023,'message':'查询对象结果为空'})

        # 方法二：
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10023, 'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
        return JsonResponse({'status': 200, 'message': '查询成功', 'data': event})

    if name != '':
        datas = []
        # 模糊查询：name__contains
        results = Event.objects.filter(name__contains=name)
        print(results.first())
        if results:
            for i in results:
                event = {}
                # 给字典添加键值对
                event['name'] = i.name
                event['limit'] = i.limit
                event['status'] = i.status
                event['address'] = i.address
                event['start_time'] = i.start_time
                datas.append(event)
            return JsonResponse({'status': 200, 'message': '查询成功', 'datas': datas})
        else:
            return JsonResponse({'status': 10022, 'message': '查询的数据不存在'})


# 添加嘉宾接口

def add_guest(request):
    # POST请求
    eid = request.POST.get('eid', '')
    realname = request.POST.get('realname', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')

    if eid == '' or realname == '' or phone == '' or email == '':
        return JsonResponse({'status': 10021, 'message': '参数错误'}, json_dumps_params={'ensure_ascii': False})

    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': '发布会id不存在'})

    # 判断发布会状态是否有效
    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status': 10023, 'message': '发布会状态无效'})

    # object.get只返回一条数据，发布会只有一个，filter返回对象查询集，一个发布会下有多个嘉宾
    event_limit = Event.objects.get(id=eid).limit  # 发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)  # 发布会已添加的嘉宾数

    print(len(guest_limit))
    print(event_limit)
    if len(guest_limit) >= event_limit:
        return JsonResponse({'status': 10024, 'message': '发布会人数已满'})

    event_time = Event.objects.get(id=eid).start_time
    # 日期字符串转换成日期对象
    timeArray = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")

    # 返回以秒的日期，入参struct_time。
    e_time = int(time.mktime(timeArray))
    # 获取当前时间(单位:秒)
    n_time = int(time.time())
    print(e_time)
    print(n_time)
    if n_time >= e_time:
        return JsonResponse({'status': 10025, 'message': '发布会已经开始了'})

    try:
        Guest.objects.create(event_id=int(eid), phone=int(phone), sign=0, realname=realname, email=email)
    except IntegrityError:
        return JsonResponse({'status': 10026, 'message': '手机号码重复'})
    result2 = Event.objects.filter(id=eid)
    new_result = serializers.serialize('json', result2)
    print(result2)
    return JsonResponse({'status': 200, 'message': '成功添加嘉宾', 'datas': json.loads(new_result)})


# 查询嘉宾接口
def get_guest_list(request):
    # GET请求
    eid = request.GET.get('eid', '')  # 关联发布会id
    phone = request.GET.get('phone', '')

    if eid == '':
        return JsonResponse({'status': 10021, 'message': '发布会id不能为空'})
    # 输入发布会id查询,查询发布会下所有嘉宾
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for i in results:
                guest_list = {}
                guest_list['realname'] = i.realname
                guest_list['phone'] = i.phone
                guest_list['email'] = i.email
                guest_list['sign'] = i.sign
                datas.append(guest_list)
            return JsonResponse({'status': 200, 'message': '查询成功', 'datas': datas})
        else:
            return JsonResponse({'status': 10022, 'message': '查询的数据不存在'})
    # 查询发布会下某个嘉宾
    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(event_id=eid, phone=phone)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10023, 'message': '查询的结果为空'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['sign'] = result.sign
            guest['email'] = result.email
            return JsonResponse({'status': 200, 'message': '查询成功', 'datas': guest})


# 嘉宾签到接口
def user_sign(request):
    # POST接口
    eid = request.POST.get('eid', '')
    phone = request.POST.get('phone', '')
    if eid == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': '参数错误'})

    try:
        result = Event.objects.get(id=eid)
    except Event.DoesNotExist:
        return JsonResponse({'status': 10022, 'message': '发布会id不存在'})
    if result.status is False:
        return JsonResponse({'status': 10023, 'message': '发布会未开启'})

    # 发布会时间
    event_time = result.start_time
    timeArray = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    # 当前时间
    n_time = int(time.time())

    if n_time >= e_time:
        return JsonResponse({'status': 10024, 'message': '发布会时间已过'})

    # 存在发布会后，再校验手机号码：
    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status': 10025, 'message': '手机号码不存在'})
    else:
        for i in result:
            if i.event_id == int(eid):
                break
        else:
            return JsonResponse({'status': 10026, 'message': '嘉宾不属于该发布会'})

    result = Guest.objects.get(event_id=eid, phone=phone)
    if result.sign is True:
        return JsonResponse({'status': 10027, 'message': '嘉宾已签到'})
    else:
        result.sign = True
        result.save()
        return JsonResponse({'status': 200, 'message': '签到成功'})

# Create your views here.
