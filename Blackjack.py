again = True


def blackjack():
    global again
    again = True
    import random
    import art
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def clear():
        print("\n" * 50)

    def total():
        return sum(player_cards)

    def total_opp():
        return sum(computer_cards)

    def first_display():
        print(f"""
            Your cards: {player_cards}, current score: {total()}
            Computer's first card: {computer_cards[0]}
            """)

    def display():
        print(f"""
                Your cards: {player_cards}, current score: {total()}
                dealer cards: {computer_cards}, current score {total_opp()}
                """)

    def add():
        rand_card = (random.choice(cards))
        player_cards.append(rand_card)

    def add_opp():
        computer_cards.append(random.choice(cards))

    def check():
        global again
        if sum(player_cards) == 21 and sum(computer_cards) == 21:
            print("Both players have 21, Draw!")
            again = False
        elif sum(player_cards) > 21:
            print("You went over. You lose 😭")
            again = False
        elif sum(player_cards) == 21:
            print("You win 😄")
            again = False
        elif sum(computer_cards) > 21:
            print("Opponent went over. You win 😁")
            again = False
        elif sum(computer_cards) == 21:
            print("You lose 😓")
            again = False
        elif deal != "y" and sum(computer_cards) > sum(player_cards):
            print("You lose 😢")
            again = False
        elif deal != "y" and sum(computer_cards) == sum(player_cards) and sum(computer_cards) >= 16:
            print("Both players got the same number, it's a draw")
            again = False

    if play == "y":
        print(art.logo)
    player_cards = []
    for turns in range(0, 2):
        add()

    computer_cards = []
    for turn in range(0, 2):
        computer_cards.append(random.choice(cards))
    first_display()
    if total() == 21:
        print("Black jack 😄😄")
        print("You win 🎉🎉🎉")
        again = False
    while again:
        deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if deal == "y":
            clear()
            print(art.logo)
            check()
            add()
            if sum(player_cards) > 21 and 11 in player_cards:
                for n in player_cards:
                    if n == 11:
                        ace_index = player_cards.index(11)
                        player_cards[ace_index] = 1
            first_display()
            check()
        else:
            clear()
            print(art.logo)
            while total() > total_opp():
                check()
                add_opp()
                if sum(computer_cards) > 21 and 11 in computer_cards:
                    for n in computer_cards:
                        if n == 11:
                            ace_index = computer_cards.index(11)
                            computer_cards[ace_index] = 1
            display()
            check()
    if not again:
        ask = input("Do you want to play another game of Blackjack? Type 'y' or 'n':").lower()
        if ask == "y":
            blackjack()


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
if play == 'y':
    blackjack()
