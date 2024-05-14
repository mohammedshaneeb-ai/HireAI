from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("create_user_profile/",views.create_user_profile,name='create_user_profile'),
    path("edit_user_profile/<int:user_id>/",views.edit_user_profile, name='edit_user_profile'),
    path('profile_dashboard/', views.profile_dashboard, name='profile_dashboard'),
    
    
]