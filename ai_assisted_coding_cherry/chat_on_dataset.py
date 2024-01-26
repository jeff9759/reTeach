# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/chat_dataset.ipynb.

# %% auto 0
__all__ = ['chat_on_dataset']

# %% ../nbs/chat_dataset.ipynb 1
import openai
import pandas as pd

# %% ../nbs/chat_dataset.ipynb 2
def chat_on_dataset(message, history, file=None):
    messages = []
    if history:
        # convert the history correspondingly to the format of OpenAI, the first message is always from the user, the second is from the bot
        for message_tuple in history:
            if message_tuple[0] != "Start Chating!":
                messages.append({"role": "user", "content": message_tuple[0]})
                messages.append({"role": "assistant", "content": message_tuple[1]})
    elif message is None:
        history = []
        messages = [{"role": "system", "content": "Start Chatting!"}]


    # If a file is uploaded, read it as a DataFrame and convert it to string
    if file is not None:
        try:
            df = pd.read_csv(file.name)
            processed_csv_message = df.to_string()
        except Exception as e:
            processed_csv_message = f"Failed to read the file: {e}"
        
        message += f"The csv file is as following: \n\n{processed_csv_message}"
    
    messages.append({"role": "user", "content": message})

    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    bot_response = response.choices[0].message['content']
    # print(bot_response)
    # Append the bot's response to the history
    # history.append((message, bot_response))

    return bot_response