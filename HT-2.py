import random
import string

#create a list of random number of dicts (from 2 to 10)
dictList = []                                            #create list of dicts
for _ in range(random.randint(2,10)):                    # random number of dictionaries
    size= random.randint(1,3)                            # random dictionary size
    keys = random.sample(string.ascii_lowercase,size)    # random letters
    values= (random.randint(1,100) for _ in range(size)) # random numbers
    oneDict = dict(zip(keys,values))                     # assemble dict.
    dictList.append(oneDict)                             # add it to the list

print(dictList)

# get previously generated list of dicts and create one common dict:

all_keys = []                                            # create an empty list for all keys
for d in dictList:                                       # go through each key from dictList
    all_keys.extend(d)                                   # add it to the list
#print(all_keys)

DupList =[]                                             # create an empty list for duplicate keys
AllList=[]                                              # create an empty list for all keys
for i in all_keys:                                      # go through each key from all_keys and if >2  and not in dup_list put in
    if all_keys.count(i) >= 2:
        if i not in DupList:
            DupList.append(i)
        elif i not in AllList:
            AllList.append(i)
    elif i not in AllList:
         AllList.append(i)
print(DupList)
print(AllList)

common_dict = {}                                     # create an empty common dictionary

for key in AllList:
    if key in DupList:                                   #if this letter is in "duplicated_keys" list
        max_value = 0                                    # max value for each key
        dict_number = 0                                  # the number of the dictionary in the list
        for i, rand_dict in enumerate(dictList):          # check if the key is in the first generate dictionary
            if key in rand_dict and rand_dict[key] > max_value:   # AND the key's value is bigger than max value
                max_value = rand_dict[key]                 #update max value and add 1 to number
                dict_number = i + 1
        key_final = key + '_' + str(dict_number)             # create and insert new key
        common_dict.setdefault(key_final, max_value)
    if key not in DupList:
        for rand_dict in dictList:                           # iterate over each dictionary
            if key in rand_dict:
                common_dict.setdefault(key, rand_dict[key])  # insert key and its value in the one_common_dict

print(common_dict)
