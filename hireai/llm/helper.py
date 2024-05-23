from langchain_community.document_loaders import DirectoryLoader
from langchain_community.utilities.sql_database import SQLDatabase

import json
from django.conf import settings
import os


app_directory = os.path.dirname('../userapp')
resume_path = os.path.join(app_directory, 'resumes')

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')


def get_user_resumes_path():
    user_resumes_folder = 'resumes'
    userapp_path = os.path.join(settings.BASE_DIR, 'userapp', user_resumes_folder)
    return userapp_path


# function for extracting data
def get_resume_content():
    resume_path = get_user_resumes_path()
    print(f"resume path: {resume_path}")

    loader = DirectoryLoader(resume_path)
    docs = loader.load()

    print(f"The len of doc is : {len(docs)}")
    print(docs[0].page_content)
    return docs[0].page_content


# this code for filtering informations from AI JSON output
def parse_data(data_str):
    # Initialize variables to store parsed values
    name = email = phone = education = skills = technologies = None

    try:
        # Convert string to dictionary
        data_dict = json.loads(data_str)

        # Extract values if present
        name = data_dict.get('name')
        email = data_dict.get('email')
        phone = data_dict.get('phone')
        education = data_dict.get('education')
        skills = data_dict.get('skills', [])
        technologies = data_dict.get('technologies', [])

        # Ensure skills and technologies are lists
        if not isinstance(skills, list):
            skills = [skills]
        if not isinstance(technologies, list):
            technologies = [technologies]

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")

    return name, email, phone, education,skills, technologies

