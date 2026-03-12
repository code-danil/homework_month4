from django.shortcuts import render, redirect
from .forms import ITSpecialisForm

def registration_view(request):
    if request.method == 'POST':
        form = ITSpecialisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ITSpecialisForm()

    return render(request, 'registration.html', {'form': form})

