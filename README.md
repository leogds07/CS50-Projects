# ** Hotel Automation **
 ** Purpose of the Program:  ** It asks the user some infos, such as, the name, the e-mail, a location, dates ecc. and it sends a booking request email to 30 hotels, in that location. It is very useful, as people always have to do this operation manually, usually searching up for hotels on booking.com and then sending them an email not to pay the extra booking commission.

 ## ** Important Files **
 - get_info.py
 - get_emails_hotels.py
 - generate_email.py
 - send_email.py
 - handle_password.py
 - main.py

 ## ** Secondary Folders and Files **
 - DRAFTS folder
 - FUTURE IMPROVEMENTS folder
 - not useful anymore folder
 - venv folder
 - __pycache__ folder
 - .env
 - .gitignore
 - requirements.txt 

* Let's get through the important ones *

## ** get_info.py **
The get_info.py file collects all the user's infos necessary for the program to run (and validates them), such as:
- name
- phone
- location
- check in date
- check out date
- number of adults
- number of children
- age of children (if any)
- number of rooms
- e-mail
- app password
- preferred price (on a scale from 1 to 5)

* Imports from other files:  *
```
    from handle_password import generate_key, load_key, encrypt_message
```

## ** get_emails_hotels.py **
This file connects to the OpenAI API to reach the ChatGPT model:
```
    model="gpt-4o-mini"
```
The system is given this instruction:
```
    {"role": "system", "content": "You are an assistant whose role is to search up for a certain number of hotels in a city and the e-mails in their websites. The Hotels must exist in real life, not invented, and the e-mails have to be the real ones of those hotels, displayed in those websites. It is also important that the hotels are actually in the given city. If the given city is, for example, Rome, you cannot output the Hilton Hotel Times Square, because it is in New York City, but you could, instead, output the Singer Palace Hotel, because it is located in Rome. This was just an example, but this counts for every city: you must not output an hotel that is not located in the given city. The answer must be a python dictionary, with the hotel names as keys and each e-mail as value. Nothing else should be written, excpet from the dictionary, not even the word python. If the location does not exist, the output should be 'Location does not exist.'. Also keep in mind to output exactly 30 hotels and emails, and with the right price, on a scale from 1 to 5, given in the prompt."},

```
and this prompt:
```
prompt = f'Can you write me a list of 30 hotels and their e-mails in {location}. The price from 1 to 5 has to be {price}'
```
* Imports from other files:  *
```
    from get_info import get_location, get_price
```
The location and the price are needed to be in the prompt

The function in this file returns 2 lists: 30 hotels and 30 hotel e-mails


## ** generate_email.py **
This files generates two different types of emails, using most of the infos given by the user, depending on the case if the user either has children or not

It returns a list of 30 e-mails, corresponding to the 30 hotels.

* Imports from the other files:  *
```
from get_emails_hotels import get_emails_hotels
from get_info import get_name, get_phone, get_rooms, check_in, check_out, adults, children, get_age
```

## ** send_email.py **
This file sends all the emails to all the corresponding hotels, using the SMTP and the MIMEText libraries.
It logs in to Gmail, using the user's email and app password, that can be found via this instructions, given in the * get_info.py * file:
```
    pwd = input("\n///\nYou have to write Gmail's app password.\nGo to your Google Account and Log In\n-> Security\n-> Check if 2 step verification is active (if not, activate it)\n-> Search in the search bar 'App Password'\n-> Add an app password for Gmail\nALERT! Remember to take a screenshot, because you will not be able to check the password again.\nIf you forgot to take a screenshot, you will have to delete the password and generate a new one.\nApp Password: ")
```
handling errors such as:
```
    except smtplib.SMTPAuthenticationError:
        sys.exit('Unable to sign in')
```
or
```
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {receiver}: {str(e)}")
```

When the process is completed, a.k.a., all the e-mails have been sent, the program prints: * Process Completed! *


* Imports from the other files:  *
```
from generate_email import generate_emails
from get_info import get_email, get_pwd
from handle_password import load_key, decrypt_message
from get_emails_hotels import get_emails_hotels
```

## ** handle_password.py **
This file uses the cryptography.fernet library to:
1. Generate a key -> used in get_info.py when asking for the password
2. Load that key -> used in get_info.py when asking for the password; used in send_email.py as the password is needed to log in Gmail
3. Encrypt the password using that key -> used in get_info.py when asking for the password
4. Decrypt the password using that key -> used in send_email.py as the password is needed to log in Gmail

## ** main.py **
This file calls the send_emails() function imported from send_email.py, running the program.

It also deletes the key files, blocking hackers' attempts to steal it, and handles possible errors if that file, for example doesn't exist:
```
    #delete key file and handle possible errors
    file_path = 'python/secret.key'
    try:
        os.remove(file_path)
        print('The key file has been deleted successfully.')
    except FileNotFoundError:
        sys.exit(f'{file_path} does not exist')
    except PermissionError:
        sys.exit(f'Permission denied: {file_path} cannot be deleted')
    except Exception as e:
        sys.exit(f'Error: {e}')
```


SPDX-FileCopyrightText: © 2024 Leonardo Giuliani de Santis <leogiulianidesantis@gmail.com>

SPDX-License-Identifier: BSD-3-Clause
