
##ipa_transcriber.py 
import json 

#load IPA dict once 
with open("utils/data_dict.json", "r", encoding="utf-8") as f: 
    DATA_DICT = json.load(f)

def get_ipa(word):
    
    ##Convert a word to its IPA transcription. 

    return DATA_DICT.get(word.lower(), "IPA not found")

def main(): 
    print("Welcome to the IPA Converter!")
    
    while True: 
        user_input = input ("Enter a word (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break 

        ipa = get_ipa(user_input)
        print(f"IPA transcription: {ipa}\n")


if __name__ == "__main__": 
    main()