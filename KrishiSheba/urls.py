from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Pages.urls')),
    path('accounts/',include('Accounts.urls')),
    path('contact/',include('Contact.urls')),
    path('ProductItem/',include('ProductItem.urls')),
    
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
