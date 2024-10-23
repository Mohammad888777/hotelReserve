from django.shortcuts import render,redirect,get_object_or_404
from django.views import View


def home(request):

    print(request.resolver_match.url_name)

    context={
        ''
    }
    
    return render(request,"main/home.html")
