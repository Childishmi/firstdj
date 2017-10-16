from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render_to_response

"""
def hello(request):     #定义视图函数
    return HttpResponse("Hello world")

    # 每个视图函数至少要有一个参数，通常被叫作request
    #这是一个触发这个视图、包含当前Web请求信息的对象，是类django.http.HttpRequest的一个实例
    #虽然不用request做任何事情，然而它仍必须是这个视图的第一个参数。
    #一个视图就是Python的一个函数。这个函数第一个参数的类型是HttpRequest；它返回一个HttpResponse实例。
    # 为了使一个Python的函数成为一个Django可识别的视图，它必须满足这两个条件。
"""

def hello(request):
    return render_to_response('hello_world.html',{'my_name':'childishmi'})


"""
def current_datetime(request):
    now=datetime.datetime.now()
    t=get_template('current_datetime.html')     #选择模板文件
    html=t.render(Context({'current_date':now}))
    #html="<html><body>It is now %s.</body></html>" %now        #不要对模板路径硬编码
    return HttpResponse(html)
"""

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
#模板加载、上下文创建、模板解析和 HttpResponse 创建工作均在对 render_to_response() 的调用中完成了
#第一个参数必须是要使用的模板名称。 如果要给定第二个参数，那么该参数必须是为该模板创建 Context 时所使用的字典

"""
def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hour(s),it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)
"""
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset,'next_time':dt})
