import re
import string

text= """homEwork:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

text=text.lower() #converts a string into lower case

last_words= re.findall(r"\s(\w+)\.\s+", text) #find all last words

all_words=' '.join(last_words) #union them

new_sentence=f'\n\tlist of last words for new sentence: {all_words}.' #create new sentence

#new_text=text +new_sentence #add new sentence to the end of the text

position= re.search(r"this paragraph.", text).end() #find position of the end of paragraph
#print(position)

new_text=text[:position] + new_sentence +text[position:] #add new sentence to the end of paragraph
#print(nex_text)

first_words = re.split('(\.\s+)', new_text) #split text on sentence

upper_words=[word.capitalize() for word in first_words] #capitalize first letters of each sentence

update_text ="".join(upper_words) #union all parts

final_text= update_text.replace(' iz ', ' is ') #replace 'iz' by 'is'

# d=0 #calculate number of whitespace
# for i in final_text:
#     if i.isspace():
#          d +=1
d= len(re.findall(r'[\s]', final_text))

print(f'New version:\n{final_text}')
print(f'Number of whitespaces: {d}')
