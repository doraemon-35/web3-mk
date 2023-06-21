from django.shortcuts import render
from home import models as mo
from .models import all_pro_list

# Create your views here.

def product_list(request):
    
    all_pro = all_pro_list.objects.all()

    f_pro = mo.featured_product.objects.all()
    l_pro = mo.leatest_product.objects.all()


    return render(request, 'product_list.html', {'t_1':f_pro,'t_2':l_pro,'t_3':all_pro})


def product_list_log(request, uname):
    
    all_pro = all_pro_list.objects.all()

    f_pro = mo.featured_product.objects.all()
    l_pro = mo.leatest_product.objects.all()

    id_ = mo.register.objects.filter(username=uname)
    for i in id_:
        uname = i.username


    return render(request, 'product_list.html', {'t_1':f_pro,'t_2':l_pro,'t_3':all_pro,'uname':uname})


# ------------------------------


def product_detail(request, id):

    respo =  all_pro_list.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})


def log_product_detail(request, id, uname):

    respo =  all_pro_list.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})


def add_to_cart(request, id, uname):

    ms =  mo.register.objects.create()

    return render(request, 'cart.html',{'uname':uname})


# ------------------------------


def f_detail(request, id):

    respo = mo.featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})


def log_f_detail(request, id, uname):

    respo = mo.featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})


# ------------------------------


def l_detail(request, id):

    respo =  mo.leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})


def log_l_detail(request, id, uname):

    respo =  mo.leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})