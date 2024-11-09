
from django.http import JsonResponse
from django.shortcuts import render,redirect
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,AddCart,Order,Machinery,Rent_Request
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.
class ProductView(View):
    def get(self,request):
        seeds=Product.objects.filter(category='S')
        pesticides=Product.objects.filter(category='P')
        fertilizers=Product.objects.filter(category='F')
        return render(request,'ProductItem/seedingitem.html',{'seeds':seeds,'pesticides':pesticides,'fertilizers':fertilizers})

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        item_already_in_cart= False
        if request.user.is_authenticated:
            item_already_in_cart= AddCart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'ProductItem/productdetail.html',{'product':product , 'item_already_in_cart':item_already_in_cart})




@login_required
def add_to_cart(request):
 user=request.user
 product_id=request.GET.get('prod_id')
 product=Product.objects.get(id=product_id)
 AddCart(user=user,product=product).save()
 return redirect('showcart')


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=AddCart.objects.filter(user=user)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in AddCart.objects.all()
        if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                total_amount = amount + shipping_amount
        return render(request, 'ProductItem/addtocart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})

from django.db.models import Q
from django.http import JsonResponse
def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=AddCart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in AddCart.objects.all()
        if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data={
         'quantity':c.quantity,
         'amount': amount,
         'total_amount':amount + shipping_amount
            }
        return JsonResponse(data)


def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=AddCart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in AddCart.objects.all()
        if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        data={
         'quantity':c.quantity,
         'amount': amount,
         'total_amount':amount + shipping_amount
            }
        return JsonResponse(data)



def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=AddCart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in AddCart.objects.all()
        if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data={
         'amount': amount,
         'total_amount':amount + shipping_amount
            }
        return JsonResponse(data)

@login_required
def checkout(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items=AddCart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in AddCart.objects.all()
    if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        total_amount=amount+shipping_amount
    return render(request, 'ProductItem/checkout.html',{'add':add,'total_amount':total_amount,'cart_items':cart_items})


@login_required
def paymentdone(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=AddCart.objects.filter(user=user)
    for c in cart:
        Order(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

@login_required
def orders(request):
 op=Order.objects.filter(user=request.user)
 return render(request, 'ProductItem/orders.html',{'order_placed':op})


# from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.core.paginator import Paginator
class MachineryView(View):
    def get(self, request):
        # Fetch all available machinery items
        machines = Machinery.objects.filter(is_Available=True)

        # Set up pagination: 6 items per page
        paginator = Paginator(machines, 6)  # 6 items per page
        page_number = request.GET.get('page')  # Get the page number from the URL
        page_obj = paginator.get_page(page_number)

        # Render template with the paginated machines
        return render(request, 'ProductItem/machineryitem.html', {'machines': page_obj})


class MachineryDetailView(View):
    def get(self,request,pk):
        mproduct=Machinery.objects.get(pk=pk)
        return render(request,'ProductItem/machinedetail.html',{'mproduct':mproduct})


@login_required
def machinery_contact(request):

   
    if request.method == 'POST':

       product_name=request.POST['mproduct']
       user_id=request.POST['user_id']
       product_id=request.POST['product_id']
       name=request.POST['name']
       email=request.POST['email']
       phone=request.POST['phone']
       message=request.POST['message']



       if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Rent_Request.objects.all().filter(user_id=user_id,product_id=product_id)

            if has_contacted:
                messages.error(request, 'You have already has contact for this ')
                return redirect('rent')
        
       
       
       machinery_contact=Rent_Request(product_name=product_name,name=name,email=email,phone=phone,message=message,user_id=user_id,product_id=product_id)

       machinery_contact.save()

       messages.success(request,'Your Request has been submited.We will contact you soon')

       

       return redirect('rent')


def rent(request):

    interested_machinery_details=Rent_Request.objects.filter(user_id=request.user.id)
    context={

        'interested_machinery_details':interested_machinery_details,
         
        }

    return render(request,'ProductItem/rent.html',context)


from django.db.models import Q
def search (request,):
    query=request.POST.get('search','')
    if query:
        queryset=(Q(title__icontains=query)) | (Q(selling_price__icontains=query)) | (Q(category__icontains=query)) | (Q(description__icontains=query)) | (Q(brand__icontains=query))
        results=Product.objects.filter(queryset).distinct()
    
    else:
        results=[]
    context = {
        'results':results
    }
    return render (request,'ProductItem/search.html',context)


def information(request):
    return render(request,'ProductItem/info.html')