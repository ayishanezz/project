from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,DeleteView
from account.models import Products,Cart,Review,Orders
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

#decorator

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please login first!!")
            return redirect('log')
    return inner

dec=[signin_required,never_cache]

# Create your views here.

# class HomeView(View):
#     def get(self,request):
#         return render(request,"uhome.html")

@method_decorator(dec,name="dispatch")
class HomeView(TemplateView):
    template_name='uhome.html'


# class ProductsView(View):
#     def get(self,request):
#         data=Products.objects.all()
#         return render(request,"products.html",{"data":data})
@method_decorator(dec,name="dispatch")
class ProductsView(ListView):
    template_name="products.html"
    queryset=Products.objects.all()
    context_object_name="products"

    def get_context_data(self, **kwargs):
        # res=super().get_context_data(**kwargs)
        # print(res)
        res=Products.objects.filter(categories=self.kwargs.get('cat'))
        print(res)
        print(self.kwargs)
        return{"products":res}
    

# class DetailsView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('pid')
#         pro=Products.objects.get(id=id)
#         return render(request,"details.html",{"data":pro})
    
@method_decorator(dec,name="dispatch")
class DetailsView(DetailView):
    template_name="details.html"
    queryset=Products.objects.all()
    pk_url_kwarg='pid'
    context_object_name="product"
    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        pid=self.kwargs.get('pid')
        product=Products.objects.get(id=pid)
        rev=Review.objects.filter(product=product)
        context['reviews']=rev
        print(context)
        return context

dec
def addtocart(request,*args,**kwargs):
    pid=kwargs.get('pid')
    pro=Products.objects.get(id=pid)
    user=request.user
    Cart.objects.create(product=pro,user=user)
    return redirect('home')

@method_decorator(dec,name="dispatch")
class CartList(ListView):
    template_name="cartlist.html"
    queryset=Cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user,status="Added")
        return res
    
# class DeleteView(View):
#     def get(self,request,**kwargs):
#         id=kwargs.get('cid')
#         data=Cart.objects.get(id=id)
#         data.delete()
#         return redirect('cart')

@method_decorator(dec,name="dispatch")
class CartDeleteView(DeleteView):
    model=Cart
    success_url=reverse_lazy('cart')
    template_name='deletecart.html'
    pk_url_kwarg='cid'

dec
def addreview(request,**kwargs):
    review=request.POST.get('rev')
    product_id=kwargs.get('pid')
    product=Products.objects.get(id=product_id)
    user=request.user
    print(review,product_id)
    Review.objects.create(review=review,user=user,product=product)
    messages.success(request,"Review Added!!")
    return redirect('home')

@method_decorator(dec,name="dispatch")
class Placeorder(TemplateView):
    template_name="placeorder.html"
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        product=cart.product
        user=request.user
        Orders.objects.create(product=product,user=user,phone=phone,address=address)
        cart.status="Order Placed"
        cart.save()
        return redirect('home')


@method_decorator(dec,name="dispatch")
class OrderList(ListView):
    template_name="order.html"
    queryset=Orders.objects.all()
    context_object_name="order"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user)
        return res


@method_decorator(dec,name="dispatch")
class  Ordercancel(View):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        order=Orders.objects.get(id=id)
        order.order_status="Cancelled"
        order.save()
        #mail service
        to_mail=request.user.email
        msg=f"Order for the product {order.product.title} is cancelled successfully!! Check your ecommerce account for more details!"
        from_mail="ayishanasrin468@gmail.com"
        subject="Order Cancellation Configuration"
        send_mail(subject,msg,from_mail,[to_mail])
        return redirect('order')
    


