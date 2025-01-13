import json
import random
import logging


logging.basicConfig(
    filename='try.log', 
    filemode='a', 
    level=logging.DEBUG, 
    format='%(asctime)s - [Time] - %(message)s',
    datefmt="%H:%M:%S",
)

def read_file():
    with open ('res.json','r',encoding='utf-8') as storage:
        data = json.load(storage)
        return data
    
def language_data(choice,data):
    language_map = {1: "english_language", 2 : "nepali_language", 3 : "spanish_language"}
    key = language_map.get(choice)
    if key in data:
        agents_name = data[key]["agents"]
        random_response = data[key]["random_response"]
        keyord_response = data[key]["keyword_response"]
        return agents_name,random_response,keyord_response
    else:
        print("error reading data")

def agent_response(keyword_response,random_response,user_input):
    all_keword_responses = []
    for keyword , response in keyword_response.items():
        if keyword in user_input.lower():
            all_keword_responses.append(response)
    if all_keword_responses:
        response = " ".join(all_keword_responses) 
    else:
        response = random.choice(random_response)
    return response
def name():
        print('*'*10 + " Welcome to ChatBot " + '*'*10 + "\n" )
        while True:
            user_name = input("Hi there! What is your name: ")
            if user_name == "" or user_name == " ":
                print("You did not enter your name")
                continue
            print("Which language would you prefer: ")
            print("1. English")
            print("2. Nepali")
            print("3. Spanish")
            choice = int(input("Please choose your language:"))
            return user_name, choice
        
    
def main():
    data = read_file()
    user_name, choice = name()
    agents_name,random_response,keyword_response = language_data(choice,data)
    agents_name = random.choice(agents_name)
    if choice == 1:
        chat_record = f"{agents_name}: Hello {user_name} How may i assist you "
        print(chat_record)
        logging.info(chat_record)
    elif choice == 2:
        chat_record = f"{agents_name}: Namaste {user_name} Kasto cha? "
        print(chat_record)
        logging.info(chat_record)
    elif choice == 3:
        chat_record = f"{agents_name}: Hola {user_name} ¿En qué puedo ayudle? "
        print(chat_record)
        logging.info(chat_record)
    
    while True:
        user_input = input(f"{user_name}: ")
        logging.info(f"{user_name}: {user_input}")

        if user_input.lower() in ["exit","bye","end","adios", "salir", "hasta lugeo", "la ma gako"]:
            logging.info(f"{user_name} ended the conversation.")
            print(f"Goodbye {user_name}! It was nice chatting with you.")
            break
        response = agent_response(keyword_response,random_response,user_input)
        agent_reply = (f"{agents_name}: {response}")
        print(agent_reply)
        logging.info(agent_reply)
    

                
if __name__ == "__main__":
    main()