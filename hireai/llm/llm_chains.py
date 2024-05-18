from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from .prompts import template_resume_extraction,job_summarizer_template
from .llm_initializations import mixtral_llm
from .helper import parse_data,get_resume_content

output_parser = StrOutputParser()

## Chain Information extraction from Resumes
def get_user_detials():
    resume_content = get_resume_content()
    output_parser = StrOutputParser()
    prompt = PromptTemplate.from_template(template_resume_extraction)
    chain = prompt | mixtral_llm | output_parser
    result = chain.invoke({"resume_content": resume_content})
    print(f"result from LLM: {result}")
    name,email,phone,education,skills,technologies = parse_data(result)

    return name,email,phone,education,skills,technologies


def get_job_summary(job_description,job_responsibilities,job_requirements):
    prompt = PromptTemplate.from_template(job_summarizer_template)
    chain = prompt | mixtral_llm | output_parser
    chain.invoke({"job_description": job_description,"job_responsibilities":job_responsibilities,"job_requirements":job_requirements})



# if __name__ == '__main__':
#     name,email,phone,education,skills,technologies = get_user_detials()
#     print("Name:", name)
#     print("Email:", email)
#     print("Phone:", phone)
#     print("Education",education)
#     print("Skills:", skills)
#     print("Technologies:", technologies)
