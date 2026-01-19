from django.http import JsonResponse
from .models import Cart, CartItem
from accounts.models import Customer
from books.models import Book

def add_to_cart(request):
    customer = Customer.objects.get(id=request.POST['customer_id'])
    book = Book.objects.get(id=request.POST['book_id'])

    cart, _ = Cart.objects.get_or_create(customer=customer)
    CartItem.objects.create(cart=cart, book=book, quantity=1)

    return JsonResponse({'message': 'Added to cart'})

def view_cart(request, customer_id):
    cart = Cart.objects.get(customer_id=customer_id)
    items = CartItem.objects.filter(cart=cart)

    data = []
    for item in items:
        data.append({
            'book': item.book.title,
            'quantity': item.quantity
        })

    return JsonResponse(data, safe=False)
