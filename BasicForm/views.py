from django.shortcuts import render
from django.http import HttpResponse
from .BasicForm import ContactForm
from . import service


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_response = service.form_service(form)
            return HttpResponse(user_response)

    form = ContactForm
    return render(request, 'form.html', {'form': form})
