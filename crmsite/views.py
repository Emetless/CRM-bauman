from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from crmsite.forms import *
from crmsite.models import *


def index(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite//index/index.html')
    else:
        return render(request, 'crmsite/index/index.html', {'username': auth.get_user(request)})


def login(request):
    args = {}
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "not found"
            return render(request, 'crmsite/login.html', args)
    else:
        return render(request, 'crmsite/login.html', args)


def register(request):
    args = {}
    args['form'] = UserSignUpForm
    if request.POST:
        newuser_form = UserSignUpForm(request.POST)
        if request.POST['password'] != request.POST['password_confirmation']:
            return redirect('/register/')
        elif newuser_form.is_valid():
            newuser = User.objects.create(username=request.POST['username'],
                                          email=request.POST['email'],
                                          first_name=request.POST['first_name'],
                                          last_name=request.POST['last_name'],
                                          caf=request.POST['caf'],
                                          phoneNumber=request.POST['phoneNumber'],
                                          position=request.POST['position'],
                                          commentForAdmin=request.POST['commentForAdmin']
                                          )
            newuser.set_password(request.POST['password_confirmation'])
            newuser.save()
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'crmsite/register.html', args)


def profile(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    else:
        return render(request, 'crmsite/profile.html', {'user': user, 'username': auth.get_user(request)})


def logout(request):
    auth.logout(request)
    return redirect('/')


def createOrder(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and user.isAuthor == True:
        args = {}
        args['form'] = NewOrderForm
        if request.POST:
            neworeder_form = NewOrderForm(request.POST,  request.FILES)
            if neworeder_form.is_valid():
                newOrder = Orders.objects.create(
                    nameJob=request.POST['namejob'],
                    annotation=request.POST['annotation'],
                    typeOfWork=request.POST['typeOfWork'],
                    keyWords=request.POST['keyWords'],
                    isAnalyst=request.POST['isAnalyst'],
                    isConsult=request.POST['isConsult'],
                    isTranslator=request.POST['isTranslator'],
                    isEditor=request.POST['isEditor'],
                    Comment=request.POST['Comment'],
                    BlackFile=request.FILES['BlackFile']
                )
                newOrder.save()
                return redirect('/orders')
        else:
            args['form'] = NewOrderForm
        return render(request, 'crmsite/neworder.html', args)
    else:
        return render(request, 'crmsite/nonpermited.html')
