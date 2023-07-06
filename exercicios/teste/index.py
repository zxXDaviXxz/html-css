import random
def play ():

    user = input("O que você escolhe? 'r' for pedra, 'p' for papel, 's' for tesoura\n") 
    computer = random.choice(['ro', 'pa', 'te'])

    if user == computer:
        return 'It\'s a tie' 
    
    # r > t, t > p, p > r
    if is_win(user, computer):
        return 'Você é foda companheiro'
    
    if is_win(computer, user):
        return 'Você é horrivel'
    
    def is_win(player, oponente):
        # return true if player wins
        # r > s, s > p, p > r
        if (player == 'r' and oponente == 's') or (player == 'sts' and oponente == 'p') or (player == 'p' and oponente == 'r'):
            return True