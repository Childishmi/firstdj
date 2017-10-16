"""djcode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from djcode import view
#from djcode.view import hello,current_datetime,hours_ahead      #顶部导入current_datetime函数
from books import views
#from books.views import * #search_form,search
#from contact.views2 import * #contact
from contact import views2


admin.autodiscover()
urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url('^hello/$', view.hello),
    url('^time/$',view.current_datetime),     #添加URL模式来映射URL中的/time/和新视图
    url(r'^time/plus/(\d{1,2})/$',view.hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    #url(r'^contact/$',contact),
    url(r'^contact/thanks/$',views2.thank),
    url(r'^contact_form/$',views2.contact),
]










#URLpattern，它是一个Python的元组
#元组中第一个元素是模式匹配字符串（正则表达式）；第二个元素是那个模式将使用的视图函数
#告诉 Django，所有指向 URL /hello/ 的请求都应由 hello 这个视图函数来处理