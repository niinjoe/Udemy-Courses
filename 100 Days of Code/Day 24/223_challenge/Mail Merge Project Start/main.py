# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as main:
    message = main.read()
    with open("./Input/Names/invited_names.txt", "r") as name:
        individual = name.readlines()
        for person in individual:
            ind = individual[person].strip("\n")
            # print(ind)
            with open(f"./Output/ReadyToSend/{ind}.txt", "w") as writer:
                writer.write(f"Dear {ind},\n\n")
                writer.write(message.strip("Dear [name],\n"))

