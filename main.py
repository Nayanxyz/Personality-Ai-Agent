from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI                                   #these are langchain classes
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import HumanMessage , AIMessage
from langchain_core.output_parsers import StrOutputParser

import os
import gradio as gr                                                                        #library for theme buttons and chatboxes

load_dotenv()

gemini_api= os.getenv("GOOGLE_API_KEY")

system_prompt = """ 

"""



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api,
    temperature=0.3
)

prompt = ChatPromptTemplate([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),                               #like a storage for storing previous chat data
    ("user", "{input}")]
)

