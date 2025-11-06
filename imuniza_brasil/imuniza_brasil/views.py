from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'page': 'home'})

def calendario(request):
    return render(request, 'index.html', {'page': 'calendario'})

def fake_news(request):
    return render(request, 'index.html', {'page': 'fake_news'})
