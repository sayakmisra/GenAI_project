DEV_URL = 'http://127.0.0.1:8000'
PROD_URL = 'http://35.171.18.228:8000'

OLLAMA_HOST = "localhost"
# OLLAMA_HOST = "ollama"
# OLLAMA_PORT = 8888
OLLAMA_PORT = 11434

OLLAMA_BASE_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"

# OLLAMA_MODEL = "llama3:instruct"
OLLAMA_MODEL = "llama3.1:8b-instruct-q4_0"
OLLAMA_MODEL_LONG_CONTEXT = "llama3.1:8b"

HF_SENTIMENT_CLASSIFICATION_MODEL='cardiffnlp/twitter-roberta-base-sentiment-latest'
# HF_SENTIMENT_CLASSIFICATION_MODEL = 'siebert/sentiment-roberta-large-english'

CONCERNS = ['product issue','bad support experience','cancellation request','no issue','need update','need action', 'related to payment' ]
SENTIMENTS = ['positive', 'negative', 'neutral']

EMOTIONS = ['joy', 'anger', 'surprise', 'upset', 'neutral']


