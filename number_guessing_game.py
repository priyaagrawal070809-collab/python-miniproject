import time
import random
start_time = time.time()
min_num = 1
max_num = 10
num = random.randint(min_num, max_num)
max_tries = 3
attempt = 0

print(f"Guess a number between {min_num} and {max_num}.")
while attempt < max_tries:
    attempt += 1
    guessing_number = int(input("Enter your number:"))#isko loop me liya

    if guessing_number == num:
        message = f"you have guessed right!\nYou took {attempt} attempts"
        print(message)
        break

    tries_left = max_tries - attempt
    if tries_left > 0:
        message = f"You have {tries_left} tries left."
    else:
        message = f"Sorry, the correct number was: {num}"

    print(message)#isko to likha hi nhi mene
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
