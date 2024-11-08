from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('category/', views.category_page, name='category_page'),
    path('stands/', views.stand_list, name='stand_list'),
    path('stands/<slug:slug>/', views.stand_detail, name='stand_detail'),
    path('hosper/<slug:slug>/', views.hosper_detail, name='hosper_detail'),
    path('hospers/', views.hosper_list, name='hosper_list'),
    path('smokehouses/', views.smokehouse_list, name='smokehouse_list'),
    path('smokehouses/<slug:slug>/', views.smokehouse_detail, name='smokehouse_detail'),

]