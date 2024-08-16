#IMPORTS
from openai import OpenAI
from dotenv import load_dotenv
import sys
from get_info import get_location, get_price
import json

#SETTINGS
#load env variables
load_dotenv()
#set client api
client = OpenAI()

location = get_location()
price = get_price()
prompt = f'Can you write me a list of 30 hotels and their e-mails in {location}. The price from 1 to 5 has to be {price}'


#API - get the e-mail from ChatGPT
def get_emails_hotels():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant whose role is to search up for a certain number of hotels in a city and the e-mails in their websites. The Hotels must exist in real life, not invented, and the e-mails have to be the real ones of those hotels, displayed in those websites. It is also important that the hotels are actually in the given city. If the given city is, for example, Rome, you cannot output the Hilton Hotel Times Square, because it is in New York City, but you could, instead, output the Singer Palace Hotel, because it is located in Rome. This was just an example, but this counts for every city: you must not output an hotel that is not located in the given city. The answer must be a python dictionary, with the hotel names as keys and each e-mail as value. Nothing else should be written, excpet from the dictionary, not even the word python. If the location does not exist, the output should be 'Location does not exist.'. Also keep in mind to output exactly 30 hotels and emails, and with the right price, on a scale from 1 to 5, given in the prompt."},
            {"role": "user", "content": prompt}
        ]
    )

    #extract the response and convert the string to a dict
    extract = json.loads(response.choices[0].message.content)

    #extract hotels and e-mails and put them in 2 separate lists
    hotels = list(extract.keys())
    emails = list(extract.values())


    return hotels, emails