from pydantic import BaseModel

class EmailInput(BaseModel):
    email_topic: str
    no_of_words: str
    style: str
    sender: str
    recipient: str
    pointers: str
    
class RespondEmailInput(BaseModel):
    prev_email: str
    no_of_words: str
    style: str
    sender: str
    recipient: str
    
class TaskInput(BaseModel):
    task_topic: str
    no_of_words: str
    task_pointers: str
    
class NoteInput(BaseModel):
    note_topic: str
    no_of_words: str
    note_pointers: str
    
    
class MessageInput(BaseModel):
    message_topic: str
    no_of_words: str
    message_pointers: str
    
class CommentInput(BaseModel):
    no_of_words: str
    comment_pointers: str
    
class ActionInput(BaseModel):
    action_topic: str
    no_of_words: str
    action_pointers: str
    
    
class IntentInput(BaseModel):
    email_body: str
    
class EmotionInput(BaseModel):
    email_body: str
    
class SentimentInput(BaseModel):
    email_body: str
    
class SummarizeInput(BaseModel):
    zapscore: int
    zs_percentile_score: int
    customer_name: str
    aggregation: str
    churn_prob: str
    zapscore_change: int
    usage_score_change: int
    gutfeel_score_change: int
    tickets_score_change: int
    features_score_change: int
    comms_score_change: int
    payments_score_change: int
    total_tasks: int
    total_messages: int
    total_actions: int
    total_messages: int
    pinned_features_used: int
    page_visits: int
    
class SummarizeInputV2(BaseModel):
    zapscore: int
    zs_percentile_score: int
    name: str
    aggregation: str
    churn_prob: str
    zapscore_change: int
    usage_score_change: int
    gutfeel_score_change: int
    tickets_score_change: int
    features_score_change: int
    comms_score_change: int
    payments_score_change: int
    total_tasks: int
    total_messages: int
    total_actions: int
    total_messages: int
    pinned_features_used: int
    page_visits: int
    summ_type: str
    
class ChurnReasoningInput(BaseModel):
    percent_this_c2_is_red_in_last_30_days: int
    percent_this_c2_is_green_in_last_30_days: int
    percent_this_c2_is_yellow_in_last_30_days: int
    percent_this_c2_is_grey_in_last_30_days: int
    customer_name: str
    churn_prob: str
    
    
    
class EmailSummarizeInput(BaseModel):
    email_body: str

