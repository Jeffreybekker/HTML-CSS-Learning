from django.shortcuts import render

# Create your views here.
def buttons(request):
    return render(request, 'buttons.html')


def text(request):
    return render(request, 'text.html')