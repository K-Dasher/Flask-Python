def main():
    print("Welcome to Band Name Generator")
    _city = input("What is the name of the city you were born in?")
    _pet = input("What is the name of your pet?")
    print(f"The name of your band could be: {(_city.lower()).capitalize()} {(_pet.lower()).capitalize()}")

if __name__ == "__main__":
    main()