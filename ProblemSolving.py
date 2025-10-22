# Q1: Given a list, find the count of each element in the list
# eg: marks=[10,11,12,13,15,10,20,12,15,12]
#o/p:10:2 ,11:1, 12:3,13:1,15:2,20:1
'''
marks=[10,11,12,13,15,10,20,12,15,12]
element_count ={}

for element in marks:
    element_count[element] = element_count.get(element, 0) + 1
print(element_count)



###Way 2:  Given a list, find the count of each element in the list

marks=[10,11,12,13,15,10,20,12,15,12]
element_count ={}

for element in marks:
    if element in element_count:
        element_count[element] = element_count[element] + 1
    else:
        element_count[element] = 1
print(element_count)


# Q1: find duplicates and uniques marks

marks=[10,11,12,13,15,10,20,12,15,12]
element_count ={}

for element in marks:
    if element in element_count:
        element_count[element] = element_count[element] + 1
    else:
        element_count[element] = 1
print("marks count:",element_count)

unique =[]
duplicates =[]
for element in element_count:
    if element_count[element] == 1:
        unique.append(element)
    elif element_count[element] > 1:
        duplicates.append(element)
print("unique :",unique)
print("Dups:",duplicates)




# Q1: find duplicates and uniques marks -with function

def find_unique_duplicate_marks(marks):

    element_count ={}

    for element in marks:
        if element in element_count:
            element_count[element] = element_count[element] + 1
        else:
            element_count[element] = 1
    print("marks count:",element_count)

    unique =[]
    duplicates =[]
    for element in element_count:
        if element_count[element] == 1:
            unique.append(element)
        elif element_count[element] > 1:
            duplicates.append(element)
    #print("unique :",unique)
    #print("Dups:",duplicates)
    return unique,duplicates

##calling function
marks=[10,11,12,13,15,10,20,12,15,12]
res=find_unique_duplicate_marks(marks)

print("Unique-->",res[0])
print("Dups-->",res[1])

'''

