import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    
    generate_questions()
    
def generate_questions():
    correct_count = 0
    while correct_count < 3:
        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)

        print("What is", number1, "+", number2, "?")
        answer = int(input())
        correct_answer = number1 + number2

        if answer == correct_answer:
            correct_count += 1
            print("Your answer:", answer)
            print("Correct! You've gotten", correct_count, "correct in a row.\n")
        else:
            correct_count = 0
            print("Your answer:", answer)
            print("Incorrect! The expected answer is", correct_answer,"\n")
        
        if correct_count == 3:
            print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()