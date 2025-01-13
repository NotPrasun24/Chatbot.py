def get_language_data(choice, data):


    language_map = {
        1: "english_language",
        2: "nepali_language",
        3: "spanish_language"
    }

    # Get the language key based on choice
    language_key = language_map.get(choice)
    print(language_key)

    # Return the data for the selected language if it exists
    if language_key and language_key in data:
        return {
            "agents": data[language_key]["agents"],
            "random_response": data[language_key]["random_response"],
            "keyword_response": data[language_key]["keyword_response"]
        }
    else:
        return {"error": "Invalid choice or data not found for the selected language."}

# Example usage
import json

# Load your JSON file
with open('res.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

choice = 3  # Example: 1 for English
result = get_language_data(choice, data)
print(result)
