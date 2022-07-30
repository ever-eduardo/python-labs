from django.shortcuts import render
from .models import Quote


# Create your views here.
def show_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})

