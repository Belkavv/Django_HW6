import logging
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Product
from .forms import ProductForm

logger = logging.getLogger(__name__)


def index(request):
    context = {"title": 'Главная страница'}
    logger.info('Index page accessed')
    return render(request, "hw4/index.html", context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            Product.objects.create(
                name=form_data['name'],
                description=form_data['description'],
                price=form_data['price'],
                quantity=form_data['quantity'],
                image=request.FILES['image']
            )

    else:
        form = ProductForm()
    context = {'title': 'Добавить продукт', 'form': form}
    return render(request, 'hw5/add_product.html', context)
