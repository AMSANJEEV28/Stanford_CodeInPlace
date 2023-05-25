# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    for i in range(100):
        i += 1
        if(i%2==1):
            number = "odd"
        else:
            number = "even"
        print(i, "is", number )

if __name__ == "__main__":
    main()