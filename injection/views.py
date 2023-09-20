from django.shortcuts import render
from .forms import (
    InjectionForm,
)
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def injection1(request):
    if request.method == "POST":
        form = InjectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "성공~!")
            return HttpResponseRedirect('/injection1')
        
        else:
            return render(request, "injection/injection_1.html", {'form':form})
    else:
        form = InjectionForm()
        return render(request, "injection/injection_1.html", {'form':form})
    return render(request, "injection/injection_1.html")