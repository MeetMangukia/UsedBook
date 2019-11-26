from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from . import views
from .models import BookSeller
from product.models import Book

# Create your views here.

def dashboard(request):
    if request.method == "POST":
        if request.POST['form_type'] == 'signup':
            print("Signup")
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            password = request.POST['password']

        if request.POST['form_type'] == 'login':
            email = request.POST['email']
            password = request.POST['password']
            try:
                book_seller = BookSeller.objects.get(user_email=email, user_password=password)
                book_list = Book.objects.all().filter(book_owner=book_seller.id)
                context = {
                    'book_seller': book_seller,
                    'book_list': book_list,
                }
                messages.success(request, "Your success fully LogIn")
                return render(request, 'accounts/dashboard.html', context)
            except ObjectDoesNotExist:
                messages.error(request, "Your Email or Password is incorrect")
                return redirect('login')
            
    return render(request, 'accounts/dashboard.html')
    

def edit_profile(request, seller_id):
    if request.method == "POST":
        if request.POST['form_type'] == 'edit_profile':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            photo = request.POST['photo']

            book_seller = BookSeller(user_name=name, user_email=email, user_phone=phone,
            user_address=address, user_city=city, user_state=state, user_photo=photo)

            book_seller.save()
            messages.success(request, "Your data has been Updates")
    
    book_seller = BookSeller.objects.get(id=seller_id)
    context = {
        'book_seller': book_seller
    }
    return render(request, 'accounts/edit_profile.html', context)

def edit_password(request):
    return render(request, 'accounts/edit_password.html')

def add_product(request, seller_id):
    if request.method == "POST":
        if request.POST['form_type'] == 'product_form':
            category = request.POST['category'] 
            title = request.POST['title']
            author = request.POST['author']
            price = request.POST['price']
            edition = request.POST['edition']
            old = request.POST['old']
            pages = request.POST['pages']
            discription = request.POST['discription']

            photo_1 = request.POST['photo_1']
            photo_2 = request.POST['photo_2']
            photo_3 = request.POST['photo_3']
            photo_4 = request.POST['photo_4']

            book_seller = BookSeller.objects.get(id=seller_id)

            book = Book(book_owner=book_seller, book_category=category, book_title=title, book_author=author, 
            book_price=price, book_edition=edition, book_old=old, book_page=pages, 
            book_description=discription, book_image_1=photo_1, book_image_2=photo_2, 
            book_image_3=photo_3, book_image_4=photo_4)

            book.save()
    book_seller = BookSeller.objects.get(id=seller_id)
    context = {
        'book_seller': book_seller
    }
    return render(request, 'accounts/add_product.html', context)