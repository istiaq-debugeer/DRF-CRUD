from django.contrib import admin
from django.urls import path, include
from .views import PostList,PostDitails,student_info,Student_create

app_name='blog_Api'

urlpatterns = [

    path('<int:pk>/',PostDitails.as_view(),name='detailCreate' ),
    path('', PostList.as_view(), name='listcreate'),
    path('student/',student_info.as_view()),
    path('deserialize/',Student_create,name='createdeserialize')
]