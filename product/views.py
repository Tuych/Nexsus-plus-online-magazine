from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import ProductImage
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            product_image = request.POST.get('file')
            product_detail_image = request.POST.get('file2')
            ProductImage.objects.create(product=product, image=product_image, detail_image=product_detail_image)
            return redirect('products')

    form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'product/create.html', context)
