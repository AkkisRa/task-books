# cloth/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import ProductCL, OrderCL, TagCL
from .forms import OrderCLForm

class MainView(ListView):
    model = ProductCL
    template_name = 'base.html'
class ProductListView(ListView):
    model = ProductCL
    template_name = 'product_list.html'


class OrderCreateView(View):
    template_name = 'order_form.html'

    def get(self, request, *args, **kwargs):
        form = OrderCLForm()
        return render(request, 'order_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = OrderCLForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # Устанавливаем total_price на основе цены товара и его количества
            order.total_price = form.cleaned_data['product'].price * form.cleaned_data['quantity']
            order.save()

            # Теперь, когда у заказа есть ID, мы можем добавить теги
            order.tags.set(form.cleaned_data['tags'])

            return render(request, 'success_page.html')
        return render(request, 'order_form.html', {'form': form})
class Tag1ListView(ListView):
    model = ProductCL
    template_name = 'tag1_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        tag = TagCL.objects.get(name='prada')
        return ProductCL.objects.filter(tags=tag)


class Tag2ListView(ListView):
    model = ProductCL
    template_name = 'tag2_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        tag = TagCL.objects.get(name='warm')
        return ProductCL.objects.filter(tags=tag)

class Tag3ListView(ListView):
    model = ProductCL
    template_name = 'tag3_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        tag = TagCL.objects.get(name='jewelry')
        return ProductCL.objects.filter(tags=tag)

class Tag4ListView(ListView):
    model = ProductCL
    template_name = 'tag4_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        tag = TagCL.objects.get(name='cap')
        return ProductCL.objects.filter(tags=tag)
