from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer

def register(request):
    if request.method == 'POST':
        Customer.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return JsonResponse({'message': 'Register success'})
