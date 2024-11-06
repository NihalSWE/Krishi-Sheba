from django.urls import path
<<<<<<< HEAD
from .views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]
=======
from django.views import View 
from .views import ContactView
from . import views
# from .pdf import post_pdf

urlpatterns = [
    

    path('Contact/', views.Contact, name="Contact"),
   
] 
>>>>>>> origin/master
