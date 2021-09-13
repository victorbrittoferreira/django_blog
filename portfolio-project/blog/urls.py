from django.urls import path
 
from . import views 

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    
    #look for and int after "blog"
    path('<int:blog_id>/', views.detail, name = 'detail'),
]




