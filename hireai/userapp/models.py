from django.db import models

# Create your models here.

class Candidate(models.Model):
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
    candidate_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()
    domain = models.CharField(max_length=100)
    skills = models.JSONField()  # List of strings
    technologies = models.JSONField()  # List of strings
    resume_link = models.URLField()

    def __str__(self):
        return self.name
    
