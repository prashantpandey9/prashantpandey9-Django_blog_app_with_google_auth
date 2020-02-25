from django.contrib import admin
from django.urls import path,include
from posts.views import *
urlpatterns = [
    path('',post_list),
    path('create/',posts_create),
    path('<slug:slug>/update',posts_update),
    path('<slug:slug>/delete',posts_delete),
    path('<slug:slug>/',post_detail),
    #url(r'^P<slug:slug>[\w-]+/',post_detail),

]
