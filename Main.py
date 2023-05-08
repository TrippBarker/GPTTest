import os
import openai

openai.api_key_path = 'D:\KEYS\TextAdvKey.txt'
model_engine = "text-davinci-003"
prompt = "[Prompt] I want to play a guessing game, I will be thinking of a number between 1 and 100, and I would like for you to guess the number, please model your responses to be sassy and use ecelctic language. For your first response, please provide your first guess."
chatlog = prompt

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 64,
    n = 1,
    stop = None,
    temperature = 0.5,
)
chatlog += "\n" + prompt
prompt = "[Prompt] We are playing a number guessing game, I am thinking of a number between 1 and 100 and you are trying to guess what my number is."

response = completion.choices[0].text
print(response)
guesses = "\nYou have already made the following guesses: \n"
userResponse = ""

running = True

while (running):
    userResponse = input("Enter response: ")
    if (userResponse == "yes"):
        chatlog += prompt + guesses + "\n[user says] You guessed the number correctly!"
        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt + guesses + "\n[user says] You guessed the number correctly!",
            max_tokens = 64,
            n = 1,
            stop = None,
            temperature = 0.75,
        )
        running = False
    else:
        chatlog += prompt + guesses + "\n[user says] " + userResponse + " please make another guess.\n------------------------------------------------------------------------------\n"
        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt + guesses + "\n[user says] " + userResponse + " please make another guess.",
            max_tokens = 64,
            n = 1,
            stop = None,
            temperature = 0.75,
        )
    response = completion.choices[0].text
    guesses += response + "\n"
    print(response)
with open('chatlog.txt', 'w') as f:
    f.write(chatlog)
