# Builds the dict of possible characters, the more frequent the more likely
# For example {a : [b, b, b, c, d, d, e]}

def build_next_character_dict(filename : str) -> dict:
    next_character_dict = {}
    
    with open(filename, "r", encoding="utf-8") as file:
        for word in file:
            # print(word)
            for i, c in enumerate(word[:-2]):
                if i == len(word) - 1:
                    break
                
                if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    c = c.lower()
                    
                if c not in next_character_dict:
                    next_character_dict[c] = []
                
                next_c = word[i+1]
                
                if next_c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    next_c = next_c.lower()
                    
                next_character_dict[c].append(next_c)
    
    return next_character_dict

if __name__ == "__main__":
    print(build_next_character_dict("data.txt"))