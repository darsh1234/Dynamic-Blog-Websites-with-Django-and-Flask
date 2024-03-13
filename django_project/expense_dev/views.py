from django.shortcuts import render

def home(request):
    return render(request , 'expense_dev/home.html')
