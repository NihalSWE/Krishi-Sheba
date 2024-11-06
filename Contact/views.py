<<<<<<< HEAD
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
=======
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import FormView 
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def Contact(request):  
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactForm()

    return render (request,'Contact/contact.html',{'form':form}) 


class ContactView(FormView):
    form_class=ContactForm
    template_name='Contact/contact.html'
    #success_url='/'
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Form successfully submitted!')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        form.save()
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('homeview')  
>>>>>>> origin/master
