from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)
