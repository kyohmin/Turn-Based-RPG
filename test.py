def top_line(TITLE):
    print("==== " + TITLE +" " +"=" * (43 - len(TITLE)))

def turn_line(NUMBER, PLAYING):
    print("==== "+"TURN "+ str(NUMBER) +" ["+ PLAYING +"] "+"=" * (35 - (len(str(NUMBER))+ len(PLAYING))))

turn = 1
top_line("MAIN MENU")
turn_line(turn, "ALLY'S TURN")
turn = 10
turn_line(turn, "PLAYER'S TURN")