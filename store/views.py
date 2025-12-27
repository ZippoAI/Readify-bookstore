from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/pages/home.html')




def all_books(request):
    return render(request, 'store/pages/all_books.html')