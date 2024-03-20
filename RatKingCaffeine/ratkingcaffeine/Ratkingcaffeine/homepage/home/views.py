from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect


from . import models
from . import forms

##@login_required
##def index(request):
def index(request, page = 0):

	current_user = request.user
	#return HttpResponse("CINS465 Hello world. your at home")
	page_list = list(range(page*10, page*10 + 10, 1))
	context ={

		'current_user': current_user,
		'title': 'CINS465',
		'msg': 'Hello World',
		'page_list': page_list,
		'prev_page': page - 1,
		'next_page': page + 1,
	}
	return render(request, "index.html",context=context)
def comments(request):
	if request.method == "POST":
		c_form = forms.usercommentsForm(request.POST)
		if c_form.is_valid():
			c_form.save()
			c_form = forms.usercommentsForm()

	else:
		c_form = forms.usercommentsForm()

	
	c_form = forms.usercommentsForm()
	comment_list = models.usercomments.objects.all()
	context = {
		'title': 'Comment Section',
		'c_form': c_form,
		'comment_list': comment_list,

	}
	return render(request, "comments.html", context=context)
def register(request):
	if request.method == "POST":
		form = forms.RegistrationForm(request.POST)
		if form.is_valid():
			form.save(request)
			return redirect('/login/')
	else:
		form = forms.RegistrationForm(request.POST)
	context = {
	"form": form

	}
	return render(request,"registration/register.html", context=context)
def comment_json(request):
	comment_list = models.usercomments.objects.all()
	c_dictionary ={}
	c_dictionary["comments"]=[]
	for c in comment_list:
		temp_c ={}
		temp_c["comment_test"]= c.commenttext
		temp_c["pub_date"] = c.thedate
		acommenttext = models.usercomments.objects.filter(comment = c)
		temp_c["comments"] = acommenttext
		c_dictionary["comments"] +=[temp_c]

	return JsonResponse(comment_list)

	return render(request,"registration/register.html", context=context)
##def comment_json(request):
def logout_user(request):
	logout(request)
	return redirect("/login/")

def customer_service(request):
	context = {
			'title': 'Customer Service',
	}
	return render(request,"CoffeeDirectory/customer_service.html", context=context)

def home(request):
	context = {
			'title': 'Home',
	}
	return render(request,"CoffeeDirectory/home.html", context=context)
	
def coffee(request):
        product_list = models.products.objects.all()
        context = {
                        'product_list': product_list,
                        'title': 'Coffee',
        }
        return render(request,"CoffeeDirectory/coffee.html", context=context)

def Apperal(request):
	context = {
			'title': 'Apperal',
	}
	return render(request,"CoffeeDirectory/Apparel.html", context=context)
def utilities(request):
	context = {
			'title': 'utilities',
	}
	return render(request,"CoffeeDirectory/utilities.html", context=context)
def about(request):
	context = {
			'title': 'About',
	}
	return render(request,"CoffeeDirectory/About.html", context=context)
def profile(request):
	cur_user = request.user    
	context = {
                        'cur_user': cur_user,
			'title': 'Profile',
		    
	}
	return render(request,"CoffeeDirectory/profile.html", context=context)

def profile_edit(request):
        if request.method == "POST":
            info_form = forms.userinformation(request.POST)
            if info_form.is_valid() and request.user.is_authenticated:
                info_form.save(request)
                return redirect("/profile/")
        else:
            info_form = forms.userinformation()
        context = {
                'title': 'edit Profile',
                'info_form':info_form,
	}
        return render(request,"CoffeeDirectory/profile_edit.html", context=context)

def service(request, room_name):
    return render(request, "CoffeeDirectory/service.html", {"room_name": room_name})
