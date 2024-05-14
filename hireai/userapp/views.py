from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.auth import login, authenticate
from .models import CandidateDetails
from .forms import UserProfileForm


# Create your views here.
def signup(request):
    """
    View for user signup.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'userapp/signup.html', {'form': form})


def signin(request):
    """
    View for user signin.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'userapp/signin.html', {'form': form})

@login_required
def index(request):
    candidates = CandidateDetails.objects.all()
    # print(candidates)
    return render(request,'userapp/index.html',{'candidates':candidates})

@login_required(login_url="signin")
def dashboard(request):
    """
    View for the user dashboard.
    If user profile exists, display user details and option to edit profile.
    If user profile doesn't exist, display option to create profile.
    """
    # try:
    #     print(request.user.username)
    #     user_profile = user.objects.get(candidate_id=request.user.candidate_id)
    #     has_profile = True
    # except UserProfile.DoesNotExist:
    #     user_profile = None
    #     has_profile = False

    # if has_profile:
    print(request.user)
    return render(request, 'userapp/dashboard.html')
    # else:
    #     return redirect('create_user_profile')

@login_required(login_url="signin")
def create_user_profile(request):
    """
    View to create a user profile.
    """
    # if request.user:
    #     candidate_details = CandidateDetails.objects.get(user=request.user)
    #     if candidate_details:
    #         return redirect('profile_dashboard')
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            candidate_details = form.save(commit=False)
            candidate_details.user = request.user  # Set the user field
            candidate_details.save()  # Save the instance to the database
            return redirect('profile_dashboard')  # Redirect to a success page
        else:
            print("not valid")
    else:
        form = UserProfileForm()
    return render(request, 'userapp/create_user_profile.html', {'form': form})

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
            # Now candidate_details contains the details of the logged-in user
            return render(request, 'userapp/profile_dashboard.html', {'candidate_details': candidate_details})
        except CandidateDetails.DoesNotExist:
            # Handle case where CandidateDetails does not exist for the user
            return render(request, 'userapp/profile_dashboard.html')


def user_logout(request):
    """
    View to logout the user.
    """ 
    logout(request)
    return redirect('signin')
