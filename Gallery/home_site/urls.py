from django.urls import path
from . import views

#path('url', '<view name>', name=<''url name>)
urlpatterns = [
    path('', views.home_site_view, name='home_site_view'),
    path('index.html/', views.home_site_view, name='home_site_view'),
    path('gallery/<int:number>/', views.gallery_view, name='gallery_view'),
    path('preview/<str:filename>/', views.preview_view, name='preview_view'),
    path('register/', views.registry_view, name='registry_view'),
    path('login/', views.login_view, name='login_view'),
    path('menu/add/', views.addimage_view, name='addimage_view'),
    path('menu/logout/', views.logout_view, name='logout_view'),
    path('menu/addgallery/', views.addgallery_view, name='addgallery_view'),
    path('menu/changepasswd/', views.changepassword_view, name='changepassword_view'),
    path('menu/', views.menu_view, name='menu_view'),
    path('menu/editgroup/choice/', views.editgroup_choice_view, name='editgroup_choice_view'),
    path('menu/editgroup/data/<int:groupid>', views.editgroup_data_view, name='editgroup_data_view'),
    path('preview/<str:filename>/edit/', views.editimage_view, name='editimage_view'),
    path('preview/<str:filename>/delete/', views.deleteimage_view, name='deleteimage_view'),
]