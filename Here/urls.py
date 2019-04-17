from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^project/', views.new_project, name='new-project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/', views.comment, name='comment')
   
]