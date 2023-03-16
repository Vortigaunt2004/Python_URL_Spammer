import webbrowser
import time
start = input("START? (YES/NO)")

if start == "YES" or start == "yes" :
    url = input("Enter a URL Here:\n")

    while True:
        webbrowser.open_new(url)
        time.sleep(0.1)  # replace with desired number of seconds between each opening

