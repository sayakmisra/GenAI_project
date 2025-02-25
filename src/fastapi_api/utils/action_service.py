
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def create_action(action_topic, no_of_words, action_pointers=''):
    
    """
    Asynchronously generates a description for an action using a language model, based on the given topic and optional pointers.

    Parameters:
    -----------
    action_topic : str
        The main subject or theme of the action to be described or planned.
    
    no_of_words : int
        The desired length of the action description in number of words.
    
    action_pointers : str, optional
        Additional details or specific points to include in the action plan. Default is an empty string.

    Returns:
    --------
    str
        A generated action plan or description based on the provided topic, word count, and optional pointers.

    Example:
    --------
    action = await create_action(
        action_topic="Marketing Campaign Plan",
        no_of_words=150,
        action_pointers="Focus on social media outreach, email marketing, and influencer collaborations."
    )
    """

    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

    # Template for building the PROMPT
    template = """
    You are an customer-succes actions creating assistant.
    \n\n Write a action description/body on the topic of :{action_topic}.
    \n\n Follow these key points while composing the action description : {action_pointers}
    
    Follow the below rules before generating the action body :
    
    * Strictly follow the above given pointers while generating the text and do not hallucnate and write anything new of your own.
    
    * Do not include any header, only generate the action description.
    
    * Please start your answer with the tag : <output>  and end the generated text with </output>.
    
    * Write the action description within {no_of_words} strictly.
    
    \n\n ### action description:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=[ "action_topic","no_of_words","action_pointers"],
        template=template,)

    # Generating the response using LLM
    response = llm(prompt.format(action_topic=action_topic, no_of_words=no_of_words,action_pointers=action_pointers))
    
    print(response)

    return response