from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    context = {

    }
    return render(request, template)
