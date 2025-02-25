
from langchain_community.llms import Ollama, VLLM
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL


async def create_email(email_topic,email_pointers, email_sender= '<sender_name>', email_recipient = '<recipient_name>', email_style = 'formal', no_of_words = '80'):
    """
    Asynchronously generates an email draft using a language model based on the given parameters.

    Parameters:
    -----------
    email_topic : str
        The main subject or theme of the email.
    
    email_pointers : list of str
        A list of key points or bullet points to be included in the body of the email.
    
    email_sender : str, optional
        The name or identifier of the email's sender. Default is '<sender_name>'.
    
    email_recipient : str, optional
        The name or identifier of the email's recipient. Default is '<recipient_name>'.
    
    email_style : str, optional
        The tone or style of the email. Options can include 'formal', 'informal', etc. Default is 'formal'.
    
    no_of_words : int or str, optional
        The approximate number of words for the email body. Default is '80'.
    
    Returns:
    --------
    str
        A generated email draft based on the provided topic, pointers, and style.
    
    Example:
    --------
    email = await create_email(
        email_topic="Project Update", 
        email_pointers=["Completed phase 1", "Moving to phase 2", "Awaiting client feedback"], 
        email_sender="John Doe", 
        email_recipient="Jane Smith", 
        email_style="informal", 
        no_of_words=100
    )
    """
    
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    
    # Template for building the PROMPT
    template = """
    You are an customer succes email assistant.
    \n\n Write a email in {style} style and on the topic of :{email_topic}.
    \n\n Follow these key points while composing the email : {email_pointers}
    \n\n The Sender of the email is : {sender}
    \n\n The recipient is : {recipient}
    
    ###
    Follow the bellow rules while creating the email :
    
    * Write the email within {no_of_words} strictly.
    
    * Sign off the email with sender name and 'customer success manager'.
    
    * Do not hallucinate and do not include dummy email-IDs of sender and reciever and return only the email body and nothing else in the response. 
    
    * Do follow the above instructions, while writing the email.
    
    * Start the email with  : 'subject'
    
    * Start the email body with : 'Dear'
    
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