from django.shortcuts import render

from .forms import SignUpForm
from .models import SignUp
# Create your views here.
def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)

	context = {
	"title": title,
	"form": form
	}

	if form.is_valid():

		instance = form.save(commit = False)


		roll_no = form.cleaned_data.get("roll_no")
		first_name = form.cleaned_data.get("first_name")
		last_name = form.cleaned_data.get("last_name")
		instance.save()


		context = {
		"title": "Success!",
		}



	return render(request,"home.html", context)

def list(request):
	sign_ups = SignUp.objects.all()
	context = {"users":sign_ups.order_by('first_name')}
	return render(request, "list.html", context)