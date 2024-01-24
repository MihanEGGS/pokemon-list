
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by name")
    print("5. Search by length of name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        ch = int(input("Choose the fighter of thine"))
        print(pokemons[ch])
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
    elif choice == '4':
        le = input("type eine Letter")
        newlist = [x for x in pokemons if le in x]
        print(newlist)
    elif choice == '5':
        neuelist = []
        len = int(input("Choose thine Langt"))
        for i in pokemons:
            if i.__len__() == len:
                neuelist.append(i) 
        print(neuelist)
    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
