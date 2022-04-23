from django.shortcuts import render, redirect
from .models import Maleact
from .forms import MaleactForm


def actors_home(request):
    actors = Maleact.objects.all()
    return render(request, 'actors/actors_home.html', {"actors" : actors })


def create(request):
    error = ''
    if request.method == 'POST':
        form = MaleactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверная форма'
        return redirect('home')

    form = MaleactForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'actors/create.html', data)
