
from django.conf.urls import url
from django.urls import re_path,path,include

from . import views
app_name = 'blog'


urlpatterns = [
   path('index', views.index),
   path('article/<article_id>', views.article_page,  name='article_page'),
   path('edit/action', views.edit_action, name='edit_action'),
   path('edit/<article_id>', views.edit_page, name='edit_page'),
]

