import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

# Initializing Groq api key
os.environ['GROQ_API_KEY'] = os.environ.get('GROQ_API_KEY')

# this model is used for extracting resume informations
groq_res_ex_chat_model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")



