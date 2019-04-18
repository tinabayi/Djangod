
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prof_picture = models.ImageField(upload_to = 'images/')
    user_bio = models.CharField(max_length =200)
    projects_posted=  models.IntegerField(null = True)
    contact_information=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

class Image(models.Model):
    project = models.ImageField(upload_to = 'images/',null = True)
    project_name = models.CharField(max_length =30,null=True)
    project_description= models.TextField(null=True)
    comments= models.CharField(max_length =30)
    likes = models.CharField(max_length =30)
    user=models.ForeignKey(User,null = True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    project_url= models.CharField(max_length =30,null=True)
    def save_image(self):
        self.save() 
    def delete_image(self):
        self.delete() 
    
        self.update()  
    @classmethod
    def get_image(cls):
        projects = Image.objects.all()
        return projects

    @classmethod
    def search_by_project_name(cls, search_term):
        project = cls.objects.filter(project_name__icontains=search_term)
        return project   

class Comment(models.Model):
    comments = models.CharField(max_length =30)
    image=models.ForeignKey(Image, on_delete=models.CASCADE,null=True)


    def save_comment(self):
        self.save() 
    def delete_comment(self):
        self.delete() 
    @classmethod
    def get_comment(cls):
        comments = Comment.objects.all()
        return comments

class Rating(models.Model):
    design= models.IntegerField(null=True)
    usability=models.IntegerField(null=True)
    content = models.IntegerField(null=True)
    image=models.ForeignKey(Image, on_delete=models.CASCADE,null=True)
    def save_rating(self):
        self.save() 
    def delete_rating(self):
        self.delete() 
    @classmethod
    def get_rating(cls):
        ratings = Rating.objects.all()
        return ratings
