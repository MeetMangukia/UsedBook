from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views
from django.db.models import Q 
from django.shortcuts import render, get_object_or_404
from .models import Book
from account.models import BookSeller

# Create your views here.

def product_list(request):
    if request.method == 'POST':
        if request.POST['search_detail'] and request.POST['search_location']:
            search_detail = request.POST['search_detail']
            location = request.POST['search_location'].split(',')
            city = location[0] 
            books = Book.objects.all().filter(Q(book_title__icontains = search_detail) | 
                Q(book_author__icontains = search_detail),
                Q(book_owner__user_city__icontains=city))
            context = {
                'books': books
            }
            return render(request, 'products/product_list.html', context)
        elif request.POST['search_detail']:
            search_detail = request.POST['search_detail']
            books = Book.objects.all().filter(Q(book_title__icontains = search_detail) | 
                Q(book_author__icontains = search_detail))
            context = {
                'books': books
            }
            return render(request, 'products/product_list.html', context)
        else:
            # search location
            location = request.POST['search_location'].split(',')
            city = location[0] 
            books = Book.objects.filter(book_owner__user_city__icontains=city)
            context = {
                'books': books
            }
            return render(request, 'products/product_list.html', context)
        
    if request.GET.get('category', None):
        data = {
            'msg': "Oiii",
        }
        return JsonResponse(data)    

            
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'products/product_list.html', context)

def product_page(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    other_books = Book.objects.all().filter(book_owner = book.book_owner.id).filter(~Q(pk = book_id))
    context = {
        'book': book,
        'other_books': other_books,
    }
    return render(request, 'products/product_page.html', context)
