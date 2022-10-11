from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
     path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contect_us",views.contect_us,name='contect_us'),
    path("services",views.services,name='services')
    
]