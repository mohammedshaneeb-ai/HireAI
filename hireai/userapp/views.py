from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages 
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from .models import CandidateDetails
from .forms import UserProfileForm
from llm.llm_chains import get_user_detials,get_score
from llm.helper import get_resume_content
import os
import firebase_admin
from firebase_admin import credentials, storage
from django.conf import settings
from datetime import datetime, timedelta
from django.http import JsonResponse
from dotenv import load_dotenv
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from adminapp.models import JobPosting,CompanyProfile

load_dotenv()
app_directory = os.path.dirname(__file__)
resume_path = os.path.join(app_directory, 'resumes')

# Firebase Credentials
Firebase_key = os.environ.get('Firebase_Key')
base_path = settings.BASE_DIR
file_path = os.path.join(base_path, 'hireai-4b1ee-firebase-adminsdk-p5uf7-3fe9a41c73.json',)
cred = credentials.Certificate(file_path)
firebase_admin.initialize_app(cred, {"storageBucket": "hireai-4b1ee.appspot.com"})

# # Create your views here.
# def signup(request):
#     """
#     View for user signup.
#     """
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'userapp/signup.html', {'form': form})



def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after successful registration
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, form.errors)
            return render(request, 'userapp/signup.html', {'form': form})

    else:
        form = SignUpForm()
        return render(request, 'userapp/signup.html', {'form': form})

# def signin(request):
#     """
#     View for user signin.
#     """
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'userapp/signin.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin')
            else:

                login(request, user)
                return redirect('index') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'userapp/signin.html')


@login_required
def index(request):
    # jobs = JobPosting.objects.all()
    jobs = JobPosting.objects.select_related('company_profile').all()

    
    return render(request,'userapp/index.html',{'jobs':jobs})


def about(request):
    return render(request, 'userapp/about.html')


def job_list(request):
    # jobs = Job.objects.all()
    jobs = JobPosting.objects.select_related('company_profile').all()

    return render(request,'userapp/job-list.html',{'jobs':jobs})

def job_detail(request,id):
    job = JobPosting.objects.get(id=id)
    user = request.user
    print(f"user printing from job_datail: {user}")
    c_details = CandidateDetails.objects.get(user=user)
    resume_content = c_details.resume_content
    print(f"resume_content printing from job_datail: {resume_content}")


    responsibilities_list = job.responsibilities.split('\n')
    requirements_list = job.requirements.split('\n')
    job_description = job.job_description
    job_responsibilities = job.responsibilities
    job_requirements = job.requirements

    # Concatenating the strings with their labels
    Combined_Job_Description = (
        f"Job Description:\n {job_description}\n"
        f"Job Responsibilities:\n {job_responsibilities}\n"
        f"Job Requirements:\n {job_requirements}"
    )
    

    
    print(f"JD printing from job_datail: {Combined_Job_Description}")
    score,explanation,missing,summary =get_score(resume_content,Combined_Job_Description)
    score_dic = {
        'score':score,
        'explanation':explanation,
        'missing':missing,
        'summary':summary
    }

    return render(request,'userapp/job-detail.html',{'job':job,'responsibilities_list':responsibilities_list,'requirements_list':requirements_list,'score_dic':score_dic})

def contact(request):
    return render(request, 'userapp/contact.html')


@login_required(login_url="signin")
def create_user_profile(request):
    """
    View to create a user profile.
    """
    # if request.user:
    #     candidate_details = CandidateDetails.objects.get(user=request.user)
    #     if candidate_details:
    #         return redirect('profile_dashboard')
    name = request.session.get('name')
    email = request.session.get('email')
    phone = request.session.get('phone')
    education = request.session.get('education')
    skills = request.session.get('skills')
    technologies = request.session.get('technologies')
    resume_url = request.session.get('resume_url')
    resume_content = request.session.get('resume_content')
    extracted_data = {
        'name':name,
        'email':email,
        'phone':phone,
        'education':education,
        'skills':skills,
        'technologies':technologies

        }
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            experience = request.POST.get('exp')
            age = request.POST.get('age')
            domain = request.POST.get('domain')
            education = request.POST.get('education')
            skills = request.POST.get('skills')
            technologies = request.POST.get('technologies')
            print(f"printing skills in Double quates:\n {skills}")


            
            candidate_details = CandidateDetails(
                name=name,
                email=email,
                phone=phone,
                exp = experience,
                domain = domain,
                age = age,
                education=education,
                skills=skills,
                technologies=technologies,
                resume_link = resume_url,
                user= request.user,
                resume_content = resume_content
            )

            # candidate_details = candidate_details.save(commit=False)
            # candidate_details.user = request.user  # Set the user field
            candidate_details.save()  # Save the instance to the database
            return redirect('profile_dashboard')  # Redirect to a success page
        else:
            print(form.errors)
            print("not valid")
    else:
        form = UserProfileForm()

    return render(request, 'userapp/create_user_profile.html', {'form': form,'extracted_data':extracted_data})

@login_required(login_url="signin")
def edit_user_profile(request, user_id):
    """
    View to edit a user profile.
    """
    user_profile = CandidateDetails.objects.get(candidate_id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_dashboard')  # Redirect to a success page
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'userapp/edit_user_profile.html', {'form': form})

@login_required(login_url="signin")
def profile_dashboard(request):
    if request.user.is_authenticated:
        try:
            candidate_details = CandidateDetails.objects.get(user=request.user)
            # name,email,phone,education,skills,technologies = get_user_detials()
            # print(name,email,phone,education,skills,technologies)
            # extracted_data = {
            #     'name':name,
            #     'email':email,
            #     'phone':phone,
            #     'education':education,
            #     'skills':skills,
            #     'technologies':technologies

            # }
            # Now candidate_details contains the details of the logged-in user
            return render(request, 'userapp/profile_dashboard.html', {'candidate_details': candidate_details})
        except CandidateDetails.DoesNotExist:
            # Handle case where CandidateDetails does not exist for the user
            return render(request, 'userapp/profile_dashboard.html')
        

@csrf_exempt
def upload_resume(request):
    if request.method == 'POST' and request.FILES['file']:
        print("I am  is working from upload_resume view")
        file = request.FILES['file']
        # Save the file to the resume_path
        app_directory = os.path.dirname(__file__)
        resume_path = os.path.join(app_directory, 'resumes')
        if not os.path.exists(resume_path):
            os.makedirs(resume_path)
        with open(os.path.join(resume_path, file.name), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Upload the file to Firebase
        firebase_storage = storage.bucket()
        blob = firebase_storage.blob(file.name)
        blob.upload_from_filename(os.path.join(resume_path, file.name))
        
        # Generate download link
        # blob.make_public()
        # download_link = blob.public_url

        expiration = datetime.utcnow() + timedelta(days=365)

        # Get the download URL (link) of the uploaded file
        download_url = blob.generate_signed_url(expiration)
        print(download_url)

        long_url = download_url
        api_url = f'http://tinyurl.com/api-create.php?url={long_url}&apikey={Firebase_key}'
        response = requests.get(api_url)
        short_url = response.text
        print(short_url)

        resume_content,name,email,phone,education,skills,technologies = get_user_detials()
        print(resume_content,name,email,phone,education,skills,technologies)
        
        # Delete the file from resume_path
        os.remove(os.path.join(resume_path, file.name))

        # converting skills and technologies to double quated list
        skills = list(set(skills))
        technologies = list(set(technologies))

        skills = json.dumps(skills)
        technologies = json.dumps(technologies)


        # adding variables to session
        request.session['name'] = name
        request.session['email'] = email
        request.session['phone'] = phone
        request.session['education'] = education
        request.session['skills'] = skills
        request.session['technologies'] = technologies
        request.session['resume_url'] = short_url
        request.session['resume_content'] = resume_content
        
        return JsonResponse({'success': True,  'download_link': download_url})
        
    else:
        return JsonResponse({'success': False, 'error': 'No file provided'})




def user_logout(request):
    """
    View to logout the user.
    """ 
    logout(request)
    return redirect('signin')
