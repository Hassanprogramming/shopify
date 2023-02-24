from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import *
from . utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def Search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(name=query))

    return render(request, 'store/search.html', {'products': products, 'query': query})

def Registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form':form}
    return render(request, 'store/Registration.html', context)

def loginPage(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("store")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="store/login.html", context={"login_form":form})

def logoutUser(request):
    logout(request)
    return redirect('login')

def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']

    website = Website.objects.all()
    products = Shop.objects.all()
    context = {'products': products,'website': website, 'cartItems': cartItems}
    return render(request, 'store/shop.html', context)


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    website = Website.objects.all()
    products = Product.objects.filter(luxury=False)
    second_product = Product.objects.filter(luxury=True)
    context = {'products': products,'website': website, 'cartItems': cartItems, 'second_product':second_product}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

# we can also use this dicoratore for csrf-token in here instead doing this in our html
# @csrf_exempt


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,  created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)
        
       
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShppingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['address'],
            state=data['shipping']['address'],
            zipcode=data['shipping']['address'],
        )
    return JsonResponse('Payment complete!', safe=False)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)


def post(request,pid):
    #post = Product.objects.get(id=pid)
    data = cartData(request)
    cartItems = data['cartItems']

    product = get_object_or_404(Product,pk=pid)
    context = {'product':product, 'cartItems':cartItems}
    return render(request, 'store/product.html', context)
