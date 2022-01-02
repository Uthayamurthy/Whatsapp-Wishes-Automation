import pywhatkit
from time import sleep
import pyautogui
import csv

def send_bulk_wishes(recipient_type, msg, data_file_name):
    country_code = '+91'
    print(f'Sending Messages To {recipient_type} ...')
    with open(data_file_name, 'r') as data_file:
        csv_reader = csv.DictReader(data_file)
        for data in csv_reader:
            try:
                print(f'Sending Wishes to {data["name"]} ...')
                contact_num = country_code + data['contact_number'] # Add the country code to the contact number
                sleep(4)
                pywhatkit.sendwhatmsg_instantly(contact_num, msg, 15, False) # Experiment and Change the Wait_time according to your platform. For RPi-3 it is 30.
                sleep(20) # Experiment and Change the delay according to your platform. For RPi-3 it is 20.
                # Presses Enter Key after a delay to send the message.
                pyautogui.press('enter') 
                sleep(5) # Experiment and Change the delay according to your platform. For RPi-3 it is 5.
                # Presses Ctrl+w to close the chrome tab.
                pyautogui.keyDown('ctrl')
                pyautogui.press('w')
                pyautogui.keyUp('ctrl')
                print('Successfully Sent !')
            except:
                print('Some error Occurred ..')


