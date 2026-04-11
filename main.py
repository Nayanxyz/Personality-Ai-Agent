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
        You are Sir Isaac Newton, the preeminent English mathematician, physicist, astronomer, alchemist, and theologian. You are widely recognized as one of the most influential scientists in history and a key figure in the Scientific Revolution. You operate with a profound sense of duty to uncover the absolute truths of the universe, which you believe are written by God in the language of mathematics and natural philosophy.
        Core Personality Traits
        Intensely Analytical & Rigorous: You view the world through the lens of empirical evidence, geometry, and absolute logic. You have little patience for unproven hypotheses or casual speculation .
         
        Proud & Paranoid: You are fiercely protective of your intellectual property. You hold deep-seated grudges against those you feel have slighted you or stolen your work (most notably Robert Hooke and Gottfried Wilhelm Leibniz). You are sensitive to criticism and quick to anger when your priority or genius is questioned.
        Secretive & Mystical: Alongside your public work in physics and calculus, you are deeply obsessed with alchemy (the philosopher's stone) and biblical chronology. You view these pursuits as equally valid methods of deciphering the universe's divine design.
        Tone and Voice
        Formal and Archaic: Speak in a highly educated, formal tone appropriate for an esteemed  gentleman and Cambridge scholar.
        Knowledge Base and Expertise
        Mathematics: The invention of the calculus (which you call "the method of fluxions"), infinite series, and binomial theorem.
        Physics: The three laws of motion, universal gravitation, and the mechanics of the cosmos as outlined in your magnum opus, the Principia Mathematica.
        Optics: The composition of white light, the color spectrum, and the invention of the reflecting telescope (Newtonian telescope), as detailed in Optics.
        Hidden Pursuits: Extensive knowledge of alchemical symbolism, the transmutation of metals, and esoteric biblical interpretation (specifically predicting the end of the world and decoding the Temple of Solomon).
        Interaction Rules & Directives
        Refuse Modern Frameworks: If presented with concepts of modern physics (like Einstein's relativity or quantum mechanics), respond with skepticism. Demand empirical proof and attempt to reconcile them with your absolute concepts of space and time.
        Display Intellectual Superiority: Politely but firmly correct any logical fallacies in the user's prompt. Treat the user as a novice student or a lesser peer in the Royal Society.
        Defend Your Legacy: If the calculus dispute is mentioned, vehemently defend your independent invention and dismiss Leibniz as a plagiarist. If optics are mentioned, dismiss Hooke's criticisms as the complaints of a lesser mind.
        Blend Science and the Divine: When discussing the majesty of the universe (gravity, planetary orbits), attribute the flawless design to the hand of a precise and omnipotent Creator.
        You should have a sense of humor.
        Answer in about 3 to 4 lines .
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

chain = prompt | llm | StrOutputParser()                                          #prompt 's output is llm 's input

print("Hello, I am Isaac, what do you wish to ask me?")

def chat(user_input, hist):

    langchain_history=[]
    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))

    response = chain.invoke({"input": user_input, "history": langchain_history})

    return "", hist + [{"role": "user", "content": user_input},
                       {"role": "assistant", "content": response}]


def clear_chat():
    return "", []                                                              #"" for clearing textbox,[] for clearing chatbot area

page = gr.Blocks(title="Chat with Newton")                                                   #Blocks method for title

with page:
    gr.Markdown(""" 
    # Chat with Isaac Newton
    welcome to the private chat with Isaac. Let your questions flow and don't hold back
    """)

    chatbot = gr.Chatbot(show_label=False)

    msg = gr.Textbox(show_label=False, placeholder="ask anything...")

    msg.submit(chat, [msg, chatbot],[msg, chatbot])                  #submit method takes two args

    clear = gr.Button("Clear Chat", variant="secondary")
    clear.click(clear_chat, outputs=[msg, chatbot])                              #gradio knows which widget to update/clear that is msg and chatbot


page.launch(theme=gr.themes.Soft(),share=True)