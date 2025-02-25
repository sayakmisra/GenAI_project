
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def create_note(note_topic, no_of_words, note_pointers=''):

    """
    Asynchronously generates a note based on a given topic, word count, and optional pointers using a language model.

    Parameters:
    -----------
    note_topic : str
        The subject or theme of the note to be generated.
    
    no_of_words : int
        The desired length of the note in number of words.
    
    note_pointers : str, optional
        Additional details or key points to be included in the note. Default is an empty string.

    Returns:
    --------
    str
        A generated note based on the provided topic, word count, and optional pointers.

    Example:
    --------
    note = await create_note(
        note_topic="Meeting Summary",
        no_of_words=50,
        note_pointers="Discussed project milestones, deadlines, and resource allocation."
    )
    """
    # llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words)
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

    # Template for building the PROMPT
    template = """
    You are an customer-succes notes creating assistant.
    \n\n Write a note description/body on the topic of :{note_topic}.
    \n\n Follow these key points while composing the note description : {note_pointers}
    
    Follow the below rules before generating the note body :
    
    * Strictly follow the above given pointers while generating the text and do not hallucnate and write anything new of your own.
    
    * Do not include any header, only generate the note description.
    
    * Please start your answer with the tag : <output>  and end the generated text with </output>.
    
    * Write the note description within {no_of_words} strictly.
    
    \n\n ### Note description:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=[ "note_topic","no_of_words","note_pointers"],
        template=template,)

    # Generating the response using LLM
    response = llm(prompt.format(note_topic=note_topic, no_of_words=no_of_words, note_pointers=note_pointers))
    
    print(response)

    return response