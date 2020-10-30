from django.urls import path
from . import views
#import view

#path('url', '<view name>', name=<''url name>)
urlpatterns = [
    path('', views.home_site_view, name='home_site_view'),
    path('gallery/<int:number>', views.gallery_view, name='gallery_view')
]