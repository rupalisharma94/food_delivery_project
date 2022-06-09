from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from foodapp.forms import UserInfo
from foodapp.forms import ImageUpload
from foodapp.models import Image
from foodapp.models import Userdetails
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

#######################################################______ USER ______###################################################

# Views for user.
def index(request):
    return render(request, "index.html")


def header(request):
    return render(request, "header.html")


def about(request):
    return render(request, "about.html")


def feedback(request):
    return render(request, "feedback.html")


def footer(request):
    return render(request, "footer.html")


def secondpage(request):
    return render(request, "second.html")


def home(request):
    return render(request, "home.html")


def menu(request):
    return render(request, "menu.html")


def dishes(request):
    images = Image.objects.all()
    return render(request, "dishes.html", {'images': images})


def cart(request):
    return render(request, "cart.html")


# def login(request):
#     return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def profile(request):
    return render(request, "profile.html")


def staticpage(request):
    return render(request, "staticpage.html")

# _________Register_________


def saveUser(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        # password = request.POST['password']
        user = User.objects.create_user(first_name=fname, last_name=lname,
                                        username=username, email=email, password=password, address=address)
        user.save()
        return HttpResponse('<script> alert("Form submitted successfully") </script>')
    else:
        return HttpResponse('<script> alert("Submission Error...!!!") </script>')


# _________Login__________
# def userlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/afterlogin')
#         else:
#             return redirect('/second')
#     else:
#         return HttpResponse('<script> alert("Submission Error...!!!") </script>')

def userloginf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/afterlogin')
        else:
            messages.error(request, "Invalid Crdentials, Please try again")
            return redirect('/dishes')

    return HttpResponse('<script> alert("Submission Error...!!!") </script>')

def afterlogin(request):
    return render(request, "profile.html")

# _________Logout__________
def logout(request):
    auth.logout(request)
    return redirect('/')


#######################################################______ ADMIN ______###################################################

# Views for admin.

def adminindex(request):
    return render(request, "admin/adminindex.html")


def updatedishes(request):
    return redirect('/showproduct')


def userinfo(request):
    return redirect('/show')


def adddishes(request):
    return render(request, "admin/adddishes.html")

############____ CRUD for ADMIN USERINFO _____#############


def insert(request):
    if request.method == "POST":
        form = UserInfo(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')

            except:
                pass
    else:
        form = UserInfo()
    return render(request, 'register.html', {'form': form})


def show(request):
    userdetails = Userdetails.objects.all()
    return render(request, "admin/userinfo.html", {'userdetails': userdetails})


def edit(request, id):
    userinfo = Userdetails.objects.get(id=id)
    return render(request, 'admin/edit.html', {'userinfo': userinfo})


def update(request, id):
    userinfo = Userdetails.objects.get(id=id)
    form = UserInfo(request.POST, instance=userinfo)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'admin/edit.html', {'userinfo': userinfo})


def destroy(request, id):
    userinfo = Userdetails.objects.get(id=id)
    userinfo.delete()
    return redirect("/show")

##########################################################################################################

# ____Admin Login___


def adminlogin(request):
    return render(request, "admin/adminlogin.html")


def adminloginf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/adminafterlogin')
        else:
            return redirect('/second')
    else:
        return HttpResponse('<script> alert("Submission Error...!!!") </script>')


def adminafterlogin(request):
    return render(request, "admin/adminindex.html")


# Admin Dish insert
def adddish(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = ImageUpload()
    return render(request, 'admin/adddishes.html', {'form': form})


def success(request):
    return render(request, "admin/success.html")


#########################################################################################################

#######################################################################################
def product(request):
    return render(request, "admin/show.html")

#Admin Products CRUD#


def showproduct(request):
    images = Image.objects.all()
    return render(request, "admin/show.html", {'images': images})

def editproduct(request, id):
    dishes = Image.objects.get(id=id)
    return render(request, 'admin/product_edit.html', {'dishes': dishes})

def updateproduct(request, id):
    dishes = Image.objects.get(id=id)
    form = ImageUpload(request.POST, instance=userinfo)
    if form.is_valid():
        form.save()
        return redirect("/showproduct")
    return render(request, 'admin/product_edit.html', {'dishes': dishes})

def destroyproduct(request, id):
    dishes = Image.objects.get(id=id)
    dishes.delete()
    return redirect("/showproduct")


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/afterlogin')
        else:
            return redirect('/second')
    else:
        return HttpResponse('<script> alert("Submission Error...!!!") </script>')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username=username, password=password)
		if user is not None:
			if user.is_active:
				request.session.set_expiry(86400)
				auth.login(request, user)
				return redirect('/afterlogin')
			else:
				return HttpResponse('<script> alert("Logged Out.!!!") </script>')
		else:
			messages.error(request, "Wrong Info")
			return('/second')
	else:
		return HttpResponse('<script> alert("Submission Error...!!!") </script>')
