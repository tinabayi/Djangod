from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^api/image/$', views.ImageList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/profile$', views.profile, name='profile'),
    url(r'^view/profile/(\d+)', views.viewprofile, name='viewprofile'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^new/comment$', views.comments, name='comments'),
    url(r'^new/rating$', views.rating, name='rating'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.project, name ='project'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

