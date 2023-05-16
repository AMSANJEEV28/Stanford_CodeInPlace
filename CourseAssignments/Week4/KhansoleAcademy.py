import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    
    number1 = random.randint(10, 99)
    number2 = random.randint(10, 99)
    
    print("What is", number1, "+", number2, "?" )
    answer=input()
    answer = int(answer)
    
    if (number1 + number2 == answer):
        print("Correct!")
    else:
        print("The expected answer is ", number1+number2)
if __name__ == '__main__':
    main()