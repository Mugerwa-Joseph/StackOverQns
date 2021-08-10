import requests
import json

# Simple app to check for questions from stack overflow which are not yet answered.
url = 'http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'

response = requests.get(url)

#print(response)

# To see the data returned
#print(response.json())
# Finetune the output
#print(response.json()['items'])

# You could loop over the results as follows
for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])

    else:
        print("Question answered already")
    print()
