#IMPORTS
import sys
from get_emails_hotels import get_emails_hotels
from get_info import get_name, get_phone, get_rooms, check_in, check_out, adults, children, get_age

#SETTINGS
name = get_name()
phone = get_phone()
hotels, emails = get_emails_hotels()
rooms = get_rooms()
check_in = check_in()
check_out = check_out()
adults = adults()
children = children()

#if there are children store their age in a list
if children > 0:
    children_age = []
    for child in range(children):
        child_age = get_age()
        children_age.append(child_age)

#generate two different types of e-mail message: #if there are children the e-mail message changes
def generate_emails() -> list:
    emails = []

    for hotel in hotels:
        if children > 0:
            email = f"Dear {hotel} Reservations Team,\nI hope this email finds you well. I am writing to inquire about the availability of rooms at your hotel for the following stay:\nCheck-in Date: {check_in}; \nCheck-out Date: {check_out}; \nNumber of Rooms Required: {rooms}; \nNumber of Adults: {adults}; \nNumber of Children: {children}; \nAge of Children: {children_age}.\nCould you please confirm the availability for the requested dates and provide me with the total cost of the stay? Additionally, if there are any special offers or packages available during this period, I would be grateful if you could share those details as well.\nPlease also let me know the process for securing the reservation, including any deposit requirements or cancellation policies.\nThank you in advance for your assistance. I look forward to your prompt response.\nBest regards,\n{name}\n{phone}"
            emails.append(email)
        else:
            email = f"Dear {hotel} Reservations Team,\nI hope this email finds you well. I am writing to inquire about the availability of rooms at your hotel for the following stay:\nCheck-in Date: {check_in}; \nCheck-out Date: {check_out}; \nNumber of Rooms Required: {rooms}; \nNumber of Adults: {adults}.\nCould you please confirm the availability for the requested dates and provide me with the total cost of the stay? Additionally, if there are any special offers or packages available during this period, I would be grateful if you could share those details as well.\nPlease also let me know the process for securing the reservation, including any deposit requirements or cancellation policies.\nThank you in advance for your assistance. I look forward to your prompt response.\nBest regards,\n{name}\n{phone}"
            emails.append(email)

    return emails
