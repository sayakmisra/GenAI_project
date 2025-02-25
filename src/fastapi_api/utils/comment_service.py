
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def create_comment(no_of_words, comment_pointers=''):
    """
    Asynchronously generates a comment based on a given topic, word count, and optional pointers using a language model.

    Parameters:
    -----------
    
    no_of_words : int
        The desired length of the comment in number of words.
    
    comment_pointers : str, optional
        Additional details or key points to be included in the comment. Default is an empty string.

    Returns:
    --------
    str
        A generated comment based on the provided topic, word count, and optional pointers.

    Example:
    --------
    comment = await create_comment(
        comment_topic="Team Motivation",
        no_of_words=100,
        comment_pointers="Highlight recent achievements, emphasize upcoming goals, express gratitude."
    )
    """
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    
    # Template for building the PROMPT
    template = """
    You are an customer-succes assistant who helps to write comments.
    
    \n\n Follow these key points to write the comment : 
    
    ### COMMENT POINTERS : 
    
    {comment_pointers}
    
    Follow the below rules before generating the comment body :
    
    ## RULES : 
    
    * Strictly follow the above given pointers while generating the text and do not hallucnate and write anything new of your own.
    
    * Do not include any header, only generate the comment.
    
    * Please start your answer with the tag : <output>  and end the generated text with </output>.
    
    * Write the comment description within {no_of_words} strictly.
    
    \n\n ### COMMENT description:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=[ "no_of_words","comment_pointers"],
        template=template,)

    # Generating the response using LLM
    response = llm(prompt.format(no_of_words=no_of_words,comment_pointers=comment_pointers))
    
    print(response)

    return response