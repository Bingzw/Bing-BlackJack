
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        ans = ""
        for i in range(len(self.hand)):
            ans += str(self.hand[i])+ " "
        return "Hand contains " + ans 	# return a string representation of a hand

    def add_card(self, card):	
        self.hand.append(card)         # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        rank = []
        value = 0
        for i in self.hand:
            rank.append(i.get_rank())
            value += VALUES[i.get_rank()]
        if 'A' not in rank:
            pass
        else:
            if value + 10 <= 21:
               value += 10
            else:
                pass
        return value
            
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand)):
            pos_i = [0, 0]
            pos_i[0] = pos[0] + i*CARD_SIZE[0]
            pos_i[1] = pos[1]
            self.hand[i].draw(canvas, pos_i)
        
    

        
# define deck class 
class Deck:
    def __init__(self):
        self.Deck = []	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.Deck.append(Card(i,j))
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()        
        random.shuffle(self.Deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.Deck.pop(-1)
    
    def __str__(self):
        # return a string representing the deck
        ans = ""
        for i in range(len(self.Deck)):
            ans += str(self.Deck[i])+ " "
        return "Hand contains " + ans



#define event handlers for buttons
def deal():
    # your code goes here
    global score, outcome, advice, in_play, New_Deck, Player_Hand, Dealer_Hand
    outcome = " "
    advice = "Hit or Stand?"
    New_Deck = Deck()
    New_Deck.shuffle()
    Player_Hand = Hand()
    Dealer_Hand = Hand()
    Dealer_card1 = New_Deck.deal_card()
    Dealer_card2 = New_Deck.deal_card()
    Player_card1 = New_Deck.deal_card()
    Player_card2 = New_Deck.deal_card()
    Dealer_Hand.add_card(Dealer_card1)
    Dealer_Hand.add_card(Dealer_card2)
    Player_Hand.add_card(Player_card1)
    Player_Hand.add_card(Player_card2)
    print "Dealer has:" + str(Dealer_card1) + " " + str(Dealer_card2)
    print "Player has:" + str(Player_card1) + " " + str(Player_card2)    
    if in_play:
        score -= 1
        outcome = "You lost the last round!"
    in_play = True

def hit():
    # replace with your code below
    global score, in_play, Player_Hand, New_Deck, outcome, advice
    # if the hand is in play, hit the player
    if in_play == True:
        Player_Hand.add_card(New_Deck.deal_card())
        print "Player" + " " + str(Player_Hand)
        print "Player's value: " + str(Player_Hand.get_value())
        if Player_Hand.get_value() <= 21:
            pass
        else:
            in_play = False
            outcome = "You have busted. Dealer wins!"
            advice = "New Deal?"
            score -= 1
            print outcome
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    
    global score, in_play, advice, Player_Hand, New_Deck, Dealer_Hand, outcome
    if in_play:
        while Dealer_Hand.get_value() < 17:
            Dealer_Hand.add_card(New_Deck.deal_card())
        print "Dealer" + " " + str(Dealer_Hand)
        print "Dealer's final value: " + str(Dealer_Hand.get_value())
        print "Player's final value: " + str(Player_Hand.get_value())
        if Dealer_Hand.get_value() > 21:
            outcome = "Dealer has busted. Player wins!"
            score += 1
            print outcome
        else:
            if Dealer_Hand.get_value() >= Player_Hand.get_value():
                outcome = "Dealer wins!"
                score -= 1
                print outcome
            else:
                outcome = "Player wins!"
                score += 1
                print outcome
    in_play = False
    advice = "New Deal?"
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global Player_Hand, Dealer_Hand, outcome, in_play, score
    card = Card("S", "A")
    Player_Hand.draw(canvas, [50, 380])
    Dealer_Hand.draw(canvas, [50, 180])
    canvas.draw_text(str(outcome), (130, 100), 30, 'Red')
    canvas.draw_text("Dealer's Cards", (50, 150), 30, 'Black')
    canvas.draw_text("Player's Cards", (50, 350), 30, 'Black')
    canvas.draw_text("Blackjack", (20, 50), 50, 'Yellow')
    canvas.draw_text(str(advice), (300, 350), 40, 'Blue')
    canvas.draw_text("Score: " + str(score), (400, 70), 30, 'Red')
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 180 + CARD_BACK_CENTER[1]], CARD_SIZE)
        
    # initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


