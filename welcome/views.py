from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    return render(request, 'welcome/welcome_page.html')