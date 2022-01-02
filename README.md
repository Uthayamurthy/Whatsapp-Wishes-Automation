# Whatsapp Automated Wishes

Helps to send automated wishes to your contacts in Whatsapp at scheduled time using [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit/wiki) . Written for Raspberry pi. Will mostly work on other platform too. 
 > To run it on other platforms you may have to change certain delays in automations.py. Instructions is mentoned in comments. 

## Installation Instructions

- Install Selenium Chrome Driver. For Raspberry pi run -

```
sudo apt install chromium-chromedriver
```
For other platforms refer to - https://chromedriver.chromium.org/getting-started

- Install the required python dependencies.

```
pip install pywhatkit pyautogui schedule
```

- Clone this repository or download the zip and extract.

## How to use ?

- Open web.whatsapp.com and scan the qr code from your phone.

- Run data_file_generator.py to create a data file.

- Edit the main.py according to your needs. Editing instructions is mentioned as comments in the file.

- Run main.py.

- You will see the wishes being sent at the scheduled time !

> Please Don't Move your mouse or press any keyboard key when the program is running in its scheduled time.