def multiply_array_pairs():
    Input = [2 , 3, 4, 5, 6]
    result = []

    for i in range(0, len(Input) - 1):
        result.append(Input[i] * Input[i + 1])
    print(result)

def elem_that_appears_oly_once():
    arr = [7, 3, 5, 4, 5, 3, 4]

    res = arr[0]

    for i in range(1, len(arr)):
        res = res ^ arr[i]

    print(res)

def two_int_equal_to_sum():
    arr = [1, 2, 3, 4, 5]
    k = 5

    use_a_set = set()

    for i in range(0, len(arr) - 1):
        temp =  abs(arr[i] - k)
        if  temp in use_a_set:
            print("the sum is from", arr[i], temp)
        else:
            use_a_set.add(arr[i])

def reverse_words_in_sentence():
    sentence = "hello world"

    split_sentence = sentence.split(" ")
    result = split_sentence[::-1]
    print(" ".join(result))

#First Non-Repeating Integer in an Array
def non_repeating_ints():
    arr = [1, 1, 2, 4, 5, 5, 7, 7]

    temp_dict = {}

    for item in arr:
        if item not in temp_dict:
            temp_dict[item] = 0
        temp_dict[item] += 1
    
    for val in temp_dict:
        if temp_dict[val] == 1:
            print(val)


def repeating_letters_in_string():
    string = "helloo"
    temp_dict = {}

    for item in string:
        if item not in temp_dict:
            temp_dict[item] = 0
        temp_dict[item] += 1

    for obj in temp_dict:
        if temp_dict[obj] > 1:
            print(obj)


def longestCommonPrefix(strs):
    len_ = 0
    a = zip(*strs)
    print(a)
    for i in a:
        if len(set(i)) == 1:
            len_ += 1
        else: 
            break
    print(strs[0][:len_] if len_ > 0 else "")


def longestCommonSubsequence():
    arr = ["ABAB", "BABA"]

    all_arr = zip(*arr)
    len_ = 0
    for i in all_arr:
        if (len(set(i)) == 1):
            len_ += 1
        else:
            break
    print (arr[0: len_])
            

#longestCommonSubsequence()
#longestCommonPrefix(["flow", "flower", "fl"])
#repeating_letters_in_string()
#non_repeating_ints()
#reverse_words_in_sentence()
#elem_that_appears_oly_once()
#multiply_array_pairs()
#two_int_equal_to_sum()




def sums_str_num(my_str):
    result = 0
    for c in my_str:
        if c.isdigit():
            result += int(c)
    print(result)

sums_str_num("12AB34")