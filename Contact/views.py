from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'Contact/contact.html', {'form': form})

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'Contact/contact.html'
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'success': True})
    
    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors})

    def get_success_url(self):
        return reverse_lazy('homeview')
