import json
import random
def storage_file():
    with open ('storage.json','r') as storage:
        data = json.load(storage)
        return data



def main():
    storage_data = storage_file()
    print('*'*10 + " Welcome to ChatBot " + '*'*10 + "\n" )
    user = input("Hi there! What is your name: ")
    my_agent = random.choice(storage_data["agent"])
    while True:
        user_input = input(f"{user}: ").lower()
        if user_input == "quit" or user_input == "exit":
            print(f"Goodbye {user}! It was nice chatting with you.")
            break
        elif user_input in storage_data["responses"]:
            response = storage_data["responses"][user_input]
            print(f"{my_agent}: {response} \n ")
        else:
            random_answer = random.choice(storage_data["random_responses"])
            print(f"{my_agent}: {random_answer}")
main()

def find_keyword(storage_data, user_input):
    keywords = storage_data["responses"].keys()
     = None
    for word in user_input.split():
        if word.lower() in keywords:
            found_keyword = word.lower()
            break
    return found_keyword
        
    



# keywords = storage_data["responses"].keys()
# found_keyword = None
# for word in user_input.split():
#     if word.lower() in keywords:
#         found_keyword = word.lower()
#         break
    
# # Provide the response
# if found_keyword:
#     print(responses[found_keyword])