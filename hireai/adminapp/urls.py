from django.urls import path
from . import views


urlpatterns = [
    path('',views.admin_dashboard,name='admin_dashboard'),
    path('admin-sign-up/', views.admin_sign_up, name='admin_sign_up'),
    path('admin-sign-in/', views.admin_sign_in, name='admin_sign_in'),
    path('logout-admin/', views.admin_logout, name='logout_admin'),
    path('create-company-profile/', views.create_company_profile, name='create_company_profile'),
    path('company-profile/',views.company_profile,name='company_profile'),
    path("edit-company-profile/<int:id>/",views.edit_company_profile, name='edit_company_profile'),
    path('create-job-posting/',views.create_job_posting,name='create_job_posting'),
    path("edit-job-posting/<int:job_id>/",views.edit_job_posting, name='edit_job_posting'),
    path("delete-job/<int:job_id>/",views.delete_job, name='delete_job'),



]
