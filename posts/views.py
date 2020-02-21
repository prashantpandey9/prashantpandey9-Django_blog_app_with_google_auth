from django.shortcuts import render,get_object_or_404
from .forms import *
	
# Create your views here.
from .models import Post
def post_list(request):
	post_list=Post.objects.all()
	context={
		"post_list":post_list
	}
	return render(request,"posts/post_list.html",context)

def post_detail(request,slug):
	unique_post=get_object_or_404(Post,slug=slug)
	context={
		"posts":unique_post
	}
	return render(request,"posts/post_detail.html",context)

def post_create(request):
	author,created=Author.objects.get_or_create(
		user=request.user,
		email=request.user.email,
		cell_no=request.user.cell_no
		)
	form=PostModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		form.instance.author=author
		form.save()
		return redirect('/posts/')
	context={
		"form":form
	}
	return render(request,"posts/post_create.html",context)
