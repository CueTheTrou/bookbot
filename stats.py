def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    num_char_dict = {}
    for i in text:
        lowered = i.lower()
        if lowered in num_char_dict:
            num_char_dict[lowered] += 1
        else:
            num_char_dict[lowered] = 1
    return num_char_dict

def sort_dict(num_char_dict):
    return sorted(num_char_dict.items(), key= lambda item: item[1], reverse=True)
