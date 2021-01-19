from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F #F() expressions are good for memory
from django.core.mail import send_mail

# Create your views here.
from .forms import UserRegistrationForm, ItemForm
from .models import Items
from .decorators import unauthenticated_user, allowed_users

def home_view(request):
    return render(request, 'accounts/home.html', {})

@login_required(login_url='accounts_app:login')
@allowed_users(allowed_roles=['admin'])
def item_create_view(request):
    form = ItemForm()
    if request.method == 'POST':
        #request.FILES is for file upload
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ItemForm()
            messages.success(request, 'Item added to database!')
    queryset = Items.objects.order_by('-id')
    context = {'form': form, 'object_list': queryset}
    return render(request, 'accounts/admin_panel.html', context)


@login_required(login_url='accounts_app:login')
def item_list(request):
    queryset = Items.objects.all()
    context = {'object_list': queryset}
    return render(request, 'accounts/shop_list.html', context)

def item_delete_view(request, pk):
    obj = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('accounts_app:item_create_view') # ../ goes back a few pages
    context = {'object': obj}
    return render(request, 'accounts/item_delete.html', context)
    # obj.delete()
    # return redirect('accounts:item_create_view')

def item_edit_view(request, pk):
    obj = get_object_or_404(Items, pk=pk)
    form = ItemForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('accounts_app:item_create_view')
    else:
        form = ItemForm(instance=obj)
    context = {'form':form}
    return render(request, 'accounts/item_edit.html', context)
#Function for decrement quantity
# def decrement_quantity(request, pk):
#     decrem = get_object_or_404(Items, pk=pk)
#     decrem.quantity = decrem.quantity - 1
#     decrem.save()
#     return redirect('accounts:item_list')

#Function for decrement quantity with F() expressions
def decrement_quantity(request, pk):
    decr = Items.objects.get(pk=pk)
    decr.quantity = F('quantity') - 1
    decr.save()
    send_mail('subject', 'body of the message', 'sender@example.com', ['dragojlo@net.hr',])
    messages.success(request, 'Message sent! We will contact you as soon as possible!')
    return redirect('accounts_app:item_list')

@unauthenticated_user
def register_view(request):
    form = UserRegistrationForm()
    # Checks when user is authenticated so it can't go to login and register page
    # Instead of this we can use decorator unauthenticated_user so we don't have to write if else in functions tht we need this
    # if request.user.is_authenticated:
    #     return redirect('home')
    #else:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #form = UserRegistrationForm()#vraća čista polja iz forma
            user = form.cleaned_data.get('username') #gets username
            messages.success(request, 'Account was created for ' + user)
            return redirect('accounts_app:login') #naziv za redirect je iz url namea
    context = {'form': form} #hvata sve podatke iz objekta
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def login_view(request):
    # Checks when user is authenticated so it can't go to login and register page
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts_app:item_list')
        else:
            messages.info(request, 'Username or password is incorrect')
    context= {}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts_app:login')
