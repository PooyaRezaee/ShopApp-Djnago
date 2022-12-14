from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from apps.home.models import Product
from .models import *
from .utils import Cart
import json

__all__ = [
    'CheckoOutView',
    'EditItemView'
]

class CheckoOutView(LoginRequiredMixin,View):
    def get(self,request):
        cart = CartSession.objects.filter(user=request.user)
        if cart.exists():
            cart = cart.get()
            return render(request,'cart/checkout.html',{'items':cart.items,'cart_detail':cart})
        else:
            return render(request,'cart/checkout.html')

class EditItemView(LoginRequiredMixin,View):
    def post(self,request):
        data = json.load(request)
        type = data['type']
        product_id = data['product_id']

        cart = Cart(request.user.id)
        if type == "add":
            count_product = Product.objects.get(id=product_id).amount
            if count_product == cart.count_item(product_id):
                return JsonResponse(
                            {
                                'status':'error',
                                'code':'404'
                            }
                            )
            cart.add_item(product_id)
        elif type == "subtract":
            try:
                cart.subtract_item(product_id)
            except:
                return JsonResponse({'status':'error','code':'404'})

        
        return JsonResponse(
            {
                'status':'ok',
            }
            )