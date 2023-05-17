import random

COLOURS=["R","G","B","Y","W","O"]
TRIES=10
CODE_LENGTH=4

def code_generate():
    code=[]
    for i in range(CODE_LENGTH):
        color=random.choice(COLOURS)
        code.append(color)
    return code

code=code_generate()


def guessing_code():
    while True:
        guess=input("guess:").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"you must guess {CODE_LENGTH} colour")
            continue
        for color in guess:
            if color not in COLOURS:
                print(f"Invalid colour {color} try again")
                break
        else:
            break
    return guess

def check_code(guess, real_code):
    color_counts={}
    correct_pos=0
    incorrect_pos=0

    for color in real_code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color]+=1

    for guess_color,real_color in zip(guess,real_code):
        if guess_color==real_color:
            correct_pos+=1
            color_counts[guess_color]-=1

    for guess_color,real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color]>0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    
    return correct_pos, incorrect_pos

def game():
    print(f"welcome to mastermind,you have 10 tries,the valid colors are ",*COLOURS)
    code=code_generate()
    for attempts in range(1, TRIES+1):
        guess=guessing_code()
        correct_pos,incorrect_pos = check_code(guess, code)
        if correct_pos==CODE_LENGTH:
            print(f"you gussed the code in {attempts} tries")
            break
        print(f"correct position:{correct_pos}|incorrect position:{incorrect_pos}")
    else:
            print(f"you ran out of guess, the code was:",*code)


if __name__=="__main__":
    game()

    





    


