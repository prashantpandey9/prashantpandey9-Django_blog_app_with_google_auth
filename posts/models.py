from django.db import models

from django.conf import settings

User=settings.AUTH_USER_MODEL
class Post(models.Model):
	title=models.CharField(max_length=120)
	discription=models.TextField()
	author=models.ForeignKey("Author",on_delete=models.CASCADE)
	image=models.ImageField()
	slug=models.SlugField()
	def __str__(self):
		return self.title
		
class Author(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	email=models.EmailField()
	cell_no=models.IntegerField()#for adding a country code we use "+91" after round bracket
	def __str__(self):
		return self.user.username