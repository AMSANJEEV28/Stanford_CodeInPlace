def main():
    initialNumber=float('-inf')
    count=0
    print("Enter a sequence of non-decreasing numbers")
    while True:
        number=float(input("Enter num: "))
    
        if number<initialNumber:
            print("Thanks for playing!")
            print("Sequence length: ",count )
            break
        
        initialNumber = number
        count +=1
        

    

    
    

if __name__ == "__main__":
    main()