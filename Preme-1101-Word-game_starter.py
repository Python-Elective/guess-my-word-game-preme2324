# #Problem 1
'''
varieble descriptions:
secret_word is a string, the word the user is guessing
letters_guessed is a list, what letters have been guessed so far
returns is boolean, True if all the letters of secret_word are in letters_guessed and False if not
'''

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#Testcases
print(is_word_guessed('pineapple', []))
print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(is_word_guessed('lettuce', ['k', 'v', 'a', 'e', 'n', 'd', 'b', 'f', 'u', 'c']))

# #Problem 2
# '''
# secret_word: string, the word the user is guessing
# letters_guessed: list, what letters have been guessed so far
# returns: string, comprised of letters and underscores that represents
# what letters in secret_word have been guessed so far.
# '''

def get_guessed_word(secret_word, letters_guessed):
    output_string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output_string += letter + " "
        else:
            output_string += "_ "
    return output_string

# #Testcases:
print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(get_guessed_word('coconut', ['w', 'l', 'i', 'p', 'c', 'u', 'j', 'h', 'v', 'z']))
print(get_guessed_word ('banana', []))
print(get_guessed_word ('broccoli', ['e', 'c', 'g', 'u', 'r', 'x', 's', 'a', 'p', 'j']))


# #Problem 3
# '''
# letters_guessed: list, what letters have been guessed so far
# returns: string, comprised of letters that represents what letters haven't been guessed yet.
# string.ascii_lowercase: a string comprised of all lowercase letters
# '''  

def get_available_letters(letters_guessed):
    import string
    alphabet = list(string.ascii_lowercase)

    for letter in alphabet:
        if letter in letters_guessed:
            alphabet.remove(letter)

    return ' '.join(alphabet)

# #testcases
print(get_available_letters('a'))
print(get_available_letters(['y', 'w', 'b']))


# # # Problem 4
import random
import string

def get_available_letters(letters_guessed):
    alphabet = string.ascii_lowercase
    return ''.join(letter for letter in alphabet if letter not in letters_guessed)

def get_guessed_word(secret_word, letters_guessed):
    return ''.join(letter if letter in letters_guessed else '_' for letter in secret_word)

def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

def choose_word(word_list):
    return random.choice(word_list)
def game_loop(secret_word):
    letters_guessed = []
    mistake_made = 0

    print("Let the game begin!")
    print(f"Here's a word with {len(secret_word)} letters.")

    while True:
        print(f"You have {8 - mistake_made} guesses remaining")
        print(f"Letters available to you: {get_available_letters(letters_guessed)}")
        guess = input("Guess a letter: ").lower()  # Convert the input to lowercase for consistency

        if guess in letters_guessed:
            print(f"You fool! You tried this already: {get_guessed_word(secret_word, letters_guessed)}")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Correct! {get_guessed_word(secret_word, letters_guessed)}")
        else:
            print(f"Incorrect, this letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            mistake_made += 1

        print()

        if is_word_guessed(secret_word, letters_guessed):
            print("You WIN")
            break
        if mistake_made == 8:
            print(f"GAME OVER! The word was: {secret_word}")
            break  # Game stops

#testcases
def main():
    word_list = ["apple", "banana", "orange"] 
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
if __name__ == "__main__":
    main()