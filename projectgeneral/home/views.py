from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about-us.html")

def cart(request):
    return render(request,"cart.html")

def contact(request):
    return render(request,"contact.html")

def shop(request):
    return render(request,"shop.html")

def faq(request):
    return render(request,"faq.html")

def productdetail(request):
    return render(request,"product-details.html")

# def myaccount(request):
#     return render(request,"my-account.html")

def attorneys(request):
    return render(request,"attorneys.html")


def singleattorney(request):
    return render(request,"single-attorney.html")