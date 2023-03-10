import string
import random


def create_list_of_dict(random_dict_number_from=2, random_dict_number_to=10, random_letter_from=1, random_letter_to=26,
                        random_int_from=1, random_int_to=100):
    dictList = []  # create list of dicts
    for _ in range(random.randint(random_dict_number_from, random_dict_number_to)):  # random number of dictionaries
        k = random.sample(string.ascii_lowercase,
                          random.randint(random_letter_from, random_letter_to))  # random letters (keys)
        oneDict = {n: random.randint(random_int_from, random_int_to) for n in k}  # assemble dict
        dictList.append(oneDict)  # add it to the list  # add it to the list
    return dictList

def create_lists_with_keys(dictList=create_list_of_dict()):
    distinct_keys = []  # create an empty list for distinct letters
    duplicated_keys = []  # create an empty list for letters which have duplicates

    for all_dict in dictList:  # go through each dictionary and each key
        for key in all_dict:
            if key not in distinct_keys:  # if we have the specified key in 'distinct_keys' list-populate this list with each letter
                distinct_keys.append(key)  # populate this list with each letter only once
            elif key not in duplicated_keys:  # if we have duplicated key - populate "duplicated_keys"
                duplicated_keys.append(key)
            distinct_keys.sort()  # sort "distinct_keys" list in alphabetical order
            duplicated_keys.sort()  # sort "duplicated_keys" list in alphabetical order
    return distinct_keys,duplicated_keys

#print(create_lists_with_keys())


# create the function with 3 parameters for distinct_keys, duplicated_keys, list_of_dict
def create_one_common_dict(random_dict_number_from=2, random_dict_number_to=10,
                           random_letter_from=1, random_letter_to=26,
                           random_int_from=1, random_int_to=100):
    dictList=create_list_of_dict(random_dict_number_from, random_dict_number_to, random_letter_from,
                                 random_letter_to, random_int_from, random_int_to)
    distinct_keys, duplicated_keys = create_lists_with_keys(dictList)
    common_dict = {}  # create an empty common dictionary
    for key in distinct_keys:  # check if the letter is exists in 'duplicated_keys' list
        if key in duplicated_keys:
            max_value = 0  # define max value for each key
            dict_number = 0  # define the number of the dictionary in the list
            for i, rand_dict in enumerate(dictList):  # iterate over each dictionary and check if the specified key is in
                if key in rand_dict and rand_dict[key] > max_value:
                    max_value = rand_dict[key]  # update max value
                    dict_number = i + 1  # update the number of the dictionary
            key_final = key + '_' + str(dict_number)  # create the key and insert its max value into the common_dict
            common_dict.setdefault(key_final, max_value)
        if key not in duplicated_keys:  # check if the letter is NOT exists in 'duplicated_keys' list
            for rand_dict in dictList:  # iterate over each dictionary
                if key in rand_dict:  # check if the specified key is in the specified dictionary
                    common_dict.setdefault(key, rand_dict[key])  # insert key and its value in the common_dict
    return  f'List of dictionaries: {dictList} \n' \
            f'Distinct keys: {distinct_keys} \nDuplicated keys:{ duplicated_keys} \n' \
            f'Common dictionary: {common_dict}'

#print(create_one_common_dict(1,6,1,4,1,26))
print(create_one_common_dict())
