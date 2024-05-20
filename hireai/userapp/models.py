from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CandidateDetails(models.Model):
    """
    Model to store user information.
    
    Attributes:
        candidate_id (int): The unique identifier for the candidate.
        name (str): The name of the candidate.
        email (str): The email address of the candidate.
        age (int): The age of the candidate.
        exp (int): The experience of the candidate in years.
        domain (str): The domain expertise of the candidate.
        skills (list of str): A list of skills possessed by the candidate.
        technologies (list of str): A list of technologies the candidate is familiar with.
        resume_link (str): The URL to the candidate's resume.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True)  # Optional field
    age = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()
    domain = models.CharField(max_length=100)
    skills = models.JSONField()  # List of strings
    technologies = models.JSONField()  # List of strings
    resume_link = models.URLField()
    resume_content = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    
