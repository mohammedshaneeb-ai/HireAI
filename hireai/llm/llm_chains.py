from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from .prompts import template_resume_extraction
from .llm_initializations import groq_res_ex_chat_model
from .helper import parse_data,get_resume_content

## Chain Information extraction from Resumes
def get_user_detials():
    resume_content = get_resume_content()
    output_parser = StrOutputParser()
    prompt = PromptTemplate.from_template(template_resume_extraction)
    chain = prompt | groq_res_ex_chat_model | output_parser
    result = chain.invoke({"resume_content": resume_content})
    print(f"result from LLM: {result}")
    name,email,phone,education,skills,technologies = parse_data(result)

    return name,email,phone,education,skills,technologies



# if __name__ == '__main__':
#     name,email,phone,education,skills,technologies = get_user_detials()
#     print("Name:", name)
#     print("Email:", email)
#     print("Phone:", phone)
#     print("Education",education)
#     print("Skills:", skills)
#     print("Technologies:", technologies)
