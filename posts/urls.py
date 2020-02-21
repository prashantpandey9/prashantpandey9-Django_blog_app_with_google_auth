from django.contrib import admin
from django.urls import path,include
from posts.views import post_list,post_detail,post_create
urlpatterns = [
    path('',post_list),
    path('create/',post_create),
    path('<slug:slug>/',post_detail),
    
    #url(r'^P<slug:slug>[\w-]+/',post_detail),

]
