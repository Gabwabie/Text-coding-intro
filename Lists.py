# empty_list = []
# print()

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# triples = [1, 2, 3] * 3
# print(triples)

# aList = [100, 200, 300, 400, 500]
# aList = aList[::-1]
# print(aList, "\n")

# def match_words(words):
#     ctr = 0
#     lst = []
#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             ctr += 1
#             lst.append(word)
#     print("List of words with first and last character same\n", lst)
#     return ctr

# count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
# print("Number of words having first and last character sane:", count)

L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)

count = 0
for i in L:
    count += i
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

L.sort()

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])