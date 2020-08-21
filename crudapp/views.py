from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from .filters import CustomerFilter
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from . import filters

def sample(request):
    return render(request,'sample.html')



def index(request):
    user_list = Customer.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user_list.html', { 'users': users })


def display(request):
    name = Customer.objects.all().order_by('name')
    phone = Customer.objects.all().order_by('phone')
    email = Customer.objects.all().order_by('email')
    context={'name':name,'phone':phone,'email':email}
    return render(request,'main.html',context)

def create(request):
    form=CustomerForm
    if request.method=='POST':
        form=CustomerForm(request.POST)
        form.save()
        return redirect('read')
    context={'form':form}
    return render(request,'customer.html',context)

def home(request):
    return render(request,'home.html')

def read(request):

    form = CustomerForm
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        form.save()
        return redirect('read')
    context = {'form': form}


    user_list = Customer.objects.all().order_by('name')
    page = request.GET.get('page', 1)
    filtered_qs = filters.CustomerFilter( request.GET,queryset=Customer.objects.all().order_by('name')).qs
    paginator = Paginator(filtered_qs, 5)

   # paginator = Paginator(user_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    name= Customer.objects.all().order_by('name')
    phone = Customer.objects.all().order_by('phone')
    email = Customer.objects.all().order_by('email')

    name = Customer.objects.all().order_by('name')
    phone = Customer.objects.all().order_by('phone')
    email = Customer.objects.all().order_by('email')
    context = {'name': name, 'phone': phone, 'email': email}
    #return render(request, 'main.html', context)

    customer = Customer.objects.all()
    myfilter=CustomerFilter(request.GET,queryset=customer)
    customer=myfilter.qs
    context = {'customer': customer,'myfilter':myfilter,'name':name,'phone':phone,'email':email,'users': users,'form':form}
    return render(request,"display.html", context)


def update(request):
    if request.POST:
        if "_update" in request.POST:
            pk=request.POST.get('id')
            customer=Customer.objects.get(id=pk)
            customer.name = request.POST.get('name')
            customer.email = request.POST.get('email')
            customer.phone = request.POST.get('phone')
            customer.save()
        elif "_delete" in request.POST:
            pk = request.POST.get('id')
            customer = Customer.objects.get(id=pk)
            customer.delete()
    return redirect('/')

    #customer.phone  = request.POST.get['phone']
    #customer.email = request.POST.get['email']
    #customer.save()



    # form=CustomerForm(instance=customer)
    #if request.method == 'POST':
    #form = CustomerForm(request.GET,instance=customer)
    #form.save()
    #return redirect('read')

    #context = {'form': form}
    #return render(request, 'customer.html', context)


def delete(request,pk):
    customer=Customer.objects.get(id=pk)
    customer.delete()
    return redirect('/')


   # context = {'form': customer}
   # return render(request, 'delete.html', context)

