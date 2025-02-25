
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def create_task(task_topic, no_of_words, task_pointers=''):
    """
    Asynchronously generates a detailed task description based on the given topic, word count, and optional pointers using a language model.

    Parameters:
    -----------
    task_topic : str
        The subject or main focus of the task to be generated.
    
    no_of_words : int
        The desired length of the task description in number of words.
    
    task_pointers : str, optional
        Additional specific details or key points to include in the task description. Default is an empty string.

    Returns:
    --------
    str
        A generated task description based on the provided topic, word count, and optional pointers.

    Example:
    --------
    task = await create_task(
        task_topic="Develop project roadmap",
        no_of_words=100,
        task_pointers="Include key milestones, deadlines, and resource allocation."
    )
    """
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=0.8)

    # Template for building the PROMPT
    template = """
    You are an customer succes task creating assistant.
    \n\n Write a task description/body on the topic of :{task_topic}.
    \n\n Follow these key points while composing the task description : {task_pointers}.
    
    Follow the below rules before generating the task body :
    
    * Strictly follow the above given pointers while generating the text and do not hallucnate and write anything new of your own.
    
    * Do not include any header, only generate the task description.
    
    * Please start your answer with the tag : <output>  and end the generated text with </output>.
    
    * Write the task description within {no_of_words} strictly.
    
    
    \n\n ### Task description:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=[ "task_topic","no_of_words","task_pointers"],
        template=template)

    # Generating the response using LLM
    response = llm(prompt.format(task_topic=task_topic, no_of_words=no_of_words, task_pointers=task_pointers))
    print(prompt.format(task_topic=task_topic, no_of_words=no_of_words, task_pointers=task_pointers))
    
    print('*'*80)
    print(response)
    print('*'*80)
    

    return response