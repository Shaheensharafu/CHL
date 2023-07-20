from django.shortcuts import render
from django.http import HttpResponse
from .models import staffs,Doctor
from .forms import bookingform


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def bookings(request):
    if request.method == 'POST':
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conrfirmation.html')
    form=bookingform()
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)

def docters(request):
    dict_docs={
        "docs":Doctor.objects.all()
    }
    return render(request,"docters.html",dict_docs)

def contact(request):
    return render(request,"contact.html")

def staff(request):
    dict_staff={
        "staf":staffs.objects.all()
    }
    return render(request,"staffs.html",dict_staff)
