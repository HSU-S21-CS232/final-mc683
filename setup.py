import os

# Consumer key and secret might be labled as API key and secret.
if(os.path.exists('config.py') == False):
    print("config, not found")
    consumer_key = input("Enter consumer key: ")
    consumer_secret = input("Enter consumer secret: ")
    access_key = input("Enter access key: ")
    access_secret = input("Enter access secret: ")

    print("writing key to file...")
    with open("config.py", "w") as file:
        print("consumer_key = '", consumer_key, "'", file=file, sep='')
        print("consumer_secret = '", consumer_secret, "'", file=file, sep='')
        print("access_key = '", access_key, "'", file=file, sep='')
        print("access_secret = '", access_secret, "'", file=file, sep='')
