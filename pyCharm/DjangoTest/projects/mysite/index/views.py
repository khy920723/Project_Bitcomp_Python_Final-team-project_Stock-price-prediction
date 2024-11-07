from django.shortcuts import render

def main_views(request):
    return render(request, 'index.html')

def main_tests(request):
    return render(request, 'maintest.html')

def menu_views(request):
    return render(request, 'menu.html')