from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, EmailMultiAlternatives

from django.template.loader import get_template
from django.utils.decorators import method_decorator

from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from .models import NewsLetterUser, NewsLetter
from .forms import NewsLetterUserSignupForm, NewsLetterCreationForm


def newsletter_signup(request):
    form = NewsLetterUserSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'You have already subscibed to our mailing service')
        
        else:        
            instance.save()
            messages.success(request, 'You have successfully subscribed to our mailing service')
            subject = "Thanks for joining our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/templates/newsletter/sign_up_email/html") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/unsubscribe_email.html")
            message.attach_alternative(html_template, "text/html")
            message.send()
    context = {
            'form':form,
    }
    return render(request, 'newsletter/sign_up.html', context)

def newsletter_unsubscribe(request):
    form = NewsLetterUserSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            NewsLetterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your email has successfully removed from our mailing service')
            subject = "You have been unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/templates/newsletter/unsubscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/unsubscribe_email.html")
            message.attach_alternative(html_template, "text/html")
            message.send()
        else:
            messages.warning(request, 'You email is not subscibed to our mailing service')            
    context = {
            'form':form,
    }
    return render(request, 'newsletter/unsubscribe.html', context)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        