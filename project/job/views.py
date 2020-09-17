from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


def job_lists(request):
    job_list = Job.objects.all()
    my_filter = JobFilter(request.GET, queryset=job_list)
    job_list = my_filter.qs
    paginator = Paginator(job_list, 2)
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)
    return render(request, 'job_list.html', {'jobs': job_list, 'my_filter': my_filter})


@login_required(login_url='login')
def job_details(request, slug):
    job_detail = Job.objects.get(slug=slug)
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
            return redirect(reverse('job:job_list'))
        else:
            form = ApplyForm()
    return render(request, 'job_detail.html', {'job_detail': job_detail, 'form': form})


def like_or_unlike(request,slug):
    job_detail = Job.objects.get(slug=slug)
    if request.user in job_detail.like.all():
        job_detail.like.remove(request.user)
    else:
        job_detail.like.add(request.user)
    return redirect(reverse('job:user_favourites'))


def user_favourite(request):
    user_favourites = Job.objects.filter(like=request.user)
    return render(request,'user_favourites.html',{'user_favourites':user_favourites})


@login_required(login_url='login')
def add_job(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('job:job_list'))
        else:
            form = JobForm()
    return render(request, 'add_job.html', {'form': form})
