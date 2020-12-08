from django.urls import path
from . import views
#import view

#path('url', '<view name>', name=<''url name>)
urlpatterns = [
    path('', views.home_site_view, name='home_site_view'),
    path('index.html/', views.home_site_view, name='home_site_view'),
    path('gallery/<int:number>/', views.gallery_view, name='gallery_view'),
    path('preview/<str:filename>/', views.preview_view, name='preview_view'),
    path('registry/', views.registry_view, name='registry_view'),
    path('login/', views.login_view, name='login_view'),
    path('menu/add/', views.addimage_view, name='addimage_view'),
    path('menu/logout/', views.logout_view, name='logout_view'),
    path('menu/', views.menu_view, name='menu_view'),
]