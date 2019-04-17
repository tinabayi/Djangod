from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30,null=True)
    last_name = models.CharField(max_length =30,null=True)
    email = models.EmailField(null=True) 

    def save_editor(self):
        self.save()  

class Category(models.Model):
    name = HTMLField()

    def __str__(self):
        return self.name       
    class Meta:
        ordering = ['name']

    def save_category(self):
        self.save()
    def update_category(self):
        self.update()
    def delete_category(self):
        self.delete()



class Project(models.Model):
    project_name = models.CharField(max_length =30)
    project_description = HTMLField()
    editor=models.ForeignKey(Editor,on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    
   
    def save_project(self):
        self.save() 
    def delete_project(self):
        self.delete() 
    @classmethod
    def get_project(cls):
        projects = Project.objects.all()
        return projects


    @classmethod
    def search_by_category(cls,search_term):
                category = Category.objects.filter(name__icontains=search_term).first()
                project = cls.objects.filter(category=category)
                return project


class Comment(models.Model):
    comments = HTMLField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)


    def save_comment(self):
        self.save() 
    def delete_comment(self):
        self.delete() 
    @classmethod
    def get_comment(cls):
        comments = Comment.objects.all()
        return comments 
class Like(models.Model):
    like = models.CharField(max_length =30)
    project=models.ForeignKey(Project)

    def save_like(self):
        self.save() 
    def delete_like(self):
        self.delete()      