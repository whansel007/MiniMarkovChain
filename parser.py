all_words = []

with open("list.txt", "r", encoding="utf-8") as file: 
    read_next = False
    
    for line in file:
        
        if read_next:
            read_next = False
            
            ignore = False
            word_string = ""
            for c in line[:-2]:
                if c in "<>":
                    ignore = not ignore
                    continue
                
                if not ignore:
                    if c in ",/":
                        word_string += " "
                    else:
                        # For this case we only want latin alphabets
                        if c in "ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ":
                            word_string += c.lower()
                        else:
                            word_string += ""
            print(word_string)
            
            words_list = word_string.split(" ")
            
            all_words += words_list
            all_words = list(filter(lambda x : x != '', all_words))
                            
        elif "<tr id=" in line[0:7]: 
            read_next = True
        elif "<STOP HERE PLEASE>" in line:
            break

print(all_words)

max_len = 1
min_len = 999
total_len = 0
total_words = 0
with open("data.txt", "w", encoding="utf-8") as data:
    for word in all_words:
        length = len(word)
        total_len += length 
        total_words+= 1
        
        max_len = max(length, max_len)
        min_len = min(length, min_len)
            
        data.write(word + "\n")  
          
average_len = total_len / total_words

print("max length : ", max_len)
print("min length : ", min_len)
print("average length : ", average_len)
        
        