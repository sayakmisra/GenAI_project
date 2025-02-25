
from langchain_community.llms import Ollama, VLLM
from langchain.prompts import PromptTemplate
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL


async def summarize(zapscore,zs_percentile_score,name,zapscore_change, usage_score_change, gutfeel_score_change, tickets_score_change, features_score_change, comms_score_change, payments_score_change, total_tasks, total_messages, total_actions, page_visits, pinned_features_used,churn_prob,aggregation, type='customer'):
    
    # llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY, temperature = .9, max_length=no_of_words
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

    # Template for building the PROMPT
    template = """
        You are customer success expert whose job is to provide help to a customer success person.

        Write a crisp, interesting {aggregation}ly summary of the performance of one of your {type} named : {name},  based on certain input parameters and following certain rules.
        
        ## INPUTS : 
        
        * The overal score(i.e. zapscore) for this {type} named : {name} is {zapscore} {zs_percentile_str}, for this {aggregation}.
        * The overal score(i.e. zapscore) has changed by {zapscore_change} %
        * The usage score has changed by {usage_score_change} %
        * The communication score has changed by {comms_score_change} %
        * The gutfeel score has changed by {gutfeel_score_change} %
        * The ticket score has changed by {tickets_score_change} %
        * The payment score has changed by {payments_score_change} %
        * The features score has changed by {features_score_change} %
        * A total of {page_visits} pages are visited in the {aggregation}.
        * A total of {pinned_features_used} unique pinned features are used in the {aggregation}.
        * A total of {total_tasks} tasks are completed in the {aggregation}.
        * A total of {total_messages} messages are sent in the {aggregation}.
        * A total of {total_actions} actions are completed in the {aggregation}.
        {zs_churn_str}
        
        ## RULES :
        
        * Percentiles signify the performance within it's group/cohort.
        * Higher page visits and features used is a good indication.
        * Positive change in the score from last {aggregation}, indicates it is good.
        * Negative change in the score from last {aggregation}, is not a good indication.
        * DON'T provide a tabular output only provide a textual summary.
        * Do not hallucinate and be very sure of your answer and ONLY use numbers/stats mentioned in the INPUTS section.
        * Always start your answer with the tag : <output>  and end the generated text with </output>.
        * This task is vital to my career and I greatly value your analysis.
        * Put all the positive changes in score (from last {aggregation}) in a paragrapgh and the negative changes in score (from last {aggregation}) in a seperate paragraph.
            
        
        Summarize all the input points to give a small, compact {aggregation}ly summary within 150 words but do not suggest solutions to the customer success person.
        
        ## OUTPUT :
        
        """
        
    if type == 'customer':
        zs_percentile_str = 'and it is in {zs_percentile_score} percentile'.format(zs_percentile_score=zs_percentile_score)
        zs_churn_str = '* It has a churn probability of : {churn_prob}'.format(churn_prob=churn_prob)
    else:
        zs_percentile_str = ''
        zs_churn_str = ''
        
        
    # customer_name = 'ClickUp'
    # zapscore_change, usage_score_change, gutfeel_score_change, tickets_score_change, features_score_change, comms_score_change, payments_score_change  = 9, 12, 26, -11, 27, -8, -9
    # total_tasks, total_messages, total_actions, page_visits, pinned_features_used = 27, 12, 33, 13, 3
    # churn_prob = 'low'
    # aggregation = 'month'

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["type","zapscore","zs_percentile_str","usage_score_change", "gutfeel_score_change", "tickets_score_change", "features_score_change","comms_score_change", "payments_score_change", \
            "total_tasks", "total_messages", "total_actions", "name", "zapscore_change", "zs_churn_str", "aggregation","page_visits", "pinned_features_used"],template=template)

    # print(prompt.format(type=type, zapscore=zapscore,zs_percentile_str=zs_percentile_str,usage_score_change=usage_score_change, gutfeel_score_change= gutfeel_score_change,
    #                 tickets_score_change=tickets_score_change, features_score_change=features_score_change, comms_score_change=comms_score_change, payments_score_change=payments_score_change, zs_churn_str=zs_churn_str, \
    #                 total_tasks=total_tasks, total_messages= total_messages, total_actions=total_actions, name=name, zapscore_change=zapscore_change, aggregation = aggregation, pinned_features_used=pinned_features_used,page_visits=page_visits ))
    # Generating the response using LLM
    response = llm(prompt.format(type=type, zapscore=zapscore,zs_percentile_str=zs_percentile_str,usage_score_change=usage_score_change, gutfeel_score_change= gutfeel_score_change,
                    tickets_score_change=tickets_score_change, features_score_change=features_score_change, comms_score_change=comms_score_change, payments_score_change=payments_score_change, zs_churn_str=zs_churn_str, \
                    total_tasks=total_tasks, total_messages= total_messages, total_actions=total_actions, name=name, zapscore_change=zapscore_change, aggregation = aggregation, pinned_features_used=pinned_features_used,page_visits=page_visits ))
    print(response)

    return response