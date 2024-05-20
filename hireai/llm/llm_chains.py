from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from .prompts import template_resume_extraction,job_summarizer_template,jd_score_template
from .llm_initializations import mixtral_llm
from .helper import parse_data,get_resume_content
import os
import json

output_parser = StrOutputParser()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.environ.get('LANGCHAIN_API_KEY')
## Chain Information extraction from Resumes
def get_user_detials():
    project_name = 'Resume Extraction'
    os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {project_name}"
    resume_content = get_resume_content()
    output_parser = StrOutputParser()
    prompt = PromptTemplate.from_template(template_resume_extraction)
    chain = prompt | mixtral_llm | output_parser
    result = chain.invoke({"resume_content": resume_content})
    print(f"result from LLM: {result}")
    name,email,phone,education,skills,technologies = parse_data(result)

    return resume_content,name,email,phone,education,skills,technologies


def get_job_summary(job_description,job_responsibilities,job_requirements):
    project_name = 'summarization'
    os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {project_name}"

    prompt = PromptTemplate.from_template(job_summarizer_template)
    chain = prompt | mixtral_llm | output_parser
    result = chain.invoke({"job_description": job_description,"job_responsibilities":job_responsibilities,"job_requirements":job_requirements})

    return result


def get_score(resume_content,job_description):
    project_name = 'Resume Scoring'
    os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {project_name}"
    prompt = PromptTemplate.from_template(jd_score_template)
    chain = prompt | mixtral_llm | output_parser
    result = chain.invoke({"resume_content":resume_content,"job_description": job_description})
    data = json.loads(result)
    score=data['Score']
    explanation = data['Explanation']
    missing=data['Missing']
    summary=data['Summary']
    return score,explanation,missing,summary

# if __name__ == '__main__':
#     name,email,phone,education,skills,technologies = get_user_detials()
#     print("Name:", name)
#     print("Email:", email)
#     print("Phone:", phone)
#     print("Education",education)
#     print("Skills:", skills)
#     print("Technologies:", technologies)
