def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    character = {}
    for i in text:
        lowercase_char = i.lower()
        if lowercase_char in character:
            character[lowercase_char] += 1
        else:
            character[lowercase_char] = 1
    return character

def sort_char_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=lambda x: x ["count"])    
    return chars_list
