from django.shortcuts import render

# Create your views here.
# CRUD-L
# Create Read Update Delete List
# 함수형 뷰 : 문법적 형식이 함수 - 제네릭뷰가 없거나 내가 기능 하나 하나를 커스터마이징 하고 싶을 때
# 클래스형 뷰 : 문법적 형식이 클래스 - 웹서비스 영역에서 빈번하게 만드는 기능은 제네릭 뷰

from django.views.generic.list import ListView

#제네릭 뷰 -> 모델 베이스 뷰
from .models import BMI

class BMIList(ListView):
    model = BMI

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import *

class BMIDetail(DetailView):
    model = BMI

class BMICreate(CreateView):
    model = BMI
    fields = ['weight', 'height']
    success_url = "/"

class BMIUpdate(UpdateView):
    model = BMI
    fields = ['weight', 'height']
    success_url = "/"

class BMIDelete(DeleteView):
    model = BMI
    success_url = "/"