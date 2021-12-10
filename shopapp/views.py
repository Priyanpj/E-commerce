from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from . models import feature_products
from . models import category
from . forms import ModeForm
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# from. models import products
# Create your views here.

def fun(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prodt=feature_products.objects.filter(prod_cat=c_page)
    else:
        prodt=feature_products.objects.all()
    cat=category.objects.all()
    # paginator = Paginator(prodt, 6)
    # try:
    #     page = int(request.GET.get('page', '1'))
    # except:
    #     page = 1
    # try:
    #     pro = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     pro = paginator.page(paginator.num_pages)
    return render(request,"index.html",{'results':prodt,'ct':cat})
# ,'pg':pro
def contact(request):
    return render(request,'contact-us.html')
def blogs(request):
    jakki = feature_products.objects.all()
    return render(request,"blog.html",{'blog': jakki})
# def blogii(request):
#     jakkis = feature_products.objects.all()
#     return render(request,"blog.html",{'blog': jakkis})
def proadd(request):
    objh=feature_products.objects.all()
    return render(request,"update.html",{'resultse':objh})
# def proadd(request):
#     objh=feature_products.objects.all()
#     return render(request,"adupde.html",{'resultse':objh})
# def detiall(request,pro_id):
#     product=feature_products.objects.get(id=pro_id)
#     return render(request,'product-details.html',{'productss':product})
def detial(request,pro_id):
    product=feature_products.objects.get(id=pro_id)
    cat = category.objects.all()
    prodt=feature_products.objects.all()
    return render(request,'product-details.html',{'products':product,'results':prodt,'ct':cat})
def blog(request,pro_id):
    cat = category.objects.all()
    product=feature_products.objects.get(id=pro_id)
    return render(request,'blog.html',{'products':product,'ct':cat})
# def blog(request,pro_id):
#     product=feature_products.objects.get(id=pro_id)
#     return render(request,'blog.html',{'products':product})

def detials(request,pro_id):
    product=feature_products.objects.get(id=pro_id)
    return render(request,'update.html',{'products':product})
def filter(request,proo_id):
    category=feature_products.objects.get(id=proo_id)
    return render(request,'index.html',{'categorys':category})
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price = request.POST.get('price')
        img = request.FILES['img']
        prod_cat = request.POST.get('prod_cat')
        pro_desc = request.POST.get('pro_desc')
        # offer = request.POST.get('offer')(default=False)
        s=feature_products(name=name,price=price,img=img,prod_cat=prod_cat,pro_desc=pro_desc)
        s.save()
        messages.info(request,"product added")
    return render(request,"adupde.html")
def update(request,id):
    objh=feature_products.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=objh)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'objh':objh})
def delete(request,id):
    if request.method=='POST':
        objh=feature_products.objects.get(id=id)
        objh.delete()
        return redirect('/')
    return render(request,'delete.html')
def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=feature_products.objects.all().filter(Q(name__contains=query)|Q(pro_desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})
def shop(request):
    jakki=feature_products.objects.all()
    return render(request,"shop.html",{'shop': jakki})
# ,'pg':pro