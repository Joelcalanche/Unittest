import random

# answer = random.randint(1, 10)

# while True:

#     try:

#         guess = int(input('guess a number 1~10: '))
        
#         if 0 < guess < 11:
#             if guess == answer:
#                 print("you are a genius!")
#                 break
#         else:
#             print("hey bozo, i said 1~10")
#     except ValueError:
#         print("please enter a number")
#         continue


def run_guess_game(guess, answer):
    
    if 0 < guess < 11:
        if guess == answer:
            print("you are a genius!")
            return True #break ---->retunr
    else:
        print("hey bozo, i said 1~10")
        return False

if __name__ =='__main__':
    answer = random.randint(1, 10)
    while True:

        try:

            guess = int(input('guess a number 1~10: '))
            run_guess_game(guess, answer)
            if (run_guess_game(guess, answer)):
                break

        except ValueError:
            print("please enter a number")
            continue

