#question number 1 reverse a list
def reverse_a_list(enter_list):
    return enter_list[::-1]
#print((reverse_a_list([1,2,3,4,5,6])))

#question number 2 Find the Maximum and Minimum Elements:
def finding_max_min(enter_num):
    finding=sorted(enter_num)
    maximum=finding[-1]
    minimum=finding[0]
    return (f" /The maximum number in list is {[maximum]}....."
            f"/The minimum number in list is {[minimum]}")

#print(finding_max_min([1,4,2,3,5,7,6]))


# question  umber 3 check if it is palindrome?
def check_if_palindrome(enter_value):
    s=enter_value.replace(" ","").upper()
    if s==s[::-1]:
        print(f" You entered sentence is a palindrome")
    else:
        print(f" You entered sentence is not an palindrome")
#print(check_if_palindrome("madan"))


# question  number 4  merge two sorted lists
def merge_two_sorted_lists(enter_list1,enter_list2):
    merge_list=[]
    filtered_list1=sorted(enter_list1)
    filtered_list2=sorted(enter_list2)
    merge_list.extend(filtered_list1)
    merge_list.extend(filtered_list2)
    print(merge_list)
#print(merge_two_sorted_lists([1,1,2,3,4,4,5,7,6],[21,23,22,26,24,12]))


#question number 5 remove duplicates from an list
def removing_duplicates(enter_a_data):
    return set(enter_a_data)
#print(removing_duplicates([1,1,1,22,22,3,4,5,5,]))


# question number 6
def count_word_frequencies(enter_a_word):
    final_dict={}
    split_the_word=enter_a_word.split()
    for item in split_the_word:
        if item in split_the_word:
            final_dict[item]=split_the_word.count(item)
    return final_dict
#print(count_word_frequencies(" my name is manjunath manjunath"))


#question number 7 invert a dictionary

def invert_a_dictionary(enter_a_dict_value):
    inverted_dict={}
    for key,value in enter_a_dict_value.items():
        inverted_dict[value]=key
    return inverted_dict
#print(invert_a_dictionary({'a': 1, 'b': 2, 'c': 3}))


# question number 8 Check if Two Dictionaries Contain the Same Keys and Values:


def  if_two_dictionaries_contains_same_keys_values(dict1,dict2):
    for key,value in dict1.items():
        for k,y in dict2.items():
            if key  in k :
                print(k,y)
#print(if_two_dictionaries_contains_same_keys_values({'a': 1, 'b': 2, 'c': 3},{"a":1,"c":3,"d":4}))


# question number 8 find the most frequent element in dictionary
#out put freq_dict = {'apple': 3, 'banana': 5, 'cherry': 2, 'date': 5}

def finding_most_frequent_element_in_dictionary(enter_the_value):
    max=1

    for x,y in enter_the_value.items():
        if max>y+1:
            print(x)
#print(finding_most_frequent_element_in_dictionary( {'apple': 3, 'banana': 5, 'cherry': 2, 'date': 5}

the_original_dictionary_is={'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# The_converted_list_is =[['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]
def _convert_dict_to_list(user_input):
   coverted_list=[[key]+value for key,value in user_input.items()]
   return coverted_list
#print(_convert_dict_to_list({'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}))


input_tuple=[("akash", 10), ("gaurav", 12), ("anand", 14),("suraj", 20), ("akhil", 25), ("ashish", 30)]
# Output : {'akash': [10], 'gaurav': [12], 'anand': [14],'ashish': [30], 'akhil': [25], 'suraj': [20]}
def convert_tuples_to_dict(enter_your_values):
    d={}
    for item in enter_your_values:
        d[item[0]]=item[1]


    return d

#print(convert_tuples_to_dict([("akash", 10), ("gaurav", 12), ("anand", 14),("suraj", 20), ("akhil", 25), ("ashish", 30)]))

the_original_dict= {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

def remove_unique_value_in_dictionary(func):
    for x,y in func.items():
        return y


#print(remove_unique_value_in_dictionary({'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}))


#write an function to create sum without using buuilt in functions
def create_sum_without_using_builtin_func(num):
    a=0
    for item in num:

            a+=item
    return a
#print(create_sum_without_using_builtin_func([1,2,3,4,5]))


# write an function to create multiplication without using built in function

def create_multipplication_without_using_builtin_function(num):
    mul=1
    for x in num:
        mul*=x
    return mul
#print(create_multipplication_without_using_builtin_function([1,2,3,4,5,]))


# inter change first and last element of a list
def interchange_first_and_last_element_of_a_list(list):
    list[0],list[-1]=list[-1],list[0]
    return list


#print(interchange_first_and_last_element_of_a_list([1,2,3,4,5]))


# create new list containing only the even numbers from the original list:
def creating_a_new_list_only_even_number(num):
    only_even=[]
    for x in num:
        if x%2==0:
            only_even.append(x)
    return only_even

#print(creating_a_new_list_only_even_number([1,2,3,4,5,6,7,8])    )


# create a new list with squares of each element in the original list

def creating_squares_of_each_list(user_inp):
    creating_squares=[item**2 for item in user_inp]
    return creating_squares

print(creating_squares_of_each_list([1,2,3,4,5,6,7,8,9,10]))


fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']
d={}

for i in fruits:
    d[i]=fruits.count(i)
print(d)







