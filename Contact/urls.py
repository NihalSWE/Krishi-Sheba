from django.urls import path
from .views import ContactView  # Import the ContactView directly

urlpatterns = [
    path('Contact/', ContactView.as_view(), name="Contact"),  # Use .as_view() for class-based views
]
