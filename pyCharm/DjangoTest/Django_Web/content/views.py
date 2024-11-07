from django.shortcuts import render
from django.utils.decorators import method_decorator

from account.decorators import login_required_content


# Create your views here.
@login_required_content
def content(request, *args, **kwargs):
    return render(request, 'content.html')