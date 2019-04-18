from django.urls import path
from .views import *
urlpatterns = [
    #클래스형 함수
    path("detail/<int:pk>/",BMIDetail.as_view(), name='detail'),
    path("update/<int:pk>/",BMIUpdate.as_view(), name='update'),
    path("delete/<int:pk>/",BMIDelete.as_view(), name='delete'),
    path("create/",BMICreate.as_view(), name='create'),

    path("",BMIList.as_view(),name='index'),
]