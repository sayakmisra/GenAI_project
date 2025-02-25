from fastapi import FastAPI
from pandas.core.common import flatten

import sys,os

# set the cwd as the root directory
sys.path.append(os.getcwd())
import json
from src.fastapi_api.utils.email_service import create_email
from src.fastapi_api.utils.respond_email_service import respond_email
from src.fastapi_api.utils.task_service import create_task
from src.fastapi_api.utils.note_service import create_note
from src.fastapi_api.utils.action_service import create_action
from src.fastapi_api.utils.message_service import create_message
from src.fastapi_api.utils.comment_service import create_comment
from src.fastapi_api.utils.intent_tagging_service import tag_intent
from src.fastapi_api.utils.emotion_tagging_service import tag_emotion
from src.fastapi_api.utils.sentiment_tagging_service import tag_sentiment
from src.fastapi_api.utils.sentiment_tagging_service_hf import tag_sentiment_hf
from src.fastapi_api.utils.helper_service import list_intersection
from src.fastapi_api.utils.zs_summarizer_service import summarize
from src.fastapi_api.utils.email_summarization_service import summarize_email
from src.fastapi_api.utils.zs_churn_reasoning_service import churn_reason
from src.fastapi_api.schemas import EmailInput, TaskInput, NoteInput, ActionInput, MessageInput, IntentInput, RespondEmailInput, EmotionInput, SummarizeInput, EmailSummarizeInput, CommentInput, ChurnReasoningInput, \
    SentimentInput, SummarizeInputV2
    
import src.config
import uvicorn
from src.config import CONCERNS, EMOTIONS, SENTIMENTS
from src.fastapi_api.utils.helper_service import extract_email_body_new

import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()

@app.post('/generate_email')
async def main(input_params: EmailInput):
    try:
        email = await create_email(input_params.email_topic,input_params.pointers, input_params.sender, input_params.recipient, input_params.style, input_params.no_of_words)
        email_subject = email.split('Subject:')[1].split('Dear')[0]
        email_body = email.split(email_subject)[1]
        email_dict = {'email_subject': email_subject, 'email_body': email_body}
        return email_dict
    except Exception as inst:
        return {'email_subject': '', 'email_body': ''}

@app.post('/respond_email')
async def main(input_params: RespondEmailInput):
    try:
        print('*'*50)
        email = await respond_email(input_params.prev_email, input_params.sender, input_params.recipient, input_params.style, input_params.no_of_words)
        email_subject = email.split('Subject:')[1].split('Dear')[0]
        email_body = email.split(email_subject)[1]
        email_dict = {'email_subject': email_subject, 'email_body': email_body}
        return email_dict
    except Exception as inst:
        return {'email_subject': '', 'email_body': ''}

@app.post('/generate_task')
async def main(input_params: TaskInput):
    try:
        task = await create_task(input_params.task_topic,input_params.no_of_words, input_params.task_pointers)
        task_body = task.split('<output>')[1].split('</output>')[0]
        task_dict = {'task_body': task_body}
        return task_dict
    except Exception as inst:
        return{'task_body': ''}

@app.post('/generate_note')
async def main(input_params: NoteInput):
    try:
        note = await create_note(input_params.note_topic,input_params.no_of_words, input_params.note_pointers)
        note_body = note.split('<output>')[1].split('</output>')[0]
        note_dict = {'note_body': note_body}
        return note_dict
    except Exception as inst:
        return{'note_body': ''}

@app.post('/generate_action')
async def main(input_params: ActionInput):
    try:
        action = await create_action(input_params.action_topic,input_params.no_of_words, input_params.action_pointers)
        action_body = action.split('<output>')[1].split('</output>')[0]
        action_dict = {'action_body': action_body}
        return action_dict
    except Exception as inst:
        return{'action_body': ''}

@app.post('/generate_message')
async def main(input_params: MessageInput):
    try:
        message = await create_message(input_params.message_topic,input_params.no_of_words, input_params.message_pointers)
        message_body = message.split('<output>')[1].split('</output>')[0]
        message_dict = {'message_body': message_body}
        return message_dict
    except Exception as inst:
        return{'message_body': ''}

@app.post('/generate_comment')
async def main(input_params: CommentInput):
    try:
        comment = await create_comment(input_params.no_of_words, input_params.comment_pointers)
        comment_body = comment.split('<output>')[1].split('</output>')[0]
        comment_dict = {'comment_body': comment_body}
        return comment_dict
    except Exception as inst:
        return{'comment_body': ''}

@app.post('/tag_intent')
async def main(input_params: IntentInput):
    try:
        intent_response = await tag_intent(input_params.email_body)
        print('intent_response : ',intent_response)
        intent = intent_response.split('<output>')[1].split('</output>')[0]
        intent = intent.replace('\n','')
        intent_list = json.loads(intent.replace("'", '"'))
        if 'no issue' in intent_list:
            intent_list.remove('no issue')
             
        print('intent_list_final : ' ,list_intersection(intent_list, CONCERNS))
        intent_list_final = list_intersection(intent_list, CONCERNS)
        
        intent_dict = {'tag': intent_list_final}
        
        return intent_dict
    except Exception as inst:
        return{'tag': []}
    
@app.post('/tag_emotion')
async def main(input_params: EmotionInput):
    
    try:
        emotion_response = await tag_emotion(input_params.email_body)
        print('emotion_response : ',emotion_response)
        emotion = emotion_response.split('<output>')[1].split('</output>')[0]
        emotion = emotion.replace('\n','')
        emotion_list = json.loads(emotion.replace("'", '"'))
        emotion_list = list(flatten(emotion_list))
             
        print('emotion_list_final : ' ,list_intersection(emotion_list, EMOTIONS))
        emotion_final_list = list_intersection(emotion_list, EMOTIONS)
        
        emotion_dict = {'tag': emotion_final_list}
        
        return emotion_dict
    except Exception as inst:
        return{'tag': []}
    
@app.post('/tag_sentiment')
async def main(input_params: SentimentInput):
    
    try:
        email_body = extract_email_body_new(input_params.email_body)
        if len(email_body) < 1850:
            sentiment_response = await tag_sentiment_hf(email_body)
        else:
            sentiment_response = await tag_sentiment(email_body)
            sentiment_response = json.loads(sentiment_response)
            
        print('sentiment_response : ',sentiment_response)
        if 'label' in sentiment_response and 'score' in sentiment_response and sentiment_response["label"] in SENTIMENTS:
            return sentiment_response
        else:
            return{'label': '', 'score' : 0}
    except Exception as inst:
        print(' exception : ',inst)
        return{'label': '', 'score' : 0}
    
@app.post('/summarize')
async def main(input_params: SummarizeInput):
    
    
    try:
        summary = await summarize(input_params.zapscore,input_params.zs_percentile_score,input_params.customer_name,input_params.zapscore_change, input_params.usage_score_change, input_params.gutfeel_score_change, input_params.tickets_score_change, input_params.features_score_change, input_params.comms_score_change, input_params.payments_score_change, input_params.total_tasks, input_params.total_messages, input_params.total_actions, input_params.page_visits, input_params.pinned_features_used,input_params.churn_prob,input_params.aggregation)
        print('*'*100)
        print('summary : ',summary)
        print('*'*100)
        summary = summary.split('<output>')[1].split('</output>')[0]
        summary_dict = {'summary': summary}
        
        return summary_dict
    except Exception as inst:
        return{'summary': ''}
    
@app.post('/summarize_v2')
async def main(input_params: SummarizeInputV2):
    try:
        summary = await summarize(input_params.zapscore,input_params.zs_percentile_score,input_params.name,input_params.zapscore_change, input_params.usage_score_change, input_params.gutfeel_score_change, input_params.tickets_score_change, input_params.features_score_change, input_params.comms_score_change, input_params.payments_score_change, input_params.total_tasks, input_params.total_messages, input_params.total_actions, input_params.page_visits, input_params.pinned_features_used,input_params.churn_prob,input_params.aggregation, input_params.summ_type)
        print('*'*100)
        print('summary : ',summary)
        print('*'*100)
        summary = summary.split('<output>')[1].split('</output>')[0]
        summary_dict = {'summary': summary}
        
        return summary_dict
    except Exception as inst:
        return{'summary': ''}
    
@app.post('/summarize_email')
async def main(input_params: EmailSummarizeInput):
    try:
        summary = await summarize_email(input_params.email_body)
        print('*'*100)
        print('summary : ',summary)
        print('*'*100)
        if '<output>' in summary:
            summary = summary.split('<output>')[1].split('</output>')[0]
        elif 'summary:' in summary:
            summary = summary.split('summary:')[1]
        summary_dict = {'summary': summary}
        
        return summary_dict
    except Exception as inst:
        return{'summary': ''}
    
@app.post('/churn_reason')
async def main(input_params: ChurnReasoningInput):
    try:
        reason = await churn_reason(input_params.customer_name, input_params.percent_this_c2_is_red_in_last_30_days, input_params.percent_this_c2_is_green_in_last_30_days, input_params.percent_this_c2_is_yellow_in_last_30_days, input_params.percent_this_c2_is_grey_in_last_30_days,input_params.churn_prob)
        print('*'*100)
        print('churn_reason : ',reason)
        print('*'*100)
        reason = reason.split('<output>')[1].split('</output>')[0]
        reason_dict = {'churn_reason': reason}
        
        return reason_dict
    except Exception as inst:
        return{'churn_reason': ''}
    
# @app.post('/churn_reason')
# async def main(input_params: ChurnReasoningInput):
#     reason = await churn_reason(input_params.customer_name, input_params.percent_this_c2_is_red_in_last_30_days, input_params.percent_this_c2_is_green_in_last_30_days, input_params.percent_this_c2_is_yellow_in_last_30_days, input_params.percent_this_c2_is_grey_in_last_30_days,input_params.churn_prob)
#     print('*'*100)
#     print('churn_reason : ',reason)
#     print('*'*100)
    
#     try:
#         churn_reason = reason.split('<output>')[1].split('</output>')[0]
#         churn_reason_dict = {'churn_reason': churn_reason}
        
#         return churn_reason_dict
#     except Exception as inst:
#         return{'churn_reason': ''}

# if __name__ == '__main__':
#     uvicorn.run(app, port=8000, host='127.0.0.1')