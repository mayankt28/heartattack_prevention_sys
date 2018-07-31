from django.shortcuts import render , redirect
from .utils import generate_key
from .forms import ClientForm
from .utils import generate_key , generate_graph
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required

# Create your views here.


# def index(request):
# 	key = generate_key()
# 	return render(request,'sanjivini/index.html',{'key':key})


# @login_required
def index(request):
	return render(request , "sanjivini/index.html",{})
	
	


def graph(request):
	graph = generate_graph()
	return render(request,'sanjivini/graph.html',{'graph':graph})

@login_required
def dashboard(request):
	# pass
	return render(request , 'sanjivini/dashboard.html',{})



def login(request):


	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request,username=username, password=password)
		dj_login(request , user)
		return redirect(dashboard)
	else:
		return render(request,'registration/login.html',{})


def register(request):
	form = ClientForm(request.POST or None)

	if form.is_valid():
		# print('\n\nfdj')
		device_id = form.cleaned_data['device_id']
		obj = form.save(commit=False)
		obj.device_secret = generate_key()
		obj.save()
		User.objects.create_user(username=obj.device_id, password=obj.device_secret, email=None)
		# new_group, created = Group.objects.get_or_create(name=obj.client_name)
		# print(new_group)
		# print(created)
		# print(obj.client_name)
		# print(obj.client_secret)
		# print('')
	
		return render(request , 'sanjivini/info.html',{"name" : obj.device_id,
					"key" : obj.device_secret})

	return render(request,'registration/register.html',{'form':form})