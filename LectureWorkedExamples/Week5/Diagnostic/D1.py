def main():
    humanHeight=float(input("Enter your height in meters _____")) 
    if(humanHeight>1.6 and humanHeight<1.9):
        print("Correct height to be an astronaut")
    if(humanHeight<=1.6):
        print("Below minimum astronaut height")
    if(humanHeight>=1.9):
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()