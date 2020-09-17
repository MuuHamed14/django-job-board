from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserForm, ProfileForm
from .models import Profile
from django.urls import reverse


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/accounts/profile')
        else:
            form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    my_profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'my_profile': my_profile})


def profile_edit(request):
    my_profile = Profile.objects.get(user=request.user)
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=my_profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=my_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form1 = profile_form.save(commit=False)
            profile_form1.user = request.user
            profile_form1.save()
            return redirect(reverse('accounts:profile'))
        else:
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=my_profile)

    return render(request, 'accounts/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})
