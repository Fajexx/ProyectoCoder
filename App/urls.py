from django.urls import path
from App import views
from App.views import create_relative, show_relatives

urlpatterns = [
    path('add/<str:name>/<int:age>/<str:birthday>/<str:relation_ship>/', create_relative),
    path('', show_relatives)
    ]
