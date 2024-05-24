from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import AdminSignUpForm, AdminSignInForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages 

from llm.llm_chains import get_job_summary
from .forms import CompanyProfileForm,JobPostingForm
from .models import CompanyProfile,JobPosting
# Create your views here.


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    """
    Display the admin dashboard for the logged-in staff user.

    This view retrieves the company profile and job postings for the 
    logged-in user and renders the admin dashboard page. If the company 
    profile does not exist, the user is redirected to the profile 
    creation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered admin dashboard page with job postings 
        and company profile.
        HttpResponseRedirect: Redirects to the company profile creation 
        page if the profile does not exist.
    """
    try:

        company_profile = CompanyProfile.objects.get(user=request.user)
        jobs = JobPosting.objects.filter(created_by=request.user)

        return render(request, 'adminapp/admin_dashboard.html',{'jobs':jobs,'company_profile':company_profile})

    except:
        return redirect('create_company_profile')

def admin_sign_up(request):
    """
    Handle the admin sign-up process.

    This view handles the submission of the admin sign-up form. If the 
    request method is POST and the form is valid, it saves the form data 
    and redirects to the admin sign-in page. If the form is invalid, it 
    returns the form with errors. For GET requests, it displays the 
    empty sign-up form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered sign-up page with the form.
        HttpResponseRedirect: Redirects to the admin sign-in page upon 
        successful sign-up.
    """
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sign_in')
        else:
            messages.error(request, form.errors)
            return render(request, 'userapp/signup.html', {'form': form})

    else:
        form = AdminSignUpForm()
    return render(request, 'adminapp/admin-sign-up.html', {'form': form})

def admin_sign_in(request):
    """
    Handle the admin sign-in process.

    This view processes the admin sign-in form. For POST requests, it 
    authenticates the user based on the provided credentials and logs in 
    the user if they are staff. If authentication fails, it displays an 
    error message. For GET requests, it displays the empty sign-in form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered sign-in page with the form.
        HttpResponseRedirect: Redirects to the admin dashboard upon 
        successful sign-in.
    """
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
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AdminSignInForm()
    return render(request, 'adminapp/admin-sign-in.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def create_company_profile(request):
    """
    Handle the creation of a company profile by an admin user.

    This view processes the company profile creation form. For POST 
    requests, it validates the form data, associates the profile with 
    the current user, and saves it. Upon successful creation, it 
    redirects the user to the admin dashboard. For GET requests, it 
    displays the empty company profile creation form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered company profile creation page with the 
        form.
        HttpResponseRedirect: Redirects to the admin dashboard upon 
        successful profile creation.
    """
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

@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_company_profile(request,id):
    """
    Handle the editing of a company profile by an admin user.

    This view processes the company profile editing form. It retrieves 
    the company profile by the given ID. For POST requests, it updates 
    the profile with the submitted data if the form is valid and then 
    redirects to the company profile page. For GET requests, it displays 
    the form populated with the current profile data.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the company profile to be edited.

    Returns:
        HttpResponse: The rendered company profile editing page with the 
        form.
        HttpResponseRedirect: Redirects to the company profile page upon 
        successful profile update.
    """
    company_profile = CompanyProfile.objects.get(id=id)
    if request.method =='POST':
        form = CompanyProfileForm(request.POST,request.FILES, instance=company_profile)
        print(f"Form : {form}")

        if form.is_valid():
            form.save()
            return redirect('company_profile')
    else:
        form = CompanyProfileForm(instance=company_profile)
    return render(request,'adminapp/edit_company_profile.html',{'form':form})
        


@login_required
@user_passes_test(lambda u: u.is_staff)
def company_profile(request):
    """
    Display the company profile for the logged-in staff user.

    This view retrieves the company profile associated with the logged-in 
    user and renders the company profile page. If the profile does not 
    exist, the user is redirected to the profile creation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered company profile page with the company 
        profile data.
        HttpResponseRedirect: Redirects to the company profile creation 
        page if the profile does not exist.
    """
    try:
        company = CompanyProfile.objects.get(user=request.user)
        print(company)
        return render(request,'adminapp/company_profile.html',{'company':company})
    except:
        return redirect('create_company_profile')


@login_required
@user_passes_test(lambda u: u.is_staff)
def create_job_posting(request):
    """
    Handle the creation of a job posting by a staff user.

    This view processes the job posting creation form. For POST requests,
    it validates the form data, associates the job posting with the current
    user and their company profile, generates a job summary, and saves the
    job posting. Upon successful creation, it redirects the user to the
    admin dashboard. For GET requests, it displays the empty job posting
    creation form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered job posting creation page with the form.
        HttpResponseRedirect: Redirects to the admin dashboard upon
        successful job posting creation.
    """
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


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_job_posting(request,job_id):
    """
    Handle the editing of a job posting by a staff user.

    This view processes the job posting editing form. It retrieves the
    job posting by the given ID. For POST requests, it updates the job
    posting with the submitted data if the form is valid and then redirects
    to the admin dashboard. For GET requests, it displays the form
    populated with the current job posting data.

    Args:
        request (HttpRequest): The HTTP request object.
        job_id (int): The ID of the job posting to be edited.

    Returns:
        HttpResponse: The rendered job posting editing page with the form.
        HttpResponseRedirect: Redirects to the admin dashboard upon
        successful job posting update.
    """
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


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_job(request, job_id):
    """
    Handle the deletion of a job posting by a staff user.

    This view processes the deletion of a job posting. It retrieves the
    job posting by the given ID. For POST requests, it deletes the job
    posting and redirects to the admin dashboard. For GET requests, it
    displays the confirmation page for deleting the job posting.

    Args:
        request (HttpRequest): The HTTP request object.
        job_id (int): The ID of the job posting to be deleted.

    Returns:
        HttpResponse: The rendered confirmation page for deleting the job
        posting.
        HttpResponseRedirect: Redirects to the admin dashboard upon
        successful deletion of the job posting.
    """
    job = JobPosting.objects.get(id=job_id)
    print("outside working")
    if request.method == 'POST':
        print("working")
        job.delete()
        return redirect('admin_dashboard')  
    return render(request, 'adminapp/delete_job.html', {'job': job})

        

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_logout(request):
    """
    Log out the admin user.

    This view logs out the currently logged-in admin user and redirects
    to the admin sign-in page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the admin sign-in page after
        logging out the user.
    """
    logout(request)
    return redirect('admin_sign_in')
