from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from . utils import cartData, guestOrder
from store.views import cartData 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def category(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = CategoryProduct.objects.all()
    context = {'products': products,
               'cartItems': cartItems}
    return render(request, 'category/category.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = CategoryProduct.objects.get(id=productId)
    order, created = CategoryOrder.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = CategoryOrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

@csrf_exempt


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,  created = CategoryOrder.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)
        
       
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        CategoryShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['address'],
            state=data['shipping']['address'],
            zipcode=data['shipping']['address'],
        )
    return JsonResponse('Payment complete!', safe=False)
