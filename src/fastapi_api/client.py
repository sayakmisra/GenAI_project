import requests
import time
import sys,os
sys.path.append(os.getcwd())


from src.config import DEV_URL, PROD_URL

# DEV_URL = 'http://0.0.0.0:8000'
# PROD_URL = 'http://35.171.18.228:8000'

start = time.time()
base_url = PROD_URL


email_url = base_url + '/generate_email'
task_url = base_url + '/generate_task'
note_url = base_url + '/generate_note'
message_url = base_url + '/generate_message'
comment_url = base_url + '/generate_comment'
action_url = base_url + '/generate_action'
intent_tagging_url = base_url + '/tag_intent'
emotion_tagging_url = base_url + '/tag_emotion'
sentiment_tagging_url = base_url + '/tag_sentiment'
respond_email_url = base_url + '/respond_email'
summarize_url = base_url + '/summarize'
summarize_url_v2 = base_url + '/summarize_v2'
summarize_email_url = base_url + '/summarize_email'
churn_reason_url = base_url + '/churn_reason'


email_obj = {'email_topic':"contract termination",'no_of_words':"80", 'style':"Formal", 'sender':"Sayak", 'recipient':"Arnab", 'pointers':"Horrible service"}
task_obj = {'task_topic':"complete onbaording of all the new customers",'no_of_words':"80",'task_pointers':'give product KT\n give induction\n complete documentation'}
note_obj = {'note_topic':"contract termination",'no_of_words':"80",'note_pointers':'give product KT\n give induction\n complete documentation'}
message_obj = {'message_topic':"contract termination",'no_of_words':"80",'message_pointers':'give product KT\n give induction\n complete documentation'}
comment_obj = {'no_of_words':"80",'comment_pointers':'aaaaa'}
action_obj = {'action_topic':"contract termination",'no_of_words':"80",'action_pointers':'give product KT\n give induction\n complete documentation'}
churn_reason_obj = {'customer_name':"Adidas",'churn_prob':'very low','percent_this_c2_is_red_in_last_30_days':0, 'percent_this_c2_is_green_in_last_30_days' : 100, 'percent_this_c2_is_yellow_in_last_30_days' : 0,'percent_this_c2_is_grey_in_last_30_days' : 0 }
summarize_obj = {'zapscore':13,'zs_percentile_score':91,'customer_name':"Nike",'zapscore_change':12,'aggregation':'month','churn_prob':'low','usage_score_change':5,'gutfeel_score_change':-17,'tickets_score_change' : -7,'features_score_change':13, 'comms_score_change':-5,'payments_score_change':1, 'total_tasks':39, \
    'total_messages':27,'total_actions': 13, 'page_visits':36,'pinned_features_used':5 }
summarize_obj_v2 = {'zapscore':13,'zs_percentile_score':91,'name':"Nike",'zapscore_change':12,'aggregation':'month','churn_prob':'low','usage_score_change':5,'gutfeel_score_change':-17,'tickets_score_change' : -7,'features_score_change':13, 'comms_score_change':-5,'payments_score_change':1, 'total_tasks':39, \
    'total_messages':27,'total_actions': 13, 'page_visits':36,'pinned_features_used':5 , 'summ_type' : 'customer segment'}

email_body = ''' 
--
Cheers,
Manasij Ganguli
Co-Founder & CEO, ZapScale
+91-852-763-5398

---------- Forwarded message ---------
From: Deepak Paripati (via Google Slides) <
drive-shares-dm-noreply@google.com>
Date: Tue, Oct 1, 2024, 18:00
Subject: Presentation shared with you: ‘Nektar - Intro meeting deck’
To: <manasij@zapscale.com>


Deepak Paripati shared a presentation
[image: Header profile photo]
Deepak Paripati (deepak@nektar.ai) has invited you to *view* the following
presentation until 30 Oct, 21:00 GMT-7:
Nektar - Intro meeting deck
<https://docs.google.com/presentation/d/1YFvLq4wCevHxd49T8rF9qjB_bDGq-Q2N7hIvwNqRdtk/edit?usp=sharing_eil&ts=66fbeb6e>

Deepak Paripati <deepak@nektar.ai> is outside your organisation.
Open
<https://docs.google.com/presentation/d/1YFvLq4wCevHxd49T8rF9qjB_bDGq-Q2N7hIvwNqRdtk/edit?usp=sharing_eip&ts=66fbeb6e>
If you don't want to receive files from this person, block the sender
<https://drive.google.com/drive/blockuser?blockerEmail=manasij@zapscale.com&blockeeEmail=deepak@nektar.ai&usp=sharing_eib>
from Drive
Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA
<https://www.google.com/maps/search/1600+Amphitheatre+Parkway,+Mountain+View,+CA+94043,+USA?entry=gmail&source=g>
You have received this email because deepak@nektar.ai shared a presentation
with you from Google Slides. [image: Google] <https://workspace.google.com/>



'''

# email_body = ''' 
# Hello,

# Not Really happy with your effort, some complains.
# '''

email_body1 = ''' 
\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <jegan@infisign.io>,  <dilip@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>\nkeeping no-reply <kundan@zapscale.com> in CC\n==============================\n\nHey Jegan,\n\n\nBased on our whatsapp conversation, sending you this email (plus Dilip, Saran and Kapil - whose emails you shared).\n\n\nJust to introduce us, I am running my 2nd SaaS business (built, scaled and sold my last startup for an all-cash deal). Now, I am\nbuilding ZapScale CS solution.\nA bunch of SaaSBoomi founders are using our CS product (ExtraaEdge, Convin, Phyllo, Astra, Xebo, Taggbox, Sheshi, Spyne, Zluri,\nDatoms, Nakad, JOP, SimpliSmart etc) and have seen very good results.\nWe also have great feedback from our customers.\nimage.png\n[https://stage.assets.zapscale.com/inbox/attachments/c1_62ea0a1e12cffd3a5b125035/inbox_6666c7a28f967648d13ce3f1/message_66f3d6ec56dfec52c178ce8e/image.png?Expires=4882951502&amp;Key-Pair-Id=K60N0IBA3IPFT&amp;Signature=eHfhOemJ1lRWwe-MqixWamA2GiMAwQmJh2UnP1WeagfUwYlwTVsH5OKG9YWl7wBpiom-8meJHlDmfJmtaMNbgUjx8-FP7tjUtjLnPnd42fgxB1g4pbhGQdzVqL1CgJ2aiVlv3rCIq-whACnfIsry19bh6Odnwn7rSI4cIB~pvmz~5SaNZNPlMkaCpQOMcyWGiGMUnHzD~yACSsUo6gVSOQ4zl2jTXcBefU50uBuu8xlhl23O0NsYCDRrGf57qxBSbqWo0juMZd6fJUbwZ6Vyoq-Q~EWhm7FwJrKYUClfmL-qePcOitJt1iELz-xL0C5T4St0cfeuwkPmZKkWBQJPKw__]\n\n\n\nWould love to show you ZapScale.\n\nPlease book a time with me at a date/time that is convenient to you here:\n\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\nLook forward to meeting you :-) \n\n\n\n--\nCheers,\nManasij Ganguli\nCEO, ZapScale\nWhatsApp: +91-852-763-5398 | LinkedIn\n[https://d2Bbff04.na1.hs-sales-engage.com/Ctc/L0+23284/d2Bbff04/JkM2-6qcW6N1vHY6lZ3m8W6s1xHc5qtnYBW98_8M-320Y98W16xd052L6b5JV9NFpY3gXpq_N33TZ3LSlPk6W2Fjm1H903dLGW3y8Q_-2-1PWtW2T50LW28tQYDW6CrpPq1FPLrJW5JxPrW17V--hV-qM_j8cBm92W55SWPm1RXzy8W321Kcz6xCvCpW1Cb69S1_0-nqW1dMdVb994Y-hMYznHg-rhJDW1Y4TBG6vN-fgW6_YsbC77QDkbN5gl4Sm3bsW1W7HhBpH3rDctsW4HtLR22h76V5W4QGrB898C2TPf757VPW04]\n| Twitter\n[https://d2Bbff04.na1.hs-sales-engage.com/Ctc/L0+23284/d2Bbff04/JkM2-6qcW6N1vHY6lZ3pQW4DBwW16wqWPpW8PVgDv6w2ZbkW738bTv4DDrLTW7T151Z1hNVJJW3yqqf181cS9PW6LRtrM1KrPKJW3bjvQ535GQHqW214f2-6PgJTjW5JrhHh7qfJRjW2ZQ3p52hnfYlW3-J6jY7wd_5kW275-_45Y62MqW4977Cd1k3xQLW42hnq486tNrZW5r9Djk6pP8PkW1ghVB73llrbYW6BDKWf7qvlMtW5Y2z6B4ql7V2W7drdVg8g7Wl5Vqm8H-13FGrSN3BSm6h20HNmW3StM8X8Vhy6Nf2mKMr604] \n[https://d2Bbff04.na1.hs-sales-engage.com/Cto/L0+23284/d2Bbff04/R5R8b45rhN6N5FmG2fDlSW1X1p2822YpdqW1Q6BcB1X2j6gW1GysHG1N36dvW3C645s1XnbmLW3LHcJP1Y_Y0-n1--W8l4W1]\n\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nWe can connect Monday 3pm ist. If this time works, please send me the invite.\n\n\n-Dilip\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nWe can connect Monday 3pm ist. If this time works, please send me the invite.\n\n\n-Dilip\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHey Dilip,\n\n\nCan you do Monday 430 to 530?\nIf not, can you please choose a date and time of your convenience here: https://meetings.hubspot.com/manasij-ganguli\n[https://meetings.hubspot.com/manasij-ganguli]\n\n\n--\nCheers,\nManasij Ganguli\nCo-Founder & CEO, ZapScale\n+91-852-763-5398\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\n5.30 pm works.\n\n\n-Dilip\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Dilip,\n\n\nI was asking for 430 to 530 meeting. \nI can't do 530 pm on Monday. \nCan you please book a meeting on my calendar as per your convenience https://meetings.hubspot.com/manasij-ganguli\n[https://meetings.hubspot.com/manasij-ganguli]\n\n\n--\nCheers,\nManasij Ganguli\nCo-Founder & CEO, ZapScale\n+91-852-763-5398\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Dilip,\n\n\nAre you able to find a date / time that works for you?\n\nPlease book a time with me at a date/time that is convenient to you here:\n\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\n\n\n__________________________________\nCheers,\nManasij Ganguli\nCo-Founder and CEO\n+91 852 763 5398 |  LinkedIn [https://www.linkedin.com/in/mganguli/] | Twitter [https://twitter.com/theManasij]\n\nZapScale logo.png [cid:ii_l1adoykq8]\nwww.zapscale.com [http://www.zapscale.com] | Follow us on LinkedIn [https://www.linkedin.com/company/zapscale]\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Dilip,\n\n\nAre you able to find a date / time that works for you?\n\nPlease book a time with me at a date/time that is convenient to you here:\n\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\n\n\n__________________________________\nCheers,\nManasij Ganguli\nCo-Founder and CEO\n+91 852 763 5398 |  LinkedIn [https://www.linkedin.com/in/mganguli/] | Twitter [https://twitter.com/theManasij]\n\nZapScale logo.png [cid:ii_l1adoykq8]\nwww.zapscale.com [http://www.zapscale.com] | Follow us on LinkedIn [https://www.linkedin.com/company/zapscale]\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Dilip,\n\n\nAre you able to find a date / time that works for you?\n\nPlease book a time with me at a date/time that is convenient to you here:\n\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\n\n\n__________________________________\nCheers,\nManasij Ganguli\nCo-Founder and CEO\n+91 852 763 5398 |  LinkedIn [https://www.linkedin.com/in/mganguli/] | Twitter [https://twitter.com/theManasij]\n\nZapScale logo.png [cid:ii_l1adoykq8]\nwww.zapscale.com [http://www.zapscale.com] | Follow us on LinkedIn [https://www.linkedin.com/company/zapscale]\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Dilip,\n\n\nAre you able to find a date / time that works for you?\n\nPlease book a time with me at a date/time that is convenient to you here:\n\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\n\n\n__________________________________\nCheers,\nManasij Ganguli\nCo-Founder and CEO\n+91 852 763 5398 |  LinkedIn [https://www.linkedin.com/in/mganguli/] | Twitter [https://twitter.com/theManasij]\n\nZapScale logo.png [cid:ii_l1adoykq8]\nwww.zapscale.com [http://www.zapscale.com] | Follow us on LinkedIn [https://www.linkedin.com/company/zapscale]\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>, vijina <vijina@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nI am looping Vijina. She will look into it. \n\n\n@Vijina - Please check their product and see if it’s fits for Infisign and entrans. \n\n\nThank you,\n-Dilip\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>, vijina <vijina@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nI am looping Vijina. She will look into it. \n\n\n@Vijina - Please check their product and see if it’s fits for Infisign and entrans. \n\n\nThank you,\n-Dilip\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>, vijina <vijina@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nI am looping Vijina. She will look into it. \n\n\n@Vijina - Please check their product and see if it’s fits for Infisign and entrans. \n\n\nThank you,\n-Dilip\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>, vijina <vijina@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nI am looping Vijina. She will look into it. \n\n\n@Vijina - Please check their product and see if it’s fits for Infisign and entrans. \n\n\nThank you,\n-Dilip\n\n==============================\n <dilip@infisign.io> wrote to \n Manasij Ganguli <manasij@zapscale.com>, vijina <vijina@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Manasij,\n\n\nI am looping Vijina. She will look into it. \n\n\n@Vijina - Please check their product and see if it’s fits for Infisign and entrans. \n\n\nThank you,\n-Dilip\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>, vijina <vijina@infisign.io>\nkeeping  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Vijina,\n\n\nCan we set up some time next week please?\nPlease book a time with me at a date/time that is convenient to you here:\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\n\n\n--\nCheers,\nManasij Ganguli\nCEO, ZapScale\nWhatsApp: +91-852-763-5398 | LinkedIn [https://www.linkedin.com/in/mganguli/] | Twitter [https://twitter.com/theManasij]\n\n==============================\nManasij Ganguli <manasij@zapscale.com> wrote to \n  <dilip@infisign.io>\nkeeping vijina <vijina@infisign.io>,  <jegan@infisign.io>,  <saran@infisign.io>,  <kapil@infisign.io>, no-reply <kundan@zapscale.com> in CC\n==============================\n\nHi Jegan / Dilip / Saran / Kapil / Vijina,\n\n\nHope you are doing well.\nI hope looking at a Customer Success solution is still something you are interested in.\nShall we aim to meet sometime this week?\n\n\n\nPlease book a time with me at a date/time that is convenient to you here:\n\nhttps://meetings.hubspot.com/manasij-ganguli [https://meetings.hubspot.com/manasij-ganguli]\n\n\n\n--\nCheers,\nManasij Ganguli\nCEO, ZapScale\nWhatsApp: +91-852-763-5398 | LinkedIn\n[https://d2Bbff04.na1.hs-sales-engage.com/Ctc/L0+23284/d2Bbff04/JkM2-6qcW6N1vHY6lZ3l1W7sk5Dy5zkV4KW8vxXmB8pcW2dW6j5VH41cLs0vW83GJR14rXMpkVl8lN32vrf_mN6Y59ZpMLcgnW66MdHK8v91yWW35YNdb20j-MkW3g2Cnl8zRYsdW89gXFX7sHRzxW5-qw1t4YnyNmW1Z3tLP91FsJFW5RJ9tg7YkLvYW6Wrtcs8g1TbvW4VPdck4d8LYtW6qj7JQ5MfnHkW7BFz555LZYrDW8JDLlB69LVtGW1h1tFd1w6rLnV9MkLG4BdXNpW2XBKNQ3qDR5QV4bFl81yZ65kf1t-jJF04]\n| Twitter\n[https://d2Bbff04.na1.hs-sales-engage.com/Ctc/L0+23284/d2Bbff04/JkM2-6qcW6N1vHY6lZ3pvW2xSx113pl6NtW8glSLd6s2LqRW7XJCF01mj61GMWrKv-R8N38MnyJPtCzNzdW20FrMs308nFwW1Q3Wy_8Z9XRwW56RQdR5BhK_8W7wd8K88v0HqGW1kg9xd3KK5ppN1W3rfg6VtfWW3mPYJb6-wRW-W6Cd9c31CLSTzW22vLRs7zj4fnW8cz6zw1d7rxTW2ClGbw5zBqxCN5SFLCvMwGrDVf97dX5RnCdqW23pYRx7hwPrlW99FVRF1s9KfxW1BZvWR4-HV1CW3X2CnD98zV6kf8qn8pY04]"
'''

tag_intent_obj = {'email_body':email_body}
tag_emotion_obj = {'email_body':email_body}
tag_sentiment_obj = {'email_body':email_body}
respond_email_obj = {'prev_email':email_body,'no_of_words':"80", 'style':"Formal", 'sender':"Sayak", 'recipient':"Arnab"}
summarize_email_obj = {'email_body':email_body1}


# response = requests.post(email_url, json = email_obj)
# response = requests.post(intent_tagging_url, json=tag_intent_obj)
# response = requests.post(churn_reason_url, json = churn_reason_obj)
response = requests.post(summarize_email_url, json = summarize_email_obj)

# print(comment_url)
# print(comment_obj)
print(response.json())

end = time.time()
print('It took {} seconds to finish execution.'.format(round(end-start)))

