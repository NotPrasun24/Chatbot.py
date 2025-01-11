import json
import random

def data_of_json():
    with open('storage.json', 'r') as storage:
        data = json.load(storage)
        return data

def main():
    storage_data = data_of_json()
    print("******** Welcome to CHATBOT ************\n")
    user_name = input("Enter your name: ")
    selected_agent = random.choice(storage_data["agent"])

    print(f"Hello {user_name} nice to meet you my name is chatbot ")
    while True:
        ask = input(f"{user_name}: ").lower()
        if ask in storage_data["responses"]:
            response = storage_data["responses"][ask]
            print(f"{selected_agent}: {response}")
        else:
            print("Sorry I didn't understand that")
main()


# # print(storage["name"])
# # ramdom_names = ["SIRI","Aleca"]
# # print(ask)


