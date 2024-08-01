import random
import hang_art
import hang_name
lives=6
#word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(hang_name.word_list)
print(chosen_word)
display=[]
for i in range (len(chosen_word)):
    display +="_"
end_of_the_game=False
while  end_of_the_game==False:   
    guess=input("Guess the letter of The chosen word").lower()
    for position in range (len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
           end_of_game = True
           print("You lose.")
    print(hang_art.stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_the_game=True
        print("You win")