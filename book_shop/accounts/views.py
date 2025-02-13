from django.shortcuts import render


def profile(request):
    template_name = 'accounts/profile.html'
    return render(request, template_name)
