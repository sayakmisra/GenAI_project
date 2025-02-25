
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL, SENTIMENTS
from src.fastapi_api.utils.helper_service import extract_email_body_new
from transformers import pipeline


# SENTIMENTS = ['positive', 'negative', 'neutral']

from src.config import SENTIMENTS, HF_SENTIMENT_CLASSIFICATION_MODEL

# model='siebert/sentiment-roberta-large-english'
# model='cardiffnlp/twitter-roberta-base-sentiment-latest' (IN USE)

async def tag_sentiment_hf(email_body, sentiment_list=SENTIMENTS):
    """
    Asynchronously tags or identifies sentiment present in the email content using a language model.

    Parameters:
    -----------
    email_body : str
        The full text of the email whose sentimental tone needs to be analyzed.
    
    sentiments : list of str, optional
        A predefined list of sentiment to check for in the email content.

    Returns:
    --------
    dict
        A dictionary where keys are sentiment and values indicate the presence or intensity of the sentiment in the email body.

    Example:
    --------
    sentiment_tags = await tag_sentiment(
        email_body="I am very happy with the progress, but a bit concerned about the upcoming deadlines."
    )
    """
    
    # Preprocess/ parse the email-body.
    email_body = extract_email_body_new(email_body)
    print('email : ',email_body)
    
    if email_body.strip() == '':
        return {'sentiment': '', 'score' : 0}
    else:
        sentiment_classify_pipeline = pipeline("sentiment-analysis", model=HF_SENTIMENT_CLASSIFICATION_MODEL, tokenizer=HF_SENTIMENT_CLASSIFICATION_MODEL)
        response=sentiment_classify_pipeline(email_body)
        print('response : ',response)
        response = response[0]

    return response