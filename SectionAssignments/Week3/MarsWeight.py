"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    weightOnEarth=input("Enter a weight on Earth: ")
    weightOnEarth=float(weightOnEarth)
    weightOnMars=(weightOnEarth*37.8)/100
    print("The equivalent weight on Mars: " , weightOnMars)
if __name__ == "__main__":
    main()