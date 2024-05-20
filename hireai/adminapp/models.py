from django.db import models

from django.contrib.auth.models import User


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
