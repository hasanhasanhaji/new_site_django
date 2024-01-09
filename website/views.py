from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages


# Create your views here.


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.data)
        if form.is_valid():
            # Set the subject field to None before saving
            form.instance.name = "Nashenas"
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket submitted very well")
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didnt submitted successfully")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your email submitted very well!")
            return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.ERROR, "Your email didnt submitted successfully!")
        return HttpResponseRedirect('/')
    return render(request, 'website/base.html', {'form': form})
