from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .forms import CreateUserForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import donate, info_request as req
from django.forms import inlineformset_factory
from django.contrib.auth import login as auth_login, authenticate,logout
from django.views import View

from .models import *

def home(request):
	return render(request,'home/home.html')

def adminview(request):
	return render(request,'home/adminview.html')

@login_required(login_url="/login")
def find(request):
	return render(request,'home/finddonar.html')


def admin_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer=Customer.objects.filter(username=username,password=password,role='admin')
        if customer:
            return render(request,"home/adminview.html",{'value': username})
        else:
            messages.error(request, 'Username OR password is incorrect')
            return render(request,'home/adminlogin.html')
    else:
        return render(request,'home/adminlogin.html')


@login_required(login_url="/login")
def don(request):
	if request.method == "POST":
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		bloodgroup = request.POST.get("bloodgroup")
		city = request.POST.get("city")
		state = request.POST.get("state")
		user = donate(name=name, phone=phone, bloodgroup=bloodgroup,city=city,state=state)
		user.save()
		return render(request, 'home/home.html')
	else:
		return render(request, 'home/donate.html')



class signup(View):

    def get(self, request):
        return render(request, 'home/signup.html')
    def post(self, request):
        postData = request.POST
        username = postData.get('username')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'username': username,

            'email': email
        }

        error_message = None

        customer = Customer(username=username,email=email, password=password)

        if not username:
            error_message = "user name required"

        elif username:
            if len(username) < 4:
                error_message = "username must be 4 characters long"

        if len(password) < 6:
            error_message = 'Password must be 6 char long'

        if len(email) < 5:
            error_message = 'Email must be 5 char long'

        if customer.isExists():
            error_message = "Email Address already registred"

        # saving
        if not error_message:
            print(username,email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return render(request,'home/home.html',{'value': username})
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'home/signup.html', data)



class login(View):

    return_url = None
    def get(self, request):
        login.return_url = request.GET.get('return_url')
        return render(request , 'home/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_username(username)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if login.return_url:
                    return HttpResponseRedirect(login.return_url)

                else:
                    login.return_url = None
                    return render(request,'home/home.html',{'error1': username})

            else:
                error_message = 'username or Password invalid !!'
        else:
            error_message = 'username or Password invalid !!'

        # print(username, password)
        return render(request, 'home/login.html', {'error': error_message})


def log(request):
	logout(request)
	return redirect('home')

@login_required(login_url="/login")
def request(request):
	if request.method == "POST":
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		bloodgroup = request.POST.get("bloodgroup")
		city = request.POST.get("city")
		state = request.POST.get("state")
		reason = request.POST.get("reason")
		user = info_request(name=name, phone=phone, bloodgroup=bloodgroup,city=city,state=state,reason=reason)
		user.save()
		return render(request, 'home/home.html')
	else:
		return render(request, 'home/request.html')

def view_request(request):
	# view_request = info_request.objects.all()
		entry=Customer.objects.all()
		return render(request,'home/view_request.html',{'entry':entry})
def viewdonar(request):
	# view_request = info_request.objects.all()
		entry=donate.objects.all()
		return render(request,'home/viewdonar.html',{'entry':entry})
def viewreq(request):
	# view_request = info_request.objects.all()
		entry=info_request.objects.all()
		return render(request,'home/requestforblood.html',{'entry':entry})

