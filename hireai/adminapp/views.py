from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import AdminSignUpForm, AdminSignInForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from llm.llm_chains import get_job_summary
from .forms import CompanyProfileForm,JobPostingForm
from .models import CompanyProfile,JobPosting
# Create your views here.


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    try:

        company_profile = CompanyProfile.objects.get(user=request.user)
        jobs = JobPosting.objects.filter(created_by=request.user)

        return render(request, 'adminapp/admin_dashboard.html',{'jobs':jobs,'company_profile':company_profile})

    except:
        return redirect('create_company_profile')

def admin_sign_up(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sign_in')
    else:
        form = AdminSignUpForm()
    return render(request, 'adminapp/admin-sign-up.html', {'form': form})

def admin_sign_in(request):
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')  # Redirect to admin dashboard
    else:
        form = AdminSignInForm()
    return render(request, 'adminapp/admin-sign-in.html', {'form': form})


@login_required
def create_company_profile(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            company_profile = form.save(commit=False)
            company_profile.user = request.user
            company_profile.save()
            return redirect('admin_dashboard')  
    else:
        form = CompanyProfileForm()

    return render(request, 'adminapp/create_company_profile.html', {'form': form})

def edit_company_profile(request,id):
    company_profile = CompanyProfile.objects.get(id=id)
    if request.method =='POST':
        form = CompanyProfileForm(request.POST, instance=company_profile)
        if form.is_valid():
            form.save()
            return redirect('company_profile')
    else:
        form = CompanyProfileForm(instance=company_profile)
    return render(request,'adminapp/edit_company_profile.html',{'form':form})
        


def company_profile(request):
    try:
        company = CompanyProfile.objects.get(user=request.user)
        print(company)
        return render(request,'adminapp/company_profile.html',{'company':company})
    except:
        return redirect('create_company_profile')


# Dummy ML model function to generate summary
def generate_summary(job_description):
    # Replace this with your actual ML model logic
    return "Generated summary based on job description"

def job_post(request):
    return render(request,'adminapp/job-post.html')


@login_required
def create_job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)
            job_posting.created_by = request.user
            job_posting.company_profile = CompanyProfile.objects.get(user=request.user)
            job_posting.summary = get_job_summary(job_posting.job_description,job_posting.responsibilities,job_posting.requirements)
            job_posting.save()
            return redirect('admin_dashboard')  # Redirect to a view that lists job postings
    else:
        form = JobPostingForm()
    return render(request, 'adminapp/create-job-posting.html', {'form': form})


def edit_job_posting(request,job_id):
    job = JobPosting.objects.get(id=job_id)
    print(job)
    if request.method == 'POST':
        form = JobPostingForm(request.POST,instance=job)
        if form.is_valid():
            job_posting = form.save(commit=False)
            job_posting.summary = get_job_summary(job_posting.job_description,job_posting.responsibilities,job_posting.requirements)
            job_posting.save()
            # form.save()
            return redirect('admin_dashboard')
    else:
        form = JobPostingForm(instance=job)
    return render(request,'adminapp/create-job-posting.html',{'form':form})


def delete_job(request, job_id):
    job = JobPosting.objects.get(id=job_id)
    print("outside working")
    if request.method == 'POST':
        print("working")
        job.delete()
        return redirect('admin_dashboard')  
    return render(request, 'adminapp/delete_job.html', {'job': job})

        

def admin_logout(request):
    """
    View to logout the user.
    """ 
    logout(request)
    return redirect('admin_sign_in')
