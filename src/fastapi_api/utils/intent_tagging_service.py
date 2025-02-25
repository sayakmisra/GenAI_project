
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL
from src.fastapi_api.utils.helper_service import extract_email_body_new

# CONCERNS = ['product issue','bad support experience','cancellation request','no issue','need update','need action', 'related to payment' ]
from src.config import CONCERNS

async def tag_intent(email_body, concerns=CONCERNS):
    # Preprocess/ parse the email-body.
    email_body = extract_email_body_new(email_body)
    
    if email_body.strip() == '':
        return '<output> [] </output>'
    else:
        llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature = 0.2)
        # llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

        # Template for building the PROMPT
        EXAMPLES = ''' 
        
        example 1: 
        email : 
        We have observed that an invoice with 200 MB of attachments did not upload successfully in the SFTP Server.
            Could you please check and confirm if there is a size limit on the SAP end?
        response : <output>['need action', 'product issue', 'need update']</output>
        
        example 2: 
        email : Satya has asked multiple time to demo the new dashboards but I am unable to commit him any date and I don’t get any response of the status.
            Can you please confirm.
        response : <output>['need action']</output>
        
        example 3: 
        email : Resolve this quickly, payment is on hold because of this.
        response : <output>['product issue', 'related to payment', 'need action']</output>
        
        example 4: 
        email : Hope you are doing well.
        response : <output>['no issue']</output>
        
        '''
        
        template = '''You are an expert email tagger.
        Given this email, decide what are the issues the customer is concerned about. Do select valid concerns from the below provided list.

        List of concerns :
        {concerns_list}

        Include ONLY concerns from the provided above list.

        Below is a customer email delimited with ###. 

        email:
        ###
        {email}
        ###
        
        Follow the below rules before generating the concerns list :

        * Please, identify the main concerns mentioned in this above email from the list of concerns provided earlier.

        * Return a list of concerns for the customer email from the provided concerns list.

        * Please Output in a list/array in the following format :
            <output> ["<concern1>", "<concern2>", ...] </output>
            
        * Do not hallucinate and provide new concerns, include ONLY concerns from the provided above list.
        
        * This task is vital to my career and I greatly value your analysis.
        
        * Be very sure of your answer, and have another look into it.
        
        * Be very sure of your answer, if you are not sure or concerns from the concern list are not relevant to the customer email, return 'no issue' like :   <output>['no issue']</output> 
        
        * Please start your response with the tag : <output>  and end the generated text with </output>. 
        
        * If the response dosenot have the <output> and </output> tags, do include <output> and </output> in your response. DO NOT respond without the tags.
        
        ### Here are a few examples:  
        {examples}

        '''

        # print('customer_email : ',customer_email)


        prompt = PromptTemplate(template=template, input_variables=["email","examples","concerns_list"])

        prompt = prompt.format(email = email_body,examples=EXAMPLES, concerns_list = concerns)
        # print(prompt)
        response=llm(prompt)
        print('response : ',response)

        return response