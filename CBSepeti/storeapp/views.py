from django.shortcuts import render, redirect
from . import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def mainpage(request):
    all_data = models.Products.objects.all()
    all_dictionary = {"Products":all_data}
    if request.POST:

        product_id = request.POST["product"]
        customer_name = request.user
        price = request.POST["price"]

        order_obj = models.Orders(Product_ID=models.Products(id=product_id),Customer_Name=customer_name,Price=price)
        order_obj.save()
    
        return(redirect(reverse("storeapp:orders")))
    else:
        return render(request, "storeapp/main.html", context=all_dictionary)

def men(request):

    men_data = models.Products.objects.filter(Category_ID="1").all()
    men_dictionary = {"Products":men_data}
    if request.POST:

        product_id = request.POST["product"]
        customer_name = request.user
        price = request.POST["price"]

        order_obj = models.Orders(Product_ID=models.Products(id=product_id),Customer_Name=customer_name,Price=price)
        order_obj.save()
    
        return(redirect(reverse("storeapp:orders")))
    else:
        return render(request, "storeapp/men.html", context=men_dictionary)

def women(request):

    women_data = models.Products.objects.filter(Category_ID="2").all()
    women_dictionary = {"Products":women_data}
    if request.POST:

        product_id = request.POST["product"]
        customer_name = request.user
        price = request.POST["price"]

        order_obj = models.Orders(Product_ID=models.Products(id=product_id),Customer_Name=customer_name,Price=price)
        order_obj.save()
    
        return(redirect(reverse("storeapp:orders")))
    else:
        return render(request, "storeapp/women.html", context=women_dictionary)

def orders(request):
    all_data = models.Orders.objects.filter(Customer_Name=request.user).all()
    all_dictionary = {"Orders":all_data}
    return render(request, "storeapp/orders.html", context=all_dictionary)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"