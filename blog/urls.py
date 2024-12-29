from django.urls import path
from blog.views import index, page, post

app_name = "blog"
urlpatterns = [
   path('', index, name='index'),
   path('page/<slug:slug>', page, name='post'),
   path('post/', post, name='page'),
]
