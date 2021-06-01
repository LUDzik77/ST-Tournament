# based on the big 5 from experimentall psychology +evel/good

def get_race_character(race):
    if race == "human":
        race_character = CHARACTER_HUMAN
    elif race == "elf":
        race_character = CHARACTER_ELF
    elif race == "dwarf":
        race_character = CHARACTER_DWARF
    elif race == "hobbit":
        race_character = CHARACTER_HOBBIT    
    return(race_character)


def trim_traits(full_list):
    opposite_traits = (
        ("Nervous","Resilient"),
        ("Outgoing","Solitary"),
        ("Friendly","Stubborn"),
        ("Organized","Lazy"),
        ("Good","Evil"))                      
    for pair in opposite_traits:
        if pair[0] in full_list and pair[1] in full_list:
            full_list.remove(pair[0])
            full_list.remove(pair[1])
    return(full_list)
        
    

CHARACTER_HUMAN = {
    "Nervous":   5,
    "Resilient": 5,
    "Curious":   5,
    "Simpleton": 5,
    "Outgoing":  5,
    "Solitary":  5,
    "Friendly":  5,
    "Stubborn":  5,
    "Organized": 5,
    "Lazy":      5,
    "Good":      5,
    "Evil":      5,
    "Human hater":  1,
    "Elf hater":    3,
    "Dwarf hater":  3,
    "Hobbit hater": 2,
    }

CHARACTER_ELF = {
    "Nervous":   1,
    "Resilient": 6,
    "Curious":   6,
    "Simpleton": 1,
    "Outgoing":  3,
    "Solitary":  2,
    "Friendly":  5,
    "Stubborn":  1,
    "Organized": 5,
    "Lazy":      4,
    "Good":      5,
    "Evil":      1,    
    "Human hater":  3,
    "Elf hater":    0,
    "Dwarf hater":  6,
    "Hobbit hater": 1,    
    }

CHARACTER_DWARF = {
    "Nervous":   6,
    "Resilient": 1,
    "Curious":   1,
    "Simpleton": 5,
    "Outgoing":  5,
    "Solitary":  1,
    "Friendly":  1,
    "Stubborn":  5,
    "Organized": 2,
    "Lazy":      5,
    "Good":      1,
    "Evil":      5,
    "Human hater":  1,
    "Elf hater":    6,
    "Dwarf hater":  0,
    "Hobbit hater": 2,    
    }

CHARACTER_HOBBIT = {
    "Nervous":   4,
    "Resilient": 4,
    "Curious":   6,
    "Simpleton": 3,
    "Outgoing":  2,
    "Solitary":  6,
    "Friendly":  6,
    "Stubborn":  3,
    "Organized": 4,
    "Lazy":      4,
    "Good":      4,
    "Evil":      4,
    "Human hater":  1,
    "Elf hater":    1,
    "Dwarf hater":  1,
    "Hobbit hater": 0,     
    }

