from email import message
from itertools import product
from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles})      

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product':product})      

def add_to_cart(request):
 user=request.user
 product = request.GET.get('prod_id')
 print(product) 
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 add = Customer.objects.filter(user=request.user) 
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category='M')
 elif data == 'Redmi' or data == 'Samsung':
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=2000)
 elif data == 'above':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=2000)        
 return render(request, 'app/mobile.html', {'mobiles':mobiles})


class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm
  return render(request, 'app/customerregistration.html', {'form':form})
  
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   form.save()
  return render(request, 'app/customerregistration.html', {'form':form})       

def checkout(request):
 return render(request, 'app/checkout.html')
def password_reset(request):
  pass

class ProfileView(View):
  def get(self, request):
    form = CustomerProfileForm()
    return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
  def post(self, request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      usr = request.user
      name = form.cleaned_data['name']
      locality = form.cleaned_data['locality']
      city = form.cleaned_data['city']
      state = form.cleaned_data['state']
      zipcode = form.cleaned_data['zipcode']
      reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
      reg.save()  
    return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})        
