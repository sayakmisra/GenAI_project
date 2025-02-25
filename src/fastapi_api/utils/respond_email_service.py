
from langchain_community.llms import Ollama, VLLM
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL


async def respond_email(prev_email, email_sender= '<sender_name>', email_recipient = '<recipient_name>', email_style = 'formal', no_of_words = '80'):
    
    # llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    # llm=Ollama(model="llama3:instruct")

    # Template for building the PROMPT
    template = """
    You are an customer succes email assistant.
    \n\n Write a response email in {style} style to the previous email chain : \n {prev_email}
    \n\n The Sender of the email is : {sender}
    \n\n The recipient is : {recipient}
    
    ###
    Follow the bellow rules while creating the email :
    
    * Write the response email, keeping the context of the previous email body in mind.
    
    * Write the email within {no_of_words} strictly.
    
    * Sign off the email with sender name and 'customer success manager'.
    
    * Do not hallucinate and do not include dummy email-IDs of sender and reciever and return only the email body and nothing else in the response. 
    
    * Do follow the above instructions, while writing the email.
    
    * Start the email with : 'subject'
    
    * Start the email body with : 'Dear'
    
    \n\n ### Email Text:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["style", "sender", "recipient","no_of_words","prev_email"],
        template=template,)

    # Generating the response using LLM
    response = llm(prompt.format(sender=email_sender, recipient=email_recipient, style=email_style, no_of_words=no_of_words, prev_email=prev_email))
    print(prompt.format(sender=email_sender, recipient=email_recipient, style=email_style, no_of_words=no_of_words, prev_email=prev_email))
    print(response)

    return response