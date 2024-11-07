"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from index import views as index_views
from pybo.views import base_views
from balance import views as balance_views
from django.conf.urls import url
from chartapp import views
# from modelpage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('main_index', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('index/', index_views.main_views),
    path('balance/', balance_views.main_view),
    path('samsung.share/',views.main_page),
    path('data.json/',views.data_json),
    path('data2.json/', views.data2_json),
    path('samsung.volume/', views.main_page2),
    path('data3.json/', views.data3_json),
    path('cos/', views.main_page3),
    path('', include('nameapp.urls', namespace='nameapp')),
    path('index_main', index_views.main_tests),
    path('menu_test', index_views.menu_views),
    # path('modelpage', modelpage.runmodel),
]
