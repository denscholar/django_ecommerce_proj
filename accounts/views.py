from django.shortcuts import render

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)



def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)
