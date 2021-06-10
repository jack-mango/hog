def front_digits(score):
    """Return the two leftmost digits of a player's score"""
    power = 0
    first_digit = 0
    second_digit = 0
    while score - score % (10 ** (power + 1)) > 0: 
        print("score - score % (10 ** (power + 1))= ", score - score % (10 ** (power + 1)))     
        if score - score % (10 ** (power + 1)) == 0:    
            first_digit = score // (10 ** power)        
            second_digit = (score - first_digit * 10 ** (power))// (10 ** (power - 1))
        power += 1
    
    
    return first_digit, second_digit

print(front_digits(101))