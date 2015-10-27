
from django.conf.urls import patterns, url
from ToDoListApp import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^add_category/$', views.add_category, name='add_category'),
               url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
               url(r'^category/(?P<category_name_slug>[\w\-]+)/add_task/$', views.add_task, name='add_task'),
               url(r'^test/', views.test, name='test'),
               ]