from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from .models import Book
from django.http import HttpResponse
import os

def index(request):
    return render(request, 'index.html')

def get_books(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

@csrf_exempt
def create_book(request):
    data = json.loads(request.body)
    book = Book.objects.create(title=data['title'], author=data['author'])
    return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author})

@csrf_exempt
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return JsonResponse({'status': 'deleted'})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

def monitor(request):
    return render(request, 'monitor.html')

@csrf_exempt
def crash(request):
    os._exit(1)
    
def ping(request):
    return HttpResponse("pong")