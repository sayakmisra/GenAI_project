
"""This is a template for a custom chain.

Edit this file to implement your chain logic.
"""

from langchain.chat_models.openai import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.runnable import Runnable
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate




def get_chain() -> Runnable:
    """Return a chain."""
    # prompt = ChatPromptTemplate.from_template("write a email on the topic : {topic}")
    llm=Ollama(model="mistral:instruct")
    
     # Template for building the PROMPT
    template = """
    You are an customer succes email assistant.
    \n\n Write a email in {style} style and on the topic of :{email_topic}.
    \n\n Follow these key points while composing the email : {pointers}
    \n\n The Sender of the email is : {sender}
    \n\n The recipient is : {recipient}
    
    Write the email within {no_of_words} words strictly.
    
    Sign off the email with sender name and 'customer success manager'.
    
    Do not hallucinate and do not include dummy email-IDs of sender and reciever and return only the email body and nothing else in the response. 
    Do follow the above instructions, while writing the email.
    \n\n ### Email Text:
    
    """

    # Creating the final PROMPT
    # input_variables=["style", "email_topic", "sender", "recipient","no_of_words"],
    
    
    prompt = PromptTemplate(
        input_variables =["style", "email_topic", "sender", "recipient","no_of_words", "pointers"],
        
        template=template,)
    
    print(prompt)
    return prompt | llm
