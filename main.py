from game import Game
def main():
    print("====================")
    print("Welcome to Scrambled")
    print("====================")
    username = input("Enter a username: ")
    game1 = Game()
    game1.select_category()
    game1.play(username)
    while True:
        usi = input("1) Try again \n2) Change category \n3) Display leaderboard \n4) Change user \n5) Try hard mode \n6) Exit \n ")
        if usi == "1":
            game1.play(username)
        elif usi == "2":
            game1.select_category()
            game1.play(username)
        elif usi == "3":
            game1.display_leaderboard()
        elif usi == "4":
            username = input("Enter a username: ")
            game1.select_category()
            game1.play(username)
        elif usi == "5":
            game1.hard_mode()
        else:
            print("Thank you for playing. Come back soon.")
            break
main()
