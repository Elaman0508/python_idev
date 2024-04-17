# import random

# def guess_number():
#     secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
#     attempts = 0

#     print("Привет! Давай поиграем в угадай число.")
#     print("Я загадал число от 1 до 100. Попробуй угадать!")

#     while True:
#         user_guess = int(input("Твоё предположение: "))
#         attempts += 1
#         if user_guess == secret_number:
#             print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
#             break
#         elif user_guess < secret_number:
#             print("Попробуй ввести большее число.")
#         else:
#             print("Попробуй ввести меньшее число. ")

# # Call the function to start the game
# guess_number()




    


    
# def main(): 
#     print('Hello')
#     print('World')
#     print('Salam')

# main()
# print('pause')
# main()


# def pools(x,y):
#     print('Квадарт числа', x, "=", x*y)

# pools(5,5)


# def look():
#     if 5>4:
#         print('hello')
#     else:
#         print('HELLO')
# look()











# import random

# def main():
#     слова = ["яблоко", "банан", "апельсин", "вишня", "груша", "слива", "манго"]
#     text = random.choice(слова)
#     попытки = 0
#     pall = False

#     print("Добро пожаловать в игру 'Угадай слово'!")

#     while not pall:
#         попытка = input("Попробуй угадать слово: ")
#         попытки += 1

#         if попытка == text:
#             pall = True
#             print(f"Поздравляю! Ты угадал слово '{text}' за {попытки} попыток.")
#         else:
#             print("Попробуй еще раз. Неправильное слово.")

# if __name__ == "__main__":
#    main()




# import random

# def choose_word():
#     words = ["apple", "banana", "orange", "cherry", "pear", "plum", "mango"]
#     return random.choice(words)

# def play_guess_the_word():
#     chosen_word = choose_word()
#     word_length = len(chosen_word)
#     attempts = 0
#     guessed_letters = []
#     mask = ["_"] * word_length
#     guessed = False

#     print("Welcome to the 'Guess the Word' game!")

#     while not guessed:
#         current_word = " ".join(mask)
#         print(f"Current word: {current_word}")
        
#         guess = enter_letter()
#         attempts += 1

#         if guess in guessed_letters:
#             print("You've already tried this letter. Try another one.")
#             continue

#         guessed_letters.append(guess)

#         if guess in chosen_word:
#             update_mask(guess, chosen_word, mask)
#         else:
#             print("There is no such letter in the word. Try again.")

#         guessed = "_" not in mask

#     print(f"Congratulations! You guessed the word '{chosen_word}' in {attempts} attempts.")

# def enter_letter():
#     while True:
#         guess = input("Enter a letter: ").lower()
#         if guess.isalpha() and len(guess) == 1:
#             return guess
#         else:
#             print("Please enter a single letter.")

# def update_mask(letter, word, mask):
#     for i, char in enumerate(word):
#         if char == letter:
#             mask[i] = letter

# if __name__ == "__main__":
#     play_guess_the_word()  






# import random

# def orel_reshka():
   
#     result = random.randint(0, 1)

#     if result == 0:
#         print("Выпал орёл!")
#     else:
#         print("Выпала решка!")


# orel_reshka()




# import random
# import time

# def orel_reshka():
#     print("Подбрасываем монетку...")
#     time.sleep(3)  
  
#     result = random.randint(1, 2)
    
#     time.sleep(1)  
    
    
#     if result == 1:
#         print("Выпал орёл!")
#     else:
#         print("Выпала решка!")

# orel_reshka()




import random
import time

def rps_game():
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = random.choice(choices)
    
    print("Камень, ножницы, бумага...")
    time.sleep(1)
    print("Подождите, я сделаю свой выбор...")
    time.sleep(2)
    
    player_choice = input("Ваш выбор (камень, ножницы, бумага): ").lower()
    
    print(f"Компьютер выбрал: {computer_choice}")
    print(f"Вы выбрали: {player_choice}")
    
    if player_choice not in choices:
        print("Неверный выбор. Попробуйте еще раз.")
        return
    
    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
         (player_choice == 'ножницы' and computer_choice == 'бумага') or \
         (player_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
    else:
        print("Компьютер победил!")


rps_game()




