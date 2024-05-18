from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),
    path('about/',views.about, name='about'),
    path('job_list/',views.job_list, name='job_list'),
    path('contact/',views.contact, name='contact'),
    path("create_user_profile/",views.create_user_profile,name='create_user_profile'),
    path("edit_user_profile/<int:user_id>/",views.edit_user_profile, name='edit_user_profile'),
    path('profile_dashboard/', views.profile_dashboard, name='profile_dashboard'),
    path('upload_resume/',views.upload_resume,name="upload_resume"),
    path("job-detail/<int:id>/",views.job_detail, name='job_detail'),

    
    
]