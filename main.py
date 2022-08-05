# printing the numbers 1-200
list1 = [i for i in range(0,201)]
print(list1)
# Use the above output to print the elements which is divisible by 2
list2 = [ i for i in list1 if i%2 == 0 ]
# for i in list1:
#     if i%2 == 0:
#         list2.append(i)
print(list2)
# Use the above out to print the values in key- value pair, the key should be the index and value is the element.
dictionary = dict(zip(list1,list2))
print(dictionary)