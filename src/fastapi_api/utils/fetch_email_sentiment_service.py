
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL, SENTIMENTS
from src.fastapi_api.utils.helper_service import extract_email_body_new

# SENTIMENTS = ['positive', 'negative', 'neutral']

from src.config import EMOTIONS

async def fetch_email_thread_sentiment(email_body, sentiment_list=SENTIMENTS):
    print('inside tag_sentiment....')
    """
    Asynchronously tags or identifies emotions present in the email content using a language model.

    Parameters:
    -----------
    email_body : str
        The full text of the email whose emotional tone needs to be analyzed.
    
    emotions : list of str, optional
        A predefined list of emotions to check for in the email content. Default is `EMOTIONS`.

    Returns:
    --------
    dict
        A dictionary where keys are emotions and values indicate the presence or intensity of the emotion in the email body.

    Example:
    --------
    emotion_tags = await tag_emotion(
        email_body="I am very happy with the progress, but a bit concerned about the upcoming deadlines."
    )
    """
    
    # Preprocess/ parse the email-body.
    email_body = extract_email_body_new(email_body)
    print('email : ',email_body)
    
    if email_body.strip() == '':
        return "{'sentiment': '', 'score' : 0}"
    else:
        # llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words)
        llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, format = 'json', temperature = 0.0)
        # llm=Ollama(model="mistral:instruct")

        # Template for building the PROMPT

        EXAMPLES = ''' 
        
        example 1: 
        email : 
        Hi Manasij, 
            great work by the team, loved the product.
        response : {{ 'label':'positive', 'score':0.9 }}
        
        example 2: 
        email : Not really satisfied with the rsponse.
        response : {{ 'label':'negative', 'score':0.9 }}
        
        example 3: 
        email : Hope you are doing well. Please find attached. Hope this works.
        response : response : {{ 'label':'neutral', 'score':0.8 }}
        
        example 4: Sending you the updated invite.
        response : response : {{ 'label':'neutral', 'score':0.9 }}
        
        example 5: This is a reminder for your next installment of Zapscale Customer Success Software. Please refer to the following details and arrange for payment. Invoice is attached for your reference.
        response : response : response : {{ 'label':'neutral', 'score':0.8 }}
        
        '''
        
        prompt = """You are an expert email sentiment analyser.
        Following is a thread of communication(email-chain) in chronological order, newest to oldest.
        Given this email chain, decide what is the sentiment of the email chain. Do select valid overall sentiment from the below provided list.

        List of sentiment :
        {sentiment_list}

        Include ONLY one sentiment from the provided above list.

        Below is a customer email delimited with ###. 

        email chain:
        ###
        {email}
        ###
        
        Follow the below rules before generating the concerns list :

        * Please, identify the main sentiment in this above email from 'positive', 'negative' or 'neutral'.
        
        * Provide a sentiment as neutral if the email provides factual information.
        
        * Add a confidence score between (0-1) to your answer.
        
        * Be very sure before your answer, if you are not very sure of the sentiment from the email, then return 'neutral' like : {{ "label": "neutral", "score": 0.9 }} 
        
        * Return 'positive' as the selected sentiment ONLY if there is something very positive reffered in the email.
        
        * Return 'negative' as the selected sentiment ONLY if there is something very negative reffered in the email.
        
        * This task is vital to my career and I greatly value your analysis.
        
        * Be very sure of your answer, and have another look into it.

        * return a json, with 'sentiment' and 'score' as the key.
            
        * Please Output/return in the following format :
            {{ 'label':<sentiment>, 'score':<score> }}
            
        * Do not hallucinate and do not provide new sentiment, include ONLY sentiment from the provided above list.
        
        
    ### Here are a few examples:  
    {examples}
    
    
    ## OUTPUT :
    
    """
    
    prompt = PromptTemplate(template=prompt, input_variables=["email","sentiment_list", "examples"])

    prompt = prompt.format(email = email_body, sentiment_list = sentiment_list, examples = EXAMPLES)
    response=llm(prompt)
    print('response : ',response)

    return response