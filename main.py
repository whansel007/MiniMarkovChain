import random
from dict_builder import build_next_character_dict


character_dict = build_next_character_dict("data.txt")

def markov_chain(next_dict : dict, max:int, min : int = 3, prev : int = 3) -> str:
    start_options_list = list(next_dict.keys())    
    random_start = start_options_list[random.randint(0, len(start_options_list) - 1)]
    
    key = random_start
    output = ""
    
    possibilities = []
    
    for _ in range(random.randint(min, max)):
        
        next_possibilities = next_dict[key]
        
        possibilities.append(next_possibilities)
        
        if len(possibilities) > prev:
            possibilities.pop(0)
        
        total_possibilities = []
        for p_list in possibilities:
            total_possibilities += p_list
        random_next = total_possibilities[random.randint(0, len(total_possibilities) - 1)]
        
        output += key
        key = random_next
    return output


print("\33[33;1mList of generations: \33[m")
for i in range(10):
    print(f"{i+1}. {markov_chain(character_dict, 17)}")