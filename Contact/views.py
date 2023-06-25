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