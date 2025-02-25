import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.llms import Ollama

## Function To get response from LLAma 2 model

# repo_id="meta-llama/Meta-Llama-3-8B-Instruct"
# repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
# repo_id = "HuggingFaceH4/zephyr-7b-beta"
repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1"

# Function to get the response back


def getLLMResponse(email_topic,email_pointers, email_sender, email_recipient, email_style, no_of_words):

    # C Transformers is the Python library that provides bindings for transformer models implemented in C/C++ using the GGML library

    llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words)
    # llm=Ollama(model="llama3:instruct")
    # llm=Ollama(model="mistral:instruct")
    # llm=Ollama(model="mymistral:latest")

    # Template for building the PROMPT
    template = """
    You are an customer succes email assistant.
    \n\n Write a email in {style} style and on the topic of :{email_topic}.
    \n\n Follow these key points while composing the email : {email_pointers}
    \n\n The Sender of the email is : {sender}
    \n\n The recipient is : {recipient}
    
    Write the email within {no_of_words} strictly.
    
    Sign off the email with sender name and 'customer success manager'.
    
    Do not hallucinate and do not include dummy email-IDs of sender and reciever and return only the email body and nothing else in the response. 
    Do follow the above instructions, while writing the email.
    \n\n ### Email Text:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["style", "email_topic", "sender", "recipient","no_of_words"],
        template=template,)

    # Generating the response using LLM
    response = llm(prompt.format(email_topic=email_topic, email_pointers= email_pointers,
                   sender=email_sender, recipient=email_recipient, style=email_style, no_of_words=no_of_words))
    print(prompt.format(email_topic=email_topic, email_pointers= email_pointers,
                   sender=email_sender, recipient=email_recipient, style=email_style, no_of_words=no_of_words))
    print(response)

    return response


st.set_page_config(page_title="Generate Emails",
                   page_icon='📧',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Generate Emails 📧")

email_topic = st.text_area('Enter the email topic/subject : ', height=10)
email_pointers = st.text_area('Enter key email-pointers :', height=200)

# Creating columns for the UI - To receive inputs from user
col1, col2, col3, col4 = st.columns([5, 5, 10, 5])
with col1:
    email_sender = st.text_input('Sender Name')
with col2:
    email_recipient = st.text_input('Recipient Name')
with col3:
    email_style = st.selectbox('Writing Style',
                               ('Formal', 'Appreciating',
                                'Not Satisfied', 'Neutral'),
                               index=0)
with col4:
    no_of_words = st.text_input('No of words')


submit = st.button("Generate")

# When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(email_topic,email_pointers, email_sender,
             email_recipient, email_style, no_of_words))