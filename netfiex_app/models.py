from django.db import models
from django.contrib.auth.models import User



# this is categroy field and relation foreginkey 
class categoryModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return f"this is categroy - {self.name}"
    




LANGUAGE = [
    ("Bangla","Bangla"),
    ("English","English"),
    ("Handi","Handi"),
    
]

# this content model 
class contentModel(models.Model):
    category = models.ForeignKey(categoryModel,on_delete=models.CASCADE,null= True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    title = models.CharField(max_length=250)
    relase_date = models.DateTimeField(auto_now_add=True)
    language = models.CharField(choices=LANGUAGE,max_length=20)
    videofile= models.FileField(upload_to='netfiex_app/videos', null=True)
    thumbell = models.ImageField(upload_to="netfiex_app/image",null=True)
    view_count = models.ManyToManyField(User,related_name="content_view")
    description = models.TextField(null=True)

    def __str__(self):
        return f" this is tile -  {self.title}  to relase date -   {self.relase_date}"

    def total_view_count(self):
        return self.view_count.count()
    
   



class Like(models.Model):
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    content = models.ForeignKey(contentModel,related_name="like",on_delete=models.CASCADE)
    liked_at = models.DateField(auto_now_add=True)

class ReviewModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content = models.ForeignKey(contentModel,on_delete=models.CASCADE,null=True)
    comment = models.TextField()
    datePosted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"UserName : {self.user.username} fisrt Name : {self.user.first_name}    video content  Title: {self.content.title}"




class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)