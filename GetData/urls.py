from django.urls import path
from . import views
from django.shortcuts import render 
from django.conf import settings
from django.conf.urls.static import static

app_name ='GetData'

urlpatterns = [
    path('time',views.timekunal),
    path('rolltime',views.timeroll),
    path('Game/',views.render_game),
     #http://127.0.0.1:8000/GetDataPage/test
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
