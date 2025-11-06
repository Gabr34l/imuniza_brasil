from django.contrib import admin
from django.urls import path
from . import views   # importa views.py da pasta imuniza_brasil

urlpatterns = [
    path('admin/', admin.site.urls),

    # páginas informativas
    path('', views.index, name='index'),
    path('calendario/', views.calendario, name='calendario'),
    path('fake-news/', views.fake_news, name='fake_news'),
]
