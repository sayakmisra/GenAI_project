
from langchain_community.llms import Ollama, VLLM
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_MODEL_LONG_CONTEXT


async def summarize_email(email_body):
    """
    Asynchronously generates a concise summary of the provided email content using a language model.

    Parameters:
    -----------
    email_body : str
        The full text of the email that needs to be summarized.

    Returns:
    --------
    str
        A summary of the email's key points and overall content.

    Example:
    --------
    summary = await summarize_email(
        email_body="Dear team, we have successfully completed phase 1 of the project. Phase 2 will begin next week, and we are awaiting feedback from the client before proceeding."
    )
    """
    
    # TODO : Parse the email-chain to make it more understandable.
    # email_body = parse_email_chain(email_body)
    
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

    # Template for building the PROMPT
    template = ''' 

    You are an expert in email communication and summarization. Following is a thread of communication in chronological order, newest to oldest.
    Write a small and crisp summary of the following email-chain/ email, and strictly follow the below mentioned rules before generating the summary.

    ## RULES :

    * Strictly provide ONLY the text summary of the email chain. 
    * This task is vital to my career and I greatly value your analysis.
    * Do not hallucinate and do not provide new information, only use the below email-body for summarizaton.
    * AlWAYS start your answer with the tag : <output>  and end the generated text with </output>.


    ### EMAIL : 

    {email_body}

    ### SUMMARY :

    '''

    # Creating the final PROMPT
    prompt = PromptTemplate(input_variables=["email_body"],template=template)
    response = llm(prompt.format(email_body=email_body))
    print('here....')
    print(response)

    return response