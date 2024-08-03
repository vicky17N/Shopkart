from django.shortcuts import redirect, render,HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from . models import *
from django.contrib import messages
from shop.form import *
from django.contrib.auth import authenticate, login,logout
import json
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def home(req):
    products = Products.objects.filter(Trending=1)
    return render(req,'shop/index.html',{"products":products})

def login_page(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        if req.method =="POST":
            name = req.POST.get('username')
            pwd = req.POST.get('password')
            user = authenticate(req,username = name, password = pwd)
            if user is not None:
                login(req,user)
                messages.success(req,"Logged in successfully..")
                return redirect('/')
            else:
                messages.error(req,"Invalid username and password")
                return redirect("/login")
        return render(req,'shop/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect('/')

def reg(req):
    form = CustomUserForm()
    if req.method == "POST":
        form = CustomUserForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Registration Successful. Now you can login..!")
            return redirect('/login')
    return render(req,'shop/Register.html',{'form':form})

def collections(req):
    catogory = Catogory.objects.filter(status=0)
    return render(req,'shop/collections.html',{"catogory":catogory})

def collectionsview(req,name):
    if(Catogory.objects.filter(name=name,status=0)):
        products = Products.objects.filter(Catogory__name=name)
        return render(req,'shop/products/index.html',{"products":products,'catogory':name})
    else:
        messages.warning(req,"No Such Catogory Found")
        return redirect('collections')
    
def product_details(req,cname,pname):
    if(Catogory.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            products = Products.objects.filter(name=pname,status=0).first()
            return render(req,'shop/products/product_details.html',{"products":products})
        else:
            messages.error("No such product found")
            redirect('collections')
    else:
        messages.error("No such Catogory found")
        redirect('collections')

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Products.objects.get(id=product_id)
      if product_status:
        if cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   
def Cart(request):
   if request.user.is_authenticated:
      Cart = cart.objects.filter(user = request.user)
      return render(request,'shop/Cart.html',{"Cart":Cart})
   else:
      return redirect('/login')
   
def remove_cart(req,cid):
   cartitem = cart.objects.get(id=cid)
   cartitem.delete()
   return redirect('/Cart')

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Products.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   
def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"shop/fav.html",{"fav":fav})
  else:
    return redirect("/login")
 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

def shipping_address_view(request,pname):
    form = ShippingAddressForm()
    products = Products.objects.filter(name = pname,status=0)
    if request.user.is_authenticated:
        try:
           if ShippingAddress.objects.get(user=request.user):
            return redirect(reverse('payment', kwargs={'pname': pname}))  
        except ShippingAddress.DoesNotExist:
          if request.method == 'POST':
              form = ShippingAddressForm(request.POST)
              if form.is_valid():
                  shipping_address = form.save(commit=False)
                  shipping_address.user = request.user
                  shipping_address.save()
                  messages.success(request,"Address added succesfully...!")
                  return redirect(reverse('payment', kwargs={'pname': pname} ))  
              else:
                  form = ShippingAddressForm()
        else:
          return redirect('/address')    
    else:
       return redirect('/login')

    return render(request, 'shop/Address.html',{'form':form,'products':products})

# Address  edit  page
def edit_address(request,pname):
    address, created = ShippingAddress.objects.get_or_create(user=request.user)
    products = Products.objects.filter(name = pname,status=0)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect(reverse('payment', kwargs={'pname': pname}))   # Redirect to a success page or another view
    else:
        form = ShippingAddressForm(instance=address)
    return render(request, 'shop/Address.html', {'form': form,'products':products})


# checkout page
def payment_view_page(req,pname):
   products = Products.objects.filter(name = pname,status=0).first()
   address = ShippingAddress.objects.filter( user = req.user)
   return render(req,'shop/payment.html' ,{'address':address,'products':products})
   


def cart_to_payment(request):
   form  = ShippingAddress()
   Cart = cart.objects.filter(user = request.user)
   products = Products.objects.filter(status=0).first()
   address = ShippingAddress.objects.filter( user = request.user)
   return render(request,'shop/checkout.html',{'cart':Cart,'products':products,'address':address})


def proceed_to_pay(request):
    if request.method == 'POST':
        total_price_value = request.POST.get('total_price', 0)
        return JsonResponse({
            'total_price': total_price_value,
        })
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def proceed_to_pay2(req):
   Cart = cart.objects.filter(user = req.user)
   total_price = 0
   for item in Cart:
      total_price = total_price +item.product.selling_price*item.product_qty
   return JsonResponse({
      "total_price":total_price
   })


@login_required
@require_POST
def order_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        data=json.load(request)
        product_id=data['pid']
        product_status=Products.objects.get(id=product_id)
        if product_status:
            Orders.objects.create(user=request.user,product_id=product_id)
            return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

def order_page_view(req):
   if req.user.is_authenticated:
    orders = Orders.objects.filter(user = req.user)
    products = Products.objects.filter(status=0).first()
    return render(req,'shop/order_page.html',{'orders':orders,'products':products})
   else:
      return redirect('/login')