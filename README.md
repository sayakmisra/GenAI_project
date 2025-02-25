## GenAI

To run the LLM, we need to install Ollama :
`curl -fsSL https://ollama.com/install.sh | sh`

Download the llama3 model :
`ollama run llama3:instruct`

To run the python/uvicorn server :
` uvicorn src.fastapi_api.app:app --reload ` 
or 
`fastapi run src/fastapi_api/app.py`

To test the GenAI server:
`python src/fastapi_api/client.py`

The various endpoints are: 

`/generate_email` ----> to generate email.
Call the endpoint, with a payload like :
`{'email_topic':"contract termination",'no_of_words':"80", 'style':"Formal", 'sender':"Sayak", 'recipient':"Arnab", 'pointers':"Horrible service"}`

`/generate_task` ----> to generate task body.

Call the above endpoint with the payload :
`{'task_topic':"contract termination",'no_of_words':"80"}`

`/generate_action` ----> to generate action body.

Call the above endpoint with the payload :
`{'action_topic':"contract termination",'no_of_words':"80"}`

`/generate_message` ----> to generate message body.

Call the above endpoint with the payload :
`{'message_topic':"contract termination",'no_of_words':"80"}`

`/generate_note` ----> to generate note body.

Call the above endpoint with the payload :
`{'note_topic':"contract termination",'no_of_words':"80"}`






# GenAI_project
