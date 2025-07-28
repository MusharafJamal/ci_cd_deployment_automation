from django.shortcuts import render, redirect
from .forms import Contactform
# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=Contactform()
    return render(request,'contact.html',{'form': form})
def success_view(request):
    return render(request,'success.html')