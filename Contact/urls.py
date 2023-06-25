from django.urls import path
from django.views import View 
from .views import ContactView
from . import views
# from .pdf import post_pdf

urlpatterns = [
    

    path('Contact/', views.Contact, name="Contact"),
   
] 