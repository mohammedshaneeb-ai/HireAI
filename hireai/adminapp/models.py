from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator, URLValidator



# Create your models here.
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_details = models.TextField()
    logo = models.ImageField(upload_to='company_logos/')
    company_website = models.URLField()

    def __str__(self):
        return self.company_name


class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    job_description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    summary = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')
    company_profile = models.ForeignKey(CompanyProfile,null=True, blank=True, on_delete=models.CASCADE, related_name='job_postings')

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job_id = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    score_summary = models.TextField(null=True,blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(validators=[EmailValidator])
    experience = models.PositiveIntegerField(help_text="Experience in years")
    age = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(100)])
    resume_link = models.URLField(validators=[URLValidator])
    # skills = models.JSONField(help_text="List of skills")
    # technologies = models.JSONField(help_text="List of technologies")
    skills = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.job_title} - {self.candidate_name}'
    
    
