from product.models import Product


def search_product(custom_word, city, category):
    products = Product.objects.all()

    if custom_word:
        products = Product.objects.filter(title__icontains=custom_word)
    if city:
        products = Product.objects.filter(city_id=city)
    if category:
        products = Product.objects.filter(category_id=category)

    if custom_word and city:
        products = Product.objects.filter(city_id=city).filter(title__icontains=custom_word)
    if custom_word and category:
        products = Product.objects.filter(category_id=category).filter(title__icontains=custom_word)
    if city and category:
        products = Product.objects.filter(category_id=category).filter(city_id=city)
    if custom_word and city and category:
        _products = Product.objects.filter(category_id=category).filter(city_id=city).filter(title__icontains=custom_word)

    return products
