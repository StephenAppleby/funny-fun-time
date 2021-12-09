import requests
import random
from time import sleep

headers = {"Accept": "text/plain"}
exit_messages = ["Nice try!", "Not this time!", "So close!", "No can do!"]

def funny_fun_time(delay):
    try:
        while True:
            r = requests.get("https://icanhazdadjoke.com/", headers=headers)
            print(r.text)
            sleep(delay)
    except KeyboardInterrupt:
        print(random.choice(exit_messages))
        funny_fun_time(delay * 0.8)

funny_fun_time(5.0)





    
