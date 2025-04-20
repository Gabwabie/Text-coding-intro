# student_data = {'id1':
#                 {'name': ['Sara'],
#                  'class': ['V'],
#                  'subject_intergration': ['english, math, science']},
#                  'id2':
#                  {'name': ['David'],
#                   'class': ['V'],
#                   'subject_intergration': ['english, math, science']},
#                   'id3':
#                   {'name': ['Sara'],
#                    'class': ['V'],
#                   'subject_intergration': ['english, math, science']},
#                   'id4':
#                   {'name': ['Surya'],
#                    'class': ['V'],
#                   'subject_intergration': ['english, math, science'],}}
# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
# print(result)

#Initialize dictionary
# test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}

#printing original dictionary
# print("The original dictionary: " + str(test_dict))

#Initialize value
# K = 2

#Using loop
#Selective key values in dictionary
# res = 0
# for key in test_dict:
#     if test_dict[key] == K:
#         res = res + 1
#printing result
# print("Frequency of K is: " + str(res))

SPCMcountry_code = {'Inda': '0091',
                    'Australia': '0025',
                    'Nepal': '00977'}
#search dictionary for country code of India
print("Country code for India -")
print(SPCMcountry_code.get('India', 'Not Found'))

#search dictionary for country code fo Japan
print("Country code for Japan -")
print(SPCMcountry_code.get('Japan', 'Not Found'))