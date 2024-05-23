from django.urls import path
from . import views


urlpatterns = [
    path('/<int:job_id>/',views.chat,name='chat'),

]