from django.shortcuts import render,redirect,get_object_or_404
from shopapp.models import *
from . models import  *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cartdetials(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quantity)
            count+=i.quantity
    except ObjectDoesNotExist:
        pas
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def add_cart(request,pro_id):
    prod=feature_products.objects.get(id=pro_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        c_items.quantity
        c_items.quantity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quantity=1,cart=ct)
        c_items.save()
    return redirect('cartdetials')


def min_cart(request,pro_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(feature_products, id=pro_id)
    c_items = items.objects.get(prodt=prod, cart=ct)
    if c_items.quantity >1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetials')
def cart_delete(request,pro_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(feature_products, id=pro_id)
    c_items = items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartdetials')