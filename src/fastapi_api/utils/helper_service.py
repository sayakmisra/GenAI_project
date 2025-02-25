import re
import pandas as pd

# Python program to illustrate the intersection
# of two lists using set() and intersection()
def list_intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def remove_url(text):
    # Define a regular expression to match URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    # Remove URLs from the text
    text_without_urls = re.sub(url_pattern, '', text)
    text_without_urls = re.sub(r'\[#.*?\]', '', text_without_urls)

    return text_without_urls

def remove_special_char_lines(text):
    # Define a regular expression to match URLs
    url_pattern = re.compile(r'\n>\s.*')
    text_without_urls = re.sub(url_pattern, '', text)
    text_without_urls = re.sub(r'\n>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'\n>>>>>>>>>>>>>>>>>>>>>>>\s.*', '', text_without_urls)
    text_without_urls = re.sub(r'(?m)^\*\*\*\*\*.*\n?', '', text_without_urls)
    return text_without_urls

def remove_underscore(text):
    # Regular expression pattern for the underscore line
    # Define patterns for underscore line and dashed line
    underscore_line_pattern = r'\n[>\s]*[-_]{9,}\n'
    dashed_line_pattern = r'\n[-_]+.*?[-_]+\n'

    # Use re.split to split the text based on either pattern
    split_parts_underscore = re.split(underscore_line_pattern, text, maxsplit=1, flags=re.IGNORECASE | re.DOTALL)
    split_parts_dashed = re.split(dashed_line_pattern, text, maxsplit=1, flags=re.IGNORECASE | re.DOTALL)

    # Choose the split that produces two parts and select the one with the minimum index
    if len(split_parts_underscore) == 2 and len(split_parts_dashed) == 2:
        index_underscore = text.find(split_parts_underscore[0])
        index_dashed = text.find(split_parts_dashed[0])
        if index_underscore < index_dashed:
            content_before_line = split_parts_underscore[0].strip()
        else:
            content_before_line = split_parts_dashed[0].strip()
    elif len(split_parts_underscore) == 2:
        content_before_line = split_parts_underscore[0].strip()
    elif len(split_parts_dashed) == 2:
        content_before_line = split_parts_dashed[0].strip()
    else:
        content_before_line = text.strip()

    # print("content_before_line:\n", content_before_line)
    return content_before_line
    

def remove_greetings(text):
    # Regular expression to find the first occurrence and capture everything after
    greetings_pattern_first = r'\b(Hi|Hello|Dear|Greetings)\b\s*([^,\n]*[,\n]*)\s*(.*)'

    # Search for the first occurrence
    match_first = re.search(greetings_pattern_first, text, flags=re.IGNORECASE | re.DOTALL)

    if match_first:
        text_after_sal = match_first.group(3)
        # text_after_sal = match_first.group(2).strip()
        return text_after_sal
    
    return text
    
def remove_sender(text):
    sender_pattern = r'From: (.+?)(?:\n|<)'
    # Find the first occurrence of the sender pattern
    matches = list(re.finditer(sender_pattern, text, flags=re.IGNORECASE))
    
    if matches:
        first_match = matches[0]
        text_without_sender = text[:first_match.start()].strip()
        
    # if match_sender:
    #     # Take only the text before the sender pattern
    #     text_without_sender = text.split(match_sender.group(0))[0].strip()
    #     print("text_without_sender\n", text_without_sender)
        
        #case when there is no greetings and the email starts with from,to pattern block
        if not text_without_sender:
            # Define the pattern to match the block of text
            pattern_to_remove = re.compile(r'''
                From: .+?                 # Match "From:" and everything until the next line
                Sent: .+?                 # Match "Sent:" and everything until the next line
                To: .+?                   # Match "To:" and everything until the next line
                Subject: .+?              # Match "Subject:" and everything until the next line
            ''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

            text_without_sender = re.sub(pattern_to_remove, '', text)    

        return text_without_sender       
    
    return text
    
def remove_signature(text):
    # # Updated regular expression
    # signature_pattern = r'^.*\b(Best Regards|Best|Regards|Thanks|Thank you|Thanks and Regards|)\b'

    # match_sign = re.search(signature_pattern, text, flags=re.IGNORECASE)
    # # print(match)

    # if match_sign:
    #     content = text[:match_sign.start(1)]
    #     return content

    signature_pattern = r'\b(?:Best Regards|Regards|Thanks,|Thank you,|Thanks and Regards|Sincerely|Yours|Yours truly|Yours sincerely|Sincerely,|The information in this e-mail is confidential|Cheers,|<div>|<html>|WARNING: max output size exceeded,|Join with Google Meet |Meeting ID:)\b'

    matches = list(re.finditer(signature_pattern, text, flags=re.IGNORECASE))
    if matches:
        last_match = matches[-1]
        # print('last_match : ',last_match)
        content_before_last_signature = text[:last_match.start()].strip()
        return content_before_last_signature
    
    return text
    

def extract_email_body_new(text):

    content_before_underscore = remove_underscore(text)
    content_after_greater_symbol_removed = remove_special_char_lines(content_before_underscore)
    # content_after_start_symbol_removed = remove_star_lines(content_after_greater_symbol_removed)

    text_without_sender = remove_sender(content_after_greater_symbol_removed)

    # text_after_sal = remove_greetings(text_without_sender)

    parsed_email_without_urls = remove_url(text_without_sender)

    text_after_sal = remove_greetings(parsed_email_without_urls)

    final_content = remove_signature(text_after_sal)

    return final_content 