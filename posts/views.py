from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostModelForm

# Create your views here.
from .models import Post,Author
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

def posts_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        cell_no=894382982)
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect('/posts/')

    context = {
        'form': form
    }
    return render(request, "posts/posts_create.html", context)

def posts_update(request,slug):
	unique_post=get_object_or_404(Post,slug=slug)
	form = PostModelForm(request.POST or None, 
						 request.FILES or None,
						 instance=unique_post)
	if form.is_valid():
		form.save()
		return redirect('/posts/')
	context={
		"form":form
	}
	return render(request,"posts/posts_update.html",context)

def posts_delete(request,slug):
	unique_post=get_object_or_404(Post,slug=slug)
	unique_post.delete()
	return redirect('/posts/')