from django.shortcuts import render

# Create your views here.
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)
    


@csrf_exempt
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'GET':
        return JsonResponse(model_to_dict(book))
    elif request.method == 'PUT':
        # Handle the update logic if needed
        # Example: Update the title
        title = request.POST.get('title')
        book.title = title
        book.save()
        return JsonResponse(model_to_dict(book))
    elif request.method == 'DELETE':
        # Handle the delete logic
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'true', 'message': 'Invalid request method'}, status=400)


