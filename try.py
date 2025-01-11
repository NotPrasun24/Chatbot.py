import json
import random
import logging


logging.basicConfig(
    filename='try.log', 
    filemode='a', 
    level=logging.DEBUG, 
    format='%(asctime)s - [Time] - %(message)s',
    datefmt="%H/%M/%S",
)

def storage_file():

    with open ('storage.json','r') as storage:
        data = json.load(storage)
        return data
def name():
        print('*'*10 + " Welcome to ChatBot " + '*'*10 + "\n" )
        while True:
            user_name = input("Hi there! What is your name: ")
            if user_name == "" or user_name == " ":
                print("You did not enter your name")
                continue
            else:
                return user_name
def main():
    storage_data = storage_file()
    user = name()  # Get the user's name
    my_agent = random.choice(storage_data["agent"])
    logging.info(f"User {user} started a conversation with {my_agent}.")
    print(f"Hi there {user} , My name is {my_agent}. How may i assist you today? ")
    while True:
        user_input = input(f"{user}: ").lower()
        logging.info(f"U{user}: {user_input}")

        if user_input == "bye" or user_input == "exit":
            logging.info(f"{user} ended the conversation.")
            print(f"Goodbye {user}! It was nice chatting with you.")
            break

        keywords = storage_data["responses"]
        found_key = False
        for keyword, response in keywords.items():  # Use .items() to access key-value pairs
            if keyword in user_input.lower():
                print(f"{my_agent}: {response}")
                logging.info(f"{my_agent} replied: {response}")

                found_key = True
                break
        if not found_key: 
            random_answer = random.choice(storage_data["random_responses"])
            print(f"{my_agent}: {random_answer}")    
            logging.info(f"{my_agent} replied: {random_answer}")
                
if __name__ == "__main__":
    main()