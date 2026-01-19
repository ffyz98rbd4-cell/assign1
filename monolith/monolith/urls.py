from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('cart/', include('cart.urls')),
]
