from django.shortcuts import render

def magic8ball(request):
    return render(request, 'magic8ball.html')
