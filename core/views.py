from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import OrderForm
from .cart import Cart

def home(request):
    products = Product.objects.all()
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, f'Заказ #{order.id} успешно оформлен! Мы свяжемся с вами в ближайшее время.')
            cart.clear()
            return redirect('home')
    else:
        form = OrderForm()
    
    context = {
        'products': products,
        'form': form,
        'cart': cart,
    }
    return render(request, 'core/home.html', context)