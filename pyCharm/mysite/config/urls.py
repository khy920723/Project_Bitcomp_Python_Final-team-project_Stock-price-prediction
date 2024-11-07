"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from pybo import views
from hello import views
from index import views as index_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),                    # 커스터마이징 된 pybo urlpattern
    re_path(r'^(?P<name>[A-Z][a-z]*)$', views.sayHello),    # 커스터마이징 된 hello urlpattern, re_path(): 정규표현식을 사용해 URL패턴 처리 가능
    path('index/', index_views.main_view),                  # 커스터마이징 된 index urlpattern, url이 index/이면 애플리케이션 뷰의 main_view()로 매핑
]
