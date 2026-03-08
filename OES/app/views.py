from django.shortcuts import render,redirect

# Create your views here.

from .models import Category,Product,Cart,Orders,User_Detail,ProductRating

import random 

from django.http import Http404

from django.contrib import auth

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models import Avg, Count
from django.conf import settings
import os

from django.views.decorators.cache import never_cache




def Admin_Base(req):
    return render(req,'Admin/Admin_Base.html')


def ensure_sample_products():
    target_count = 50
    catalog = [
        ("OnePlus 11R", "Mobiles", "39999", "High performance phone with smooth display and fast charging.", "product_image/OnePlus.jpg"),
        ("iPhone 13", "Mobiles", "59999", "Premium smartphone with great camera and battery backup.", "product_image/Iphone13.jfif"),
        ("Samsung Galaxy S23", "Mobiles", "68999", "Flagship Android phone with bright AMOLED display.", "product_image/Iphone13_BKQZxMk.jfif"),
        ("Nothing Phone 2", "Mobiles", "44999", "Unique transparent design with clean software experience.", "product_image/OnePlus_9OCquRp.jpg"),
        ("Google Pixel 8", "Mobiles", "71999", "Excellent camera and smooth stock Android experience.", "product_image/Iphone13_QUGixgL.jfif"),
        ("Moto Edge 50", "Mobiles", "32999", "Curved display phone with solid daily performance.", "product_image/OnePlus_JOFL9Uk.jpg"),
        ("Dell Inspiron 15", "Laptops", "55999", "Reliable laptop for office and student workflows.", "product_image/Iphone13_2cRKvdI.jfif"),
        ("HP Pavilion 14", "Laptops", "62999", "Portable productivity laptop with sleek metal build.", "product_image/OnePlus_KlmmvEK.jpg"),
        ("Lenovo IdeaPad Slim", "Laptops", "48999", "Lightweight laptop suited for remote work and study.", "product_image/OnePlus_kbDNltR.jpg"),
        ("ASUS Vivobook 15", "Laptops", "51999", "Fast SSD and modern processor for multitasking.", "product_image/OnePlus_jqZXA5F.jpg"),
        ("Acer Aspire 7", "Laptops", "67999", "Powerful laptop for coding, editing, and gaming.", "product_image/OnePlus_znOlBoz.jpg"),
        ("MacBook Air M1", "Laptops", "82999", "Efficient and quiet laptop with excellent battery life.", "product_image/Iphone13_BKQZxMk.jfif"),
        ("Boat Rockerz 450", "Audio", "1499", "Comfortable on-ear headphones with deep bass output.", "product_image/OnePlus.jpg"),
        ("JBL Tune 760NC", "Audio", "5499", "Noise cancelling headphones for focused listening.", "product_image/Iphone13.jfif"),
        ("Sony WH-CH520", "Audio", "4499", "Balanced wireless sound with long battery backup.", "product_image/OnePlus_9OCquRp.jpg"),
        ("Realme Buds Air 5", "Audio", "3699", "True wireless earbuds with strong call clarity.", "product_image/Iphone13_QUGixgL.jfif"),
        ("OnePlus Nord Buds 2", "Audio", "2999", "Compact earbuds with punchy sound profile.", "product_image/OnePlus_JOFL9Uk.jpg"),
        ("Apple AirPods 3", "Audio", "17999", "Premium TWS earbuds with spatial audio support.", "product_image/Iphone13_2cRKvdI.jfif"),
        ("Samsung Galaxy Watch 6", "Wearables", "26999", "Smartwatch with fitness insights and AMOLED display.", "product_image/OnePlus_KlmmvEK.jpg"),
        ("Noise ColorFit Pro 5", "Wearables", "4499", "Affordable smartwatch with health tracking.", "product_image/OnePlus_kbDNltR.jpg"),
        ("Fire-Boltt Visionary", "Wearables", "2999", "Feature-rich smartwatch for daily usage.", "product_image/OnePlus_jqZXA5F.jpg"),
        ("Amazfit Bip 5", "Wearables", "6999", "Large screen smartwatch with GPS tracking.", "product_image/OnePlus_znOlBoz.jpg"),
        ("Mi Smart Band 8", "Wearables", "3499", "Compact fitness band with all-day activity tracking.", "product_image/Iphone13_BKQZxMk.jfif"),
        ("Fitbit Charge 6", "Wearables", "15999", "Advanced fitness tracker with heart-rate analytics.", "product_image/OnePlus_9OCquRp.jpg"),
        ("Logitech MX Master 3S", "Accessories", "8999", "Ergonomic wireless mouse with precision scroll.", "product_image/OnePlus.jpg"),
        ("HP Wireless Keyboard", "Accessories", "1999", "Slim keyboard for productivity and comfort typing.", "product_image/Iphone13.jfif"),
        ("Anker 65W Charger", "Accessories", "3299", "Fast charger for phones, tablets, and laptops.", "product_image/OnePlus_JOFL9Uk.jpg"),
        ("UGREEN USB-C Hub", "Accessories", "2499", "Multiport hub for HDMI, USB, and card reader use.", "product_image/OnePlus_KlmmvEK.jpg"),
        ("Sandisk 128GB Pendrive", "Accessories", "1099", "High-speed storage for files and backups.", "product_image/OnePlus_kbDNltR.jpg"),
        ("Portronics Power Bank 20000mAh", "Accessories", "1799", "Reliable power bank for travel and emergencies.", "product_image/OnePlus_jqZXA5F.jpg"),
        ("Canon EOS 1500D", "Cameras", "41999", "Beginner DSLR with good image quality and controls.", "product_image/OnePlus_znOlBoz.jpg"),
        ("Sony ZV-E10", "Cameras", "64999", "Content creator camera with interchangeable lens.", "product_image/Iphone13_BKQZxMk.jfif"),
        ("GoPro Hero 12", "Cameras", "38999", "Action camera for travel, sports, and vlogging.", "product_image/Iphone13_QUGixgL.jfif"),
        ("DJI Osmo Action 4", "Cameras", "35999", "Rugged action camera with stabilization.", "product_image/Iphone13_2cRKvdI.jfif"),
        ("Instax Mini 12", "Cameras", "6999", "Instant print camera with fun design.", "product_image/OnePlus_9OCquRp.jpg"),
        ("Nikon D7500", "Cameras", "79999", "Advanced DSLR for enthusiasts and professionals.", "product_image/OnePlus.jpg"),
        ("BenQ 24 inch Monitor", "Displays", "12999", "Full HD monitor with eye-care features.", "product_image/Iphone13.jfif"),
        ("LG UltraWide 29", "Displays", "21999", "Ultrawide monitor for productivity and media.", "product_image/OnePlus_JOFL9Uk.jpg"),
        ("Samsung 27 Curved", "Displays", "17999", "Curved display for immersive visual experience.", "product_image/OnePlus_KlmmvEK.jpg"),
        ("Acer Nitro 27", "Displays", "24999", "High refresh monitor for gaming and editing.", "product_image/OnePlus_kbDNltR.jpg"),
        ("ViewSonic VX3211", "Displays", "19999", "Large screen monitor with rich color profile.", "product_image/OnePlus_jqZXA5F.jpg"),
        ("Dell S2421HN", "Displays", "13999", "Minimal bezel monitor for daily office use.", "product_image/OnePlus_znOlBoz.jpg"),
        ("PlayStation 5", "Gaming", "54999", "Next-gen console with ultra-fast game loading.", "product_image/Iphone13_BKQZxMk.jfif"),
        ("Xbox Series X", "Gaming", "52999", "Powerful gaming console with 4K support.", "product_image/Iphone13_QUGixgL.jfif"),
        ("Nintendo Switch OLED", "Gaming", "31999", "Portable gaming console with vibrant display.", "product_image/Iphone13_2cRKvdI.jfif"),
        ("Razer DeathAdder V2", "Gaming", "3999", "Precision gaming mouse with ergonomic shape.", "product_image/OnePlus_9OCquRp.jpg"),
        ("HyperX Cloud Stinger", "Gaming", "3499", "Comfort gaming headset with clear microphone.", "product_image/OnePlus.jpg"),
        ("Redragon K552 Keyboard", "Gaming", "2899", "Mechanical keyboard with tactile key feedback.", "product_image/Iphone13.jfif"),
        ("Seagate 1TB SSD", "Storage", "7499", "Fast external SSD for backup and editing.", "product_image/OnePlus_JOFL9Uk.jpg"),
        ("WD 2TB HDD", "Storage", "5499", "Reliable hard drive for large storage needs.", "product_image/OnePlus_KlmmvEK.jpg"),
        ("Samsung T7 1TB", "Storage", "8999", "Portable SSD with secure and fast transfers.", "product_image/OnePlus_kbDNltR.jpg"),
    ]

    category_image_map = {
        "Mobiles": "product_image/OnePlus.jpg",
        "Laptops": "product_image/laptop.svg",
        "Audio": "product_image/audio.svg",
        "Wearables": "product_image/wearables.svg",
        "Accessories": "product_image/accessories.svg",
        "Cameras": "product_image/cameras.svg",
        "Displays": "product_image/displays.svg",
        "Gaming": "product_image/gaming.svg",
        "Storage": "product_image/storage.svg",
    }
    fallback_image = "product_image/accessories.svg"

    catalog = catalog[:target_count]

    for idx, item in enumerate(catalog, start=1):
        name, category_name, amount, info, image = item
        category_obj, _ = Category.objects.get_or_create(name=category_name)
        product_id = f"PID{10000 + idx}"
        resolved_image = category_image_map.get(category_name, fallback_image)
        if category_name == "Mobiles" and "iphone" in name.lower():
            resolved_image = "product_image/Iphone13.jfif"
        elif category_name == "Mobiles" and "oneplus" in name.lower():
            resolved_image = "product_image/OnePlus.jpg"

        Product.objects.update_or_create(
            P_ID=product_id,
            defaults={
                "P_Name": name,
                "P_Amount": amount,
                "p_Image": resolved_image,
                "P_Info": info,
                "category": category_obj,
            },
        )

    # Remove accidental extra seeded rows beyond target_count.
    Product.objects.filter(P_ID__startswith="PID10", id__in=[
        p.id for p in Product.objects.filter(P_ID__startswith="PID10")
        if p.P_ID and p.P_ID[3:].isdigit() and int(p.P_ID[3:]) > (10000 + target_count)
    ]).delete()

    # Repair missing image references in seeded products and enforce category-aligned image.
    for item in Product.objects.filter(P_ID__startswith="PID10"):
        if item.category and item.category.name != "Mobiles":
            expected = category_image_map.get(item.category.name, fallback_image)
            if str(item.p_Image) != expected:
                item.p_Image = expected
                item.save(update_fields=["p_Image"])
                continue
        image_name = str(item.p_Image) if item.p_Image else ""
        image_path = os.path.join(settings.MEDIA_ROOT, image_name) if image_name else ""
        if image_name and (not os.path.exists(image_path)):
            if item.category and item.category.name == "Mobiles":
                item.p_Image = "product_image/OnePlus.jpg"
            else:
                item.p_Image = category_image_map.get(item.category.name, fallback_image)
            item.save(update_fields=["p_Image"])

def AdminLogin(req):
    if req.method=="POST":
        username=req.POST.get('name')
        password=req.POST.get('password')

        print(username,password)
        check=auth.authenticate(req,username=username,password=password)
        print(check)
        if check!=None:
            auth.login(req,check)
            return redirect('Admin_Dashboard')
    return render(req,'Admin/AdminLogin.html')

@login_required
@never_cache
def Admin_Dashboard(req):
    product_count=Product.objects.all().count()
    order=Orders.objects.all()
    user=User_Detail.objects.all().count()
    Total_revunue=sum(int(i.P_Amount) for i in order)
    print(Total_revunue)
    context={
        'product_count':product_count,
        'Revenue':Total_revunue,
        'user':user
    }
    return render(req,'Admin/Admin_Dashboard.html',context)

@login_required
@never_cache
def Transactions(req):
    Payment_Details=Orders.objects.all()
    context={
        'order':Payment_Details
    }
    return render(req,'Admin/Transactions.html',context)

@login_required
@never_cache
def Products(req):
    if req.method=="POST" and 'create' in req.POST:
        category=req.POST.get("category")
        name=req.POST.get('name')
        amount=req.POST.get('amount')
        image=req.FILES.get('image')
        text=req.POST.get('text')
        print(category,name,amount,image,text)

        product_id="PID"+str(random.randint(9999,99999))
        print(product_id)

        category_obj,create=Category.objects.get_or_create(
            name=category
        )



        Product.objects.create(
                 P_ID=product_id,
                 P_Name=name,
                 P_Amount=amount,
                 p_Image=image,
                 P_Info=text,
                 category=category_obj
        )



    return render(req,'Admin/Products.html')


@login_required
@never_cache
def adminlogout(req):
    auth.logout(req)
    return redirect('AdminLogin')
    



def Customer_Login(req):
    ensure_sample_products()
    featured_products = Product.objects.all()[:12]

    if req.method=="POST" and 'login' in req.POST:
        name=req.POST.get('name')
        password=req.POST.get('password')
        check=User_Detail.objects.filter(U_Name=name,U_Password=password).exists()
        if check:
            data=User_Detail.objects.get(U_Name=name,U_Password=password)
            req.session['customer'] = data.id
            return redirect('Customer_Dashboard')
        messages.error(req, "Invalid username or password.")
        
    return render(req,'Customer/Customer_Login.html', {"featured_products": featured_products, "total_products": Product.objects.count()})


def Otp_Verification(req):
        return redirect('Customer_Login')


@login_required
@never_cache
def Update_Delete(req):
    if req.method=="POST" and 'update' in req.POST:
        product_id=req.POST.get('product_Id')
        name=req.POST.get('name')
        amount=req.POST.get('amount')
        image=req.FILES.get('image')
        text=req.POST.get('text')

        print(image)

        data=Product.objects.get(P_ID=product_id)
        data.P_Name=name if name!='' else data.P_Name
        data.P_Amount=amount if amount!='' else data.P_Amount
        data.p_Image=image if image!=None  else data.p_Image
        data.P_Info=text if text!='' else data.P_Info
        data.save()


    if req.method=="POST" and 'delete' in req.POST:
        product_id=req.POST.get('product_Id')
        Product.objects.get(P_ID=product_id).delete()

    return render(req,'Admin/Update_Delete.html')


def Customer_Dashboard(req):
    if req.session.get('customer')!=None:
        ensure_sample_products()
        Ac_id=req.session.get('customer')
        detail=User_Detail.objects.filter(id=Ac_id)
        if req.method == "POST" and 'rate_product' in req.POST:
            product_id = req.POST.get("product_id")
            rating_value = req.POST.get("rating")
            review = (req.POST.get("review") or "").strip()
            if not product_id or not rating_value:
                messages.error(req, "Rating submission is incomplete.")
                return redirect('Customer_Dashboard')
            try:
                rating_int = int(rating_value)
                if rating_int < 1 or rating_int > 5:
                    raise ValueError
                selected_product = Product.objects.get(id=product_id)
            except (ValueError, Product.DoesNotExist):
                messages.error(req, "Invalid rating request.")
                return redirect('Customer_Dashboard')

            ProductRating.objects.update_or_create(
                User_ID=str(Ac_id),
                product=selected_product,
                defaults={"rating": rating_int, "review": review}
            )
            messages.success(req, "Your rating has been saved.")
            return redirect('Customer_Dashboard')

        product=Product.objects.all().annotate(
            avg_rating=Avg('ratings__rating'),
            rating_count=Count('ratings')
        )
        query = req.GET.get("q", "").strip()
        category = req.GET.get("category", "all").strip().lower()
        sort = req.GET.get("sort", "default").strip().lower()

        if query:
            product = product.filter(Q(P_Name__icontains=query) | Q(P_ID__icontains=query))
        if category and category != "all":
            product = product.filter(category__name__iexact=category)
        if sort == "price_asc":
            product = product.extra(select={'price_int': 'CAST(P_Amount AS UNSIGNED)'}).order_by('price_int')
        elif sort == "price_desc":
            product = product.extra(select={'price_int': 'CAST(P_Amount AS UNSIGNED)'}).order_by('-price_int')

        user_rating_map = {i.product_id: i for i in ProductRating.objects.filter(User_ID=str(Ac_id))}
        product = list(product)
        filtered_product_count = len(product)
        for p in product:
            p.user_rating = user_rating_map.get(p.id)

        cart_items = Cart.objects.select_related('product').filter(User_ID=str(Ac_id))
        order_count = Orders.objects.filter(User_ID=Ac_id).count()
        category_queryset = Category.objects.all()
        context={
         'product':product,
         'detail':detail,
         'cart_items': cart_items[:4],
         'product_count': filtered_product_count,
         'cart_count': cart_items.count(),
         'order_count': order_count,
         'category_count': category_queryset.count(),
         'categories': category_queryset,
         'query': query,
         'selected_category': category,
         'selected_sort': sort,
        }
        return render(req,'Customer/Dashboard.html',context)
    else:
        return redirect('Customer_Login')


def add_to_cart(req,id):
    if req.session.get('customer')!=None:
        Ac_id=req.session.get('customer')
        try:
            product=Product.objects.get(id=id)
        except:
            raise Http404("Product not Found ")
    
        cart_obj,create=Cart.objects.get_or_create(
          User_ID=str(Ac_id),
          product=product,
          defaults={'quantity':1}
        )
        if not create:
            cart_obj.quantity+=1
            cart_obj.save()
            messages.success(req, f"Updated quantity for {product.P_Name}.")
            return redirect('Customer_Dashboard')

        messages.success(req, f"{product.P_Name} added to cart.")
        return redirect('Customer_Dashboard')
   
    else:
        return redirect('Customer_Login')




def Cart_Item(req):
    if req.session.get('customer')!=None:
        Ac_id=req.session.get('customer')
        data=Cart.objects.filter(User_ID=str(Ac_id))
        grand_total=0
        for i in data:
            i.total_amount=int(i.product.P_Amount) * int(i.quantity)
            grand_total+=i.total_amount

        context={
          "product":data,
          "grand_total":grand_total,
        }
        return render(req,'Customer/Carts.html',context)
    else:
        return redirect('Customer_Login')



def Delete_Item(req,id):
    if req.session.get('customer')!=None:
        Ac_id=req.session.get('customer')
        check=Cart.objects.filter(id=id,User_ID=str(Ac_id)).exists()
        if check:
            Cart.objects.get(id=id,User_ID=str(Ac_id)).delete()
            messages.success(req, "Item removed from cart.")
            return redirect('Cart_Item')
        return redirect('Cart_Item')
    else:
        return redirect('Customer_Login')



def Payment_Details(req,id):
    if req.session.get('customer')!=None:
        Ac_id=req.session.get('customer')
        product_detail=Cart.objects.get(id=id,User_ID=str(Ac_id))
        data=product_detail.product

        TID="TID"+str(random.randint(999,9999))

        Total_Amount=int(data.P_Amount) * (product_detail.quantity)

        store=Orders()
        store.TID=TID
        store.User_ID=Ac_id
        store.P_Name=data.P_Name
        store.P_Amount=Total_Amount
        store.P_Image=data.p_Image
        store.save()

        context={
         'Name':data.P_Name,
         'Amount':Total_Amount,

         }


        Cart.objects.get(id=id,User_ID=str(Ac_id)).delete()
        messages.success(req, "Payment successful. Order placed.")

        return render(req,'Customer/Payments.html',context)
    else:
        return redirect('Customer_Login')


def Order_Detail(req):
    if req.session.get('customer')!=None:
        Ac_id=req.session.get('customer')
        print(Ac_id)
        product=Orders.objects.filter(User_ID=Ac_id)
        
        context={
        'product':product
        }
        return render(req,'Customer/Orders.html',context)
    else:
        return redirect('Customer_Login')
   

def Customer_Details(req):
    if req.session.get("customer")!=None:
        Acc_Id=req.session.get('customer')
        details=User_Detail.objects.get(id=Acc_Id)
        print(details)
        if req.method=="POST":
            name=req.POST.get('name')
            password=req.POST.get('password')
            image=req.FILES.get('image')
            email=req.POST.get('email')
            phonenumber=req.POST.get('phonenumber')

            print(name,password,image,email,phonenumber)

            data=details
            data.U_Name=name if name!='' else data.U_Name
            data.U_Password=password if password!='' else data.U_Password
            data.U_Image=image if image!=None else data.U_Image
            data.U_Email=email if email!='' else data.U_Email
            data.U_PoneNumber=phonenumber if phonenumber!='' else data.U_PoneNumber
            data.save()
        context={
              "user":details
        }
        return render(req,'Customer/Customer_detail.html',context)
    
    else:
        return redirect('Customer_Login')


def Customer_Register(req):
    if req.method=="POST" and 'submit' in req.POST:
        name=req.POST.get('name','').strip()
        password=req.POST.get('password','').strip()
        image=req.FILES.get('image')
        email=req.POST.get('email','').strip()
        phonenumber=req.POST.get('phonenumber','').strip()

        if not all([name, password, email, phonenumber]):
            messages.error(req, "Please fill all required fields.")
            return render(req,'Customer/Customer_Register.html')

        if User_Detail.objects.filter(U_Name=name).exists():
            messages.error(req, "Username already exists.")
            return render(req,'Customer/Customer_Register.html')

        if User_Detail.objects.filter(U_Email=email).exists():
            messages.error(req, "Email already registered.")
            return render(req,'Customer/Customer_Register.html')

        UID="UID"+str(random.randint(000,9999))

        data=User_Detail()
        data.UID=UID
        data.U_Name=name
        data.U_Password=password
        data.U_Image=image
        data.U_Email=email
        data.U_PoneNumber=phonenumber
        data.save()
        messages.success(req, "Registration successful. Please login.")
        return redirect('Customer_Login')
    return render(req,'Customer/Customer_Register.html')



def sessionlogout(req):
    if req.session.get('customer')!=None:
        del req.session['customer']
        return redirect('Customer_Login')


def Update_Cart_Quantity(req,id):
    if req.session.get('customer')!=None:
        Ac_id=req.session.get('customer')
        action = req.GET.get('action')
        cart_item = Cart.objects.filter(id=id,User_ID=str(Ac_id)).first()
        if not cart_item:
            messages.error(req, "Cart item not found.")
            return redirect('Cart_Item')

        if action == "inc":
            cart_item.quantity += 1
            cart_item.save()
        elif action == "dec":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                messages.info(req, "Minimum quantity is 1.")
        return redirect('Cart_Item')
    else:
        return redirect('Customer_Login')




    
















