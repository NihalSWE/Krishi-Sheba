from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages  # Import messages
from .models import F_Data
from .forms import ContactForm

class ContactView(View):
    template_name = 'Contact/contact.html'
    success_url = reverse_lazy('contact')  # Redirect back to the contact page after form submission

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the F_Data model
            messages.success(request, "Your message has been sent successfully!")  # Add success message
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
