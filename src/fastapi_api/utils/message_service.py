
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def create_message(message_topic, no_of_words, message_pointers=''):

    # llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words)
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    # llm=Ollama(model="llama3:instruct")
    # llm=Ollama(model="mistral:instruct")
    

    # Template for building the PROMPT
    template = """
    You are an customer-succes messages creating assistant.
    \n\n Write a message description/body on the topic of :{message_topic}.
    \n\n Follow these key points while composing the message body : {message_pointers}
    
    Follow the below rules before generating the message body :
    
    * Strictly follow the above given pointers while generating the text and do not hallucnate and write anything new of your own.
    
    * Do not include any header, only generate the message description.
    
    * Please start your answer with the tag : <output>  and end the generated text with </output>.
    
    * Write the message description within {no_of_words} strictly.
    
    \n\n ### message description:
    
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=[ "message_topic","no_of_words","message_pointers"],
        template=template,)

    # Generating the response using LLM
    response = llm(prompt.format(message_topic=message_topic, no_of_words=no_of_words,message_pointers=message_pointers))
    
    print(response)

    return response