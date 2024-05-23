import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# Initializing Groq api key
os.environ['GROQ_API_KEY'] = os.environ.get('GROQ_API_KEY')

# Initializing GOOGLE API KEY
os.environ['GOOGLE_API_KEY'] = os.environ.get('GOOGLE_API_KEY')

# this model is used for extracting resume informations and summarization
mixtral_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


# this model is used for summarizing job description
job_summarizer_llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")


# this model is used for Chat with sql
sql_llm = ChatGoogleGenerativeAI(model="gemini-pro")
