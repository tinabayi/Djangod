from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import NewProjectForm,CommentForm
from .models import Project,Comment
# Create your views here.

def welcome(request):
    projects = Project.get_project()
    comments = Comment.objects.all()
    return render(request, 'all-Here/welcome.html',{"projects":projects,"comments":comments})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form}) 

def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

            return redirect(welcome)

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_projects = Project.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-Here/search.html',{"message":message,"projects": searched_projects})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-Here/search.html',{"message":message})

 

