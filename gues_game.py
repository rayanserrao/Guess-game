import random


def guesnum(a,b,num):
    count=1
    guess=int(input(f"Guess number between {a} and {b} \n"))
    while( guess != num):
        if guess<num:
            guess=int(input("Actual number is bigger, Enter a  bigger number \n"))
            count += 1
        else:
            guess=int(input("Acuall number is smaller, Enter a smaller number \n"))
            count += 1
    print(f"You took {count} guesses to guess a number correctly")
    return count

if __name__ == "__main__":

    a=int(input(" Player 1 ,enter the number \n"))
    b=int(input("Palyer 2 , enter the number \n"))
    actualnum1=random.randint(a,b)
    print("Player 1's turn \n")
    p1=guesnum(a,b,actualnum1)
    actualnum2=random.randint(a,b)
    print("Player 2's turn \n")
    p2=guesnum(a,b,actualnum2)

    if p1>p2:
        print("Player 2 won the match")
    elif p2>p1:
        print("Player 1 won the match")
    else:
        print("Its a Tie")







        