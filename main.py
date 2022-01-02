from automation import send_bulk_wishes
import schedule
from time import sleep

def main():
    # Recipient_type , message and data_file_name nested list. Change this according to your needs before you run this file.
    rmdf = [['friends','This is a test','friends.csv']]

    for recipient, msg, data_file in rmdf:
        send_bulk_wishes(recipient, msg, data_file)

if __name__ == '__main__':
    scheduled_time = '00:00'
    schedule.every().day.at(scheduled_time).do(main) # Schedules the wishes

    while True:
        for n in range(5):
            schedule.run_pending()
            print('Waiting for {} {}'.format(scheduled_time, '.'*(n+1)))
            sleep(1)