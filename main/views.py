from django.shortcuts import render, get_object_or_404
from product.models import City, Category, Product
from .search import search_product
from blog.models import Post


def index(request):
    cities = City.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()[:6]
    posts = Post.objects.all()[:3]

    context = {
        'cities': cities,
        'categories': categories,
        'products': products,
        'posts': posts,
    }
    return render(request, 'main/index.html', context)


def products(request):
    custom_word = request.GET.get('customword', None)
    city = request.GET.get('city', None)
    category = request.GET.get('category', None)

    city = int(city) if city and city.isdigit() else None
    category = int(category) if category and category.isdigit() else None

    _products = search_product(custom_word, city, category)

    cities = City.objects.all()
    categories = Category.objects.all()

    context = {
        'products': _products,
        'cities': cities,
        'categories': categories,
        'custom_word': custom_word,
        'get_city': city,
        'get_category': category

         }

    return render(request, 'main/products.html', context)

# def category(request, category_id):
#     cities = City.objects.all()
#     categories = Category.objects.all()
#     products = Product.objects.filter(Q(category=category_id) | Q(category_parent=category_id))  # Q or vazifasida keladi __ bilan boshqa columlarnu ulasak buladi
#
#     context = {
#         'products': products,
#         'cities': cities,
#         'categories': categories,
#     }
#
#     return render(request, 'main/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    products = Product.objects.all().exclude(id=product_id)[:5]  # .exclude(id=product_id) id si prodect_id ga teng bulmagan ini chiqar

    context = {
        'product': product,
        'products': products
    }
    return render(request, 'main/product_details.html', context)
