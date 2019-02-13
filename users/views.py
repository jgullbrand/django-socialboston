from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm

def register(request):
	if request.method == "POST":
		form = UserRegistration(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'Account created for {username}. Log In here!')
			return redirect("homepage")
	else:
		form = UserRegistration()	

	context = {"form": form}
	return render(request, "users/register.html", context)


def profile(request):
	if request.method == "POST":
		u_update_form = UserUpdateForm(request.POST, instance=request.user)
		p_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_update_form.is_valid() and p_update_form.is_valid():
			u_update_form.save()
			p_update_form.save()
			messages.success(request, f'Your account information has been updated!')
			return redirect("profile")
	else:
		u_update_form = UserUpdateForm(instance=request.user)
		p_update_form = ProfileUpdateForm(instance=request.user.profile)


	context = {
		"u_update_form": u_update_form, 
		"p_update_form": p_update_form,
	}
	return render(request, "users/profile.html", context)

