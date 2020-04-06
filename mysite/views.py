from django.shortcuts import render

def top(request):
    return render(request, 'mysite/top.html')
    

def aboutme(request):
    return render(request, 'mysite/aboutme.html')