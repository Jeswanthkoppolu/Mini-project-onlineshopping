"""
URL configuration for OES project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from app.views import (
    Admin_Base,Admin_Dashboard,Transactions,Products,AdminLogin,Customer_Login,Update_Delete,Customer_Dashboard,add_to_cart,
    Cart_Item,Delete_Item,Payment_Details,Order_Detail,Customer_Details, Customer_Register,sessionlogout,adminlogout,Otp_Verification,
    Update_Cart_Quantity)

from OES import settings

from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Customer_Login,name="Customer_Login"),
    path('Admin_Base',Admin_Base,name="Admin_Base"),
    path('Admin_Dashboard',Admin_Dashboard,name="Admin_Dashboard"),
    path('Transactions',Transactions,name="Transactions"),
    path('Products',Products,name="Products"),
    path('AdminLogin',AdminLogin,name="AdminLogin"),
    path('Update_Delete',Update_Delete,name='Update_Delete'),
    path('Customer_Dashboard',Customer_Dashboard,name='Customer_Dashboard'),
    path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart'),
    path('Cart_Item',Cart_Item,name='Cart_Item'),
    path('Delete_Item/<int:id>',Delete_Item,name="Delete_Item"),
    path('Update_Cart_Quantity/<int:id>',Update_Cart_Quantity,name="Update_Cart_Quantity"),
    path('Payment_Details/<int:id>',Payment_Details,name='Payment_Details'),
    path('Order_Detail',Order_Detail,name='Order_Detail'),
    path('Customer_Details',Customer_Details,name='Customer_Details'),
    path('Customer_Register',Customer_Register,name='Customer_Register'),
    path('sessionlogout',sessionlogout,name="sessionlogout"),
    path('adminlogout',adminlogout,name='adminlogout'),
    path('otp',Otp_Verification,name="OTP")

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

