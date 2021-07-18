"""ecommerceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  
    path('',views.index, name = "home"),
    path('about/',views.about, name = "about"),
    path('cart/',views.cart, name = "cart"),
    path('contact/',views.contact, name = "contact"),
    path('shop/',views.shop, name = "shop"),
    path('faq/',views.faq, name = "faq"),
    path('attorneys/',views.attorneys, name = "attorneys"),
    path('singleattorney/',views.singleattorney, name = "singleattorney"),
    path('productdetail/',views.productdetail, name = "productdetail"),
    # path('myaccount/',views.myaccount),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
