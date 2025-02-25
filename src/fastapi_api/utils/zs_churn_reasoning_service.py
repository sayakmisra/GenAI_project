
from langchain_community.llms import Ollama, VLLM
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL


async def churn_reason(customer_name,percent_this_c2_is_red_in_last_30_days, percent_this_c2_is_green_in_last_30_days, percent_this_c2_is_yellow_in_last_30_days, percent_this_c2_is_grey_in_last_30_days,churn_prob):
    
    # llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words
    llm = Ollama(model="llama3.1:8b-instruct-q4_0")

    template = """
        You are customer success expert whose job is to provide help to a customer success person.

        The churn probalility of the customer : {customer_name} is {churn_prob}, give a proper explanation for the churn probalility being {churn_prob}, based on the bellow inputs and rules.

        ## INPUTS : 
        
        * This customer is in red(bad state) for {percent_this_c2_is_red_in_last_30_days} percent days in last 30 days.
        
        * This customer is in green(good state) for {percent_this_c2_is_green_in_last_30_days} percent days in last 30 days.
        
        * This customer is in yellow(moderate state) for {percent_this_c2_is_yellow_in_last_30_days} percent days in last 30 days.
        
        * This customer is in grey(inactive state) for {percent_this_c2_is_grey_in_last_30_days} percent days in last 30 days.
        
        ## RULES :
        
        * DON'T provide a tabular output only provide a textual summary.
        
        * Do not hallucinate and be very sure of your answer and ONLY use numbers/stats mentioned in the INPUTS section.
        
        * Always start your answer with the tag : <output>  and end the generated text with </output>.
        
        * This task is vital to my career and I greatly value your analysis.

        
        Summarize all the inputs to give a small, compact reasoning for churn-probalility being {churn_prob} within 200 words but do not suggest solutions to the customer success person.
        
        ## OUTPUT :
        
        """
        
    # customer_name = 'ClickUp'
    # percent_this_c2_is_red_in_last_30_days, percent_this_c2_is_green_in_last_30_days, percent_this_c2_is_yellow_in_last_30_days, percent_this_c2_is_grey_in_last_30_days = 27, 38, 25, 10
    # churn_prob = 'mid'

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["percent_this_c2_is_red_in_last_30_days", "percent_this_c2_is_green_in_last_30_days", "percent_this_c2_is_yellow_in_last_30_days", "percent_this_c2_is_grey_in_last_30_days", \
            "churn_prob" , "customer_name"],template=template)

    # Generating the response using LLM
    response = llm(prompt.format(percent_this_c2_is_red_in_last_30_days=percent_this_c2_is_red_in_last_30_days, percent_this_c2_is_green_in_last_30_days= percent_this_c2_is_green_in_last_30_days,
                    percent_this_c2_is_yellow_in_last_30_days=percent_this_c2_is_yellow_in_last_30_days, percent_this_c2_is_grey_in_last_30_days=percent_this_c2_is_grey_in_last_30_days,churn_prob=churn_prob,customer_name=customer_name ))

    return response