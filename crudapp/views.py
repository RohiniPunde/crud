from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from .filters import CustomerFilter
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer

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
    return render(request,'main.html')

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
    customer = Customer.objects.all()
    #delivered = orders.filter(status='Delivered').count()
    myfilter=CustomerFilter(request.GET,queryset=customer)
    customer=myfilter.qs
    context = {'customer': customer,'myfilter':myfilter}
    return render(request,"display.html", context)

def update(request,pk):
    customer=Customer.objects.get(id=pk)
    form=CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        form.save()
        return redirect('read')
    context = {'form': form}
    return render(request, 'customer.html', context)


def delete(request,pk):
    customer=Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('read')
    context = {'form': customer}
    return render(request, 'delete.html', context)

