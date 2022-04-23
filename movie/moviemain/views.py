from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Fargo', 'Lebovski', 'Joker'],
        'info': {
            'genre':'triller',
            'year': 1994,
            'raiting': 6
        }
    }
    return render(request, 'moviemain/index.html', data)
