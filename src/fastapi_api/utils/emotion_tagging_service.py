
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL
from src.fastapi_api.utils.helper_service import extract_email_body_new

# EMOTIONS = ['joy', 'anger', 'surprise', 'upset', 'neutral']

from src.config import EMOTIONS

async def tag_emotion(email_body, emotions=EMOTIONS):
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
        return '<output> [] </output>'
    else:
        llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=0.0)
        # llm=Ollama(model="mistral:instruct")

        # Template for building the PROMPT

        EXAMPLES = ''' 
        
        example 1: 
        email : 
        Hi Manasij, 
            great work by the team, loved the product.
        response : <output>['joy']</output>
        
        example 2: 
        email : Not really satisfied with the rsponse.
        response : <output>['upset']</output>
        
        example 3: 
        email : Hope you are doing well. Please find attached. Hope this works.
        response : <output>['neutral']</output>
        
        example 4: Sending you the updated invite.
        response : <output>['neutral']</output>
        
        example 5: This is a gentle reminder for your due payment.
        response : <output>['neutral']</output>
        
        '''
        
        template = """You are an expert email emotion analyser.
        Given this email, decide what is the emotion of the email. Do select valid emotion from the below provided list.

        List of emotion :
        {emotion_list}

        Include ONLY emotions from the provided above list.

        Below is a customer email delimited with ###. 

        email:
        ###
        {email}
        ###
        
        Follow the below rules before generating the emotion :

        * Please, identify the main emotion in this above email from the list of emotions provided earlier.
        
        * Provide a sentiment as neutral if the email provides mostly factual information.
        
        * Return a emotion list for the customer email from the provided emotion list.
                
        * This task is vital to my career and I greatly value your analysis.
        
        * Be very sure of your answer, and have another look into it.

        * Please Output in the following format :
            <output>['<emotion>']</output>
            
        * Be very sure before your answer, if you are not very sure of the emotion from the email, then return 'neutral' like : <output>['neutral']</output> 
                        
        * Do not hallucinate and do not provide new emotions, include ONLY emotions from the provided above list.
        
        * Return 'joy' as the selected emotion ONLY if there is something very happy/joyful reffered in the email.
        
        * Return 'surprise' as the selected emotion ONLY if there is something very surprising reffered in the email.
        
        * Return 'anger' as the selected emotion ONLY if there is something very angry reffered in the email.
        
        * Return 'upset' as the selected emotion ONLY if there is something very upsetting reffered in the email.
        
        * Please start your response with the tag : <output>  and end the generated text with </output>.

        ### Here are a few examples:  
        {examples}
    
        ## OUTPUT :
        
        """

        # print('customer_email : ',customer_email)


        prompt = PromptTemplate(template=template, input_variables=["email","examples","emotion_list"])

        prompt = prompt.format(email = email_body,examples=EXAMPLES, emotion_list = emotions)
        # print(prompt)
        response=llm(prompt)
        print('response : ',response)

        return response