# Description: Checks textfile for two strings separated by a new line.
# Sends percentage of how close the two strings are within two decimal points.

import time
import difflib as diff

COMM_TXT = 'input-checker.txt'

def get_data():
    with open(COMM_TXT, 'r') as f:
        data = f.readlines()
        return data

def calculate_percentage(answer, user_answer):
    return diff.SequenceMatcher(None, answer, user_answer).ratio() * 100

def send_data(score):
    with open(COMM_TXT, 'w') as f:
        f.write(f'{score:.2f}%')

def clear_txt():
    with open(COMM_TXT, 'w') as f:
        f.write('')

if __name__ == '__main__':
    while True:
        time.sleep(2)
        data = get_data()
        print(data)
        if len(data) != 2:
            continue
        else:
            percentage = calculate_percentage(data[0].strip(), data[1])
            send_data(percentage)
            time.sleep(5)
            clear_txt()
