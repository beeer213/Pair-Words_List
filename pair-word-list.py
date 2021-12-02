# Python3 code pairs in Word List

# Function set data to 2 words
def setListData(list_data):
    target_list = []
    for x in range(len(list_data)):
        if x % 2 == 0:
            target_list.append(list_data[x] + list_data[x + 1])
    return target_list

# Function pari target with wordList
def solve(wordList, target):
    pair_list = []
    for t_list in target:
            for w_list in wordList:
                if t_list in w_list:
                    pair_list.append(w_list)
    return pair_list

# Set word list 2 word when user input information 
word_list = list(input("wordList = "))
# Set target 2 word when user input information
target_list = list(input("target = "))

# Check user input lenght data
word_list_new = []
target_list_new = []
if len(word_list) % 2 != 0 or len(target_list) % 2 != 0:
    print("output = None")
else:
    # Convert a list with strings all to lowercase
    word_list_lowercase = [w_lowercase.lower() for w_lowercase in word_list]
    target_list_lowercase = [t_lowercase.lower() for t_lowercase in target_list]

    # Set new word_List and targer_List
    word_list_new = setListData(word_list_lowercase)
    target_list_new = setListData(target_list)

    # Set distinct target data for function pair list
    targer_distinct = list(set(target_list_new))

    # Finish pair list data
    pair_list = solve(word_list_new , targer_distinct)

    # Last check pair list more than 1 words
    if(len(pair_list) > 1):
        print("output = " + str(pair_list))
    else:
        print("output = None")