import requests

parameters= {
    "amount" : 10,
    "type" : "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data=data = response.json()['results']





# question_data = [{"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.",
#                   "correct_answer": "False",
#                   "incorrect_answers": ["True"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "Nutella is produced by the German company Ferrero.",
#                   "correct_answer": "False",
#                   "incorrect_answers": ["True"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "The Sun rises from the North.",
#                   "correct_answer": "False",
#                   "incorrect_answers": ["True"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "You can legally drink alcohol while driving in Mississippi.",
#                   "correct_answer": "True",
#                   "incorrect_answers": ["False"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "Pluto is a planet.",
#                   "correct_answer": "False", "incorrect_answers": ["True"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "When you cry in space, your tears stick to your face.",
#                   "correct_answer": "True",
#                   "incorrect_answers": ["False"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "One of Donald Trump&#039;s 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.",
#                   "correct_answer": "True", "incorrect_answers": ["False"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
#                   "correct_answer": "True",
#                   "incorrect_answers": ["False"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "The National Animal of Scotland is the Unicorn.",
#                   "correct_answer": "True",
#                   "incorrect_answers": ["False"]},
#                  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                   "question": "A pasodoble is a type of Italian pasta sauce.",
#                   "correct_answer": "False",
#                   "incorrect_answers": ["True"]}]
