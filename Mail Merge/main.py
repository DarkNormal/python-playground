#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

def save_email(name, email):
    file_name = "letter_for_" + name + ".txt"
    with open(file=file_name, mode="w") as letter:
        letter.write(email)


if __name__ == "__main__":
    with open("Input/Names/invited_names.txt", mode="r") as names_file:
        names = names_file.readlines()
    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        template = starting_letter.read()
        for name in names:
            formatted_name = name.strip()
            formatted_email = template.replace("[name]", formatted_name)
            save_email(formatted_name, formatted_email)



    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp