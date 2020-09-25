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


reverse_words_in_sentence()

#elem_that_appears_oly_once()
#multiply_array_pairs()
#two_int_equal_to_sum()




