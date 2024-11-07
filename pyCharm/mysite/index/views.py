from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def main_view(request):
    return render(request, 'index.html') # render()에 템플릿으로 사용할 파일명(index.html)만 넘겨주는 역할
