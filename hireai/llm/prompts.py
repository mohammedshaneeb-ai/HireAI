## this is template is used for extracting resume content like name, email, phone , education,skills and technologies
template_resume_extraction = '''You are a helpful information extracter.you want to extract from resume_content given below.you want to extract candidate's name,phone,email,education,skills,technologies.
and format the output like below:
name : str,email : str,phone : str,education:str,skills : list of strings ,technologies : list of strings
if you can't extract please don't make your own answer,just blank that field only.the output should be in JSON format

{resume_content}
'''

## this is for job description summarizer
job_summarizer_template = """You are a good Summarizer.i will give you job description,responsibilities and requirements.you want to summarize these:
"job description: {job_description}"
"job responsibilities: {job_responsibilities}"
"job requirements: {job_requirements}"

CONCISE SUMMARY:"""



jd_score_template = """
you are a resume score calculator.I will give you resume content and job descriptoin. based on that please give me a score out of 100.
you want to return the output in JSON format.

Resume Content : {resume_content}
Job Description : {job_description}

I want to get out put in below JSON format:
JSON output : 
    'Score' : score you give,
    'Explanation' : reason why you give this score,
    'Missing': what are missing,
    'Summary': summary


"""