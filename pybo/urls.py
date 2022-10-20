"""
    app_name : templates에서 url을 지칭하기 위해서 사용, redirect 함수에서도 사용 가능함
    path 함수안에 name은 templates에서 url 호출 시 사용
"""
from django.urls import path, include

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
