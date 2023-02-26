import re

def text_correct(string):  # function which corrects text format
    text = string.lower()  # converts a string into lower case
    first_words = re.split('(\.\s+)', text)  # split text on sentence
    upper_words = [word.capitalize() for word in first_words]  # capitalize first letters of each sentence
    update_text = "".join(upper_words)  # union all parts
    correct_text = update_text.replace(' iz', ' is')  # replace 'iz' by 'is'
    return correct_text


def last_word(string):  # function which returns last word and create new sentence
    last_words = re.findall(r"\s(\w+)\.\s+", text_correct(string))  # find all last words
    all_words = ' '.join(last_words).lower()  # union them
    sentence = f'\tList of last words for new sentence: {all_words}.\n'  # create new sentence
    return sentence


def new_text(string):  # function which unions correct text and sentence that contains last words
    new_text = text_correct(string) + last_word(string)
    return new_text


def calculate_whitespace(string):  # function that calculate number of whitespace
    d = 0  # calculate number of whitespace
    for i in new_text(string):
        if i.isspace():
            d += 1
    return f'Number of whitespaces: {d}'


# Driver code
string = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# print(last_word(string))
# print(text_correct(string))
print(new_text(string))
print(calculate_whitespace(string))
