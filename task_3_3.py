def count_letters(text_list):
    text_dict = {}
    text_list = text_list.lower()
    for char in text_list:
        if char.isalpha():
            if char in text_dict:
                text_dict[char] += 1
            else:
                text_dict[char] = 1
    return text_dict

def calculate_frequency(text_dict):
    total_letters = sum(text_dict.values())
    for char in text_dict:
            frequency = text_dict[char] / total_letters
            text_dict[char] = round(frequency, 2)
        
    return text_dict

text = "Без труда не выловишь и рыбку из пруда."
letter_count = count_letters(text)
letter_frequency = calculate_frequency(letter_count)

for char in letter_frequency:
    print(char, letter_frequency[char])
