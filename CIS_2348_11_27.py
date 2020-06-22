# Joshua Chan
# 1588459
dictionary = {}
for i in range(5):
    jersey = int(input("Enter player %s's jersey number:\n" % str(i + 1)))
    rating = int(input("Enter player %s's rating:\n" % str(i + 1)))
# user input for the jersey number and rating
    if jersey not in dictionary:
        dictionary[jersey] = rating
    print()
# If the jersey is not in the dictionary, it will be added and the entry will be printed
print("ROSTER")
for j, k in sorted(dictionary.items()):
    print("Jersey number: %d, Rating: %d" % (j, k))
print()
# The dictionary of jerseys will be printed

while True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    choice = input('\nChoose an option:\n')
# The options given to the user will be printed and they can input an option
    choice = choice.lower()
    if choice == 'o':
        print("\nROSTER")
        for a, b in sorted(dictionary.items()):
            print("Jersey number:%d,Rating:%d" % (a, b))
# The roster will be outputted
    elif choice == 'a':
        jersey = int(input("Enter a new player jersey number:\n"))
        rating = int(input("Enter player's rating:\n"))
        if jersey not in dictionary:
            dictionary[jersey] = rating
        else:
            print("\nThe Player already in the list")
# a player will be added
    elif choice == 'd':
        jersey = int(input("\nEnter a jersey number:\n"))
        if jersey in dictionary:
            del dictionary[jersey]
        else:
            print("\nThe Player is not in the list")
# a player will be removed
    elif choice == 'u':
        jersey = int(input("\nEnter a jersey number:\n"))
        if jersey in dictionary:
            rating = int(input("\nEnter a new rating for the player:\n"))
            dictionary[jersey] = rating
        else:
            print("\nThe Player is not in the list")
# update a player rating
    elif choice == 'r':
        rating = int(input("\nEnter a rating:\n"))
        for k, v in sorted(dictionary.items()):
            if v > rating:
                print("Jersey number: %d, Rating: %d" % (k, v))
    elif choice == 'q':
# output player(s) above a rating
        break
    else:
        print("\nEnter a valid choice")