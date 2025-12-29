
##ipa_transcriber.py 
import json 

#load IPA dict once 
with open("utils/a_data_dict.json", "r", encoding="utf-8") as f: 
    A_DATA_DICT = json.load(f) # to load american english IPA

def get_ipa_A(word):

    return A_DATA_DICT.get(word.lower(), "IPA not found")



with open("utils/b_data_dict.json", "r", encoding="utf-8") as f: 
    B_DATA_DICT = json.load(f) # to load British english IPA

def get_ipa_B(word):
    return B_DATA_DICT.get(word.lower(), "IPA not found")
        

    ##Convert a word to its IPA transcription. 


def main(): 
    print("Welcome to the IPA Converter!")
    
    while True: 
        user_choice_language = input ("Choose a language (write down the number): \n 1. AMERICAN ENGLISH\n 2. BRITISH ENGLISH \n or type 'exit' to quit. \n")
        
        if user_choice_language.lower() == "exit": 
            print ("Goodbye!")
            break

        if user_choice_language == "1": 

            while True: 
                user_input = input ("Enter a word (or type 'back' to quit): ")

                if user_input.lower() == "back":
                    print("Goodbye!")
                    break 

                ipa = get_ipa_A(user_input)
                print(f"IPA transcription: {ipa}\n")

        if user_choice_language == "2": 
            
            while True: 
                user_input = input ("Enter a word (or type 'back' to quit): ")
                
                if user_input.lower() == "back": 
                    print ("Goodbye!")
                    break 
                
                ipa = get_ipa_B(user_input)
                print(f"IPA transcription: {ipa}\n")




    


if __name__ == "__main__": 
    main()