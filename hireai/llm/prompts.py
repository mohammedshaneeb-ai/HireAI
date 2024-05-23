from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from .examples import examples



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



jd_score_template_1 = """
you are a resume skill calculator.I will give you resume content and job descriptoin. based on that please give me a score out of 100.
if more skills are missing in resume then give less score.
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

jd_score_template2 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Job description and
the missing keywords with high accuracy.
you want to return the output in JSON format.


Resume Content : {resume_content}
Job Description : {job_description}

I want to get out put in below JSON format:
JSON output : 
    'Score' : score you give(int),
    'Explanation' : reason why you give this score(str),
    'Missing': what are missing(in list format),
    'Summary': summary(str)


"""

jd_score_template = """
you are a resume score calculator.I will give you resume content and job descriptoin. based on that please give me a score out of 100.
you want to return the output in JSON format.

You want to follow instructions given below to give score:
    Scoring Criteria:
        A. Skills (70 points)

        Required Skills (20 points):    
            Award full points if all required skills are present.
            Deduct points proportionally for missing skills.

        B. Experience (20 points)

        Relevant Work Experience (20 points):
            Award points based on the relevance and extent of work experience compared to the JD.
            Full points for exact matches and significant relevant experience
            
        C. Specific Job Responsibilities (10 points)
            Award points based on how well the candidate's previous job responsibilities match the job description.


Resume Content : {resume_content}
Job Description : {job_description}

I want to get out put in below JSON format:
JSON output : 
    "Score" : score you give (int),
    "Explanation" : reason why you give this score(str),
    "Missing": what are missing (in list format),
    "Summary": summary(str)

"""


example_prompt = PromptTemplate.from_template("User input: {input}\nSQL query: {query}")

sql_prompt = FewShotPromptTemplate(
    examples=examples[:10],
    example_prompt=example_prompt,
    prefix="You are a Mysql expert. Given an input question, create a syntactically correct Mysql query to run. Unless otherwise specificed, do not return more than {top_k} rows.\n\nHere is the relevant table info: {table_info}\n\ngive only sql query as output not include any other strings\n\n Below are a number of examples of questions and their corresponding SQL queries.",
    suffix="User input: {input}\nSQL query: ",
    input_variables=["input", "top_k", "table_info"],
)

