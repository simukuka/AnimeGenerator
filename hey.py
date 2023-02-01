import random

action_movies = ["DBZ: Bardock the Father of Goku", "DBZ: The Future of Trunks", "Akira", "Street Fighter: Street Fighter Alpha", "Bleach: The memories of Nobody", "DBZ: Broly The legendary Super Sayain", "DBZ: Broly's Second Coming", "Naruto: Bonds", "Bleach: Hell Verse", "DBZ: Fusion Reborn", "Sakura Wars: The Movie", ]


action_shows = [ "Akashic Records of Bastard Magic Instructor", "Naruto Shippuden", "Bleach", "Dragon Ball Z", "Attack On Titan", "King of Thorn",
]

romance_movies = ["Your Name", "The garden of words", "Howl's Moving Castle", "5 centimeters per second", "Whisper of the Heart", "The Wind Rises", "Into the Forrest of Fireflies' Light"]

comedy_shows = ["Assasin's Classroom", "Shimoneta: A Boring World where Dirty Jokes Don't Exist", "Oreimo", "Good Luck girl!", "Saiki K", "Hinamatsuri", "Combatants Will be Dispatched", "Is This a Zombie?", "Highschool DXD", "Fantasy World knock", "Kaguya Sama: Love is war"]

print("Greetings! I am the random anime generator.\n")
choice = None
while choice != 'q':

  decision = input("Would you like to watch a series or a Movie?\n")

  decision = decision.capitalize()
  print("You chose a {}!".format(decision))

  if decision == "Series":
    print("\nWe have genres from comedy and action")

  if decision == "Movie":
    print("\nWe have genres from romance and action")

  user_genre = input("What Genre do you want to watch?\n")
  user_genre = user_genre.capitalize()
  print("\nYou chose {}!".format(user_genre))

  if user_genre == "Romance" and decision == "Movie":
    watch = random.choice(romance_movies)
    print("     Generated    ")
    print("         {}       ".format(watch))
  elif user_genre == "Action" and decision == "Movie":
    watch = random.choice(action_movies)
    print("     Generated    ")
    print("         {}       ".format(watch))
  elif user_genre == "Comedy" and decision == "Series":
    watch = random.choice(comedy_shows)
    print("     Generated    ")
    print("         {}       ".format(watch))
  elif user_genre == "Action" and decision == "Series":
    watch = random.choice(action_shows)
    print("     Generated    ")
    print("         {}       ".format(watch))

  choice = input("\nWould you like to choose a different {} if not press q? if yes press g: ".format(decision))

  if choice == "q":
    print("\nThank you for using the anime generator!")
    break


  while choice == "g":
    if user_genre == "Romance" and decision == "Movie":
        watch = random.choice(romance_movies)
        print("     Generated    ")
        print("         {}       ".format(watch))
        choice = input("\nWould you like to choose a different {} if not press q?: ".format(decision))
    elif user_genre == "Action" and decision == "Movie":
        watch = random.choice(action_movies)
        print("     Generated    ")
        print("         {}       ".format(watch))
        choice = input("\nWould you like to choose a different {} if not press q?: ".format(decision))
    elif user_genre == "Comedy" and decision == "Series":
        watch = random.choice(comedy_shows)
        print("     Generated    ")
        print("         {}       ".format(watch))
        choice = input("\nWould you like to choose a different {} if not press q?: ".format(decision))
    elif user_genre == "Action" and decision == "Series":
        watch = random.choice(action_shows)
        print("     Generated    ")
        print("         {}       ".format(watch))
        choice = input("\nWould you like to choose a different {} if not press q?: ".format(decision))

    if choice == "q":
        print("\nThank you for using the anime generator!")
        break



