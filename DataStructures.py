#collection/sequence data type
'''
# list :

a) ordered collection of items ( the order in which the data is stored
b) Mutable (which can be changed)
c) Insertion order is preserved
d) It can store duplicate values
e) In python we use []
    eg: student_names =['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha']

# tuple:
a) ordered collection of items ( the order in which the data is stored
b) Immutable (Once crested  can't be changed)
c) Insertion order is preserved
d) It can store duplicate values
e) In python we use ()
    eg: student_names =('Narasimha','Srikanth','Nagarjuna','Raju','Narasimha')

# set:
a) Un ordered collection of items
b) Mutable (Once crested  can't be changed)
c) Insertion order is NOT preserved
d) It can NOT store duplicate values
e) In python we use {}
    eg: student_names ={'Narasimha','Srikanth','Nagarjuna','Raju'}


#List methods/functions

NameOfStudents = ['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123]
print(NameOfStudents) # ['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123]
print(type(NameOfStudents)) #list
print(type(NameOfStudents[0])) #string
print(type(NameOfStudents[5])) # int

NameOfStudents.append("Sujatha")# adds element at the end
print(NameOfStudents) # ['Narasimha', 'Srikanth', 'Nagarjuna', 'Raju', 'Narasimha', 123, 'Sujatha']
NameOfStudents[1]= 'Gangadhar'
print(NameOfStudents) #['Narasimha', 'Gangadhar', 'Nagarjuna', 'Raju', 'Narasimha', 123, 'Sujatha']
NameOfStudents.remove(123)
print(NameOfStudents) #['Narasimha', 'Gangadhar', 'Nagarjuna', 'Raju', 'Narasimha', 'Sujatha']
print(NameOfStudents.count('Narasimha'))#2
NameOfStudents.sort()
print(NameOfStudents) #['Gangadhar', 'Nagarjuna', 'Narasimha', 'Narasimha', 'Raju', 'Sujatha']
print(len(NameOfStudents))#6
NameOfStudents.reverse()
print(NameOfStudents)#['Sujatha', 'Raju', 'Narasimha', 'Narasimha', 'Nagarjuna', 'Gangadhar']
NameOfStudents.pop()# last element get removed and return last element
print(NameOfStudents)#['Sujatha', 'Raju', 'Narasimha', 'Narasimha', 'Nagarjuna']
NameOfStudents.pop(0)#0th index element get removed
print(NameOfStudents)#['Raju', 'Narasimha', 'Narasimha', 'Nagarjuna']
NameOfStudents.insert(0,'MNRAO')
print(NameOfStudents) #['MNRAO', 'Raju', 'Narasimha', 'Narasimha', 'Nagarjuna']



# Iterate list using loop

NameOfStudents = ['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123]
#Way 1:
#for i in NameOfStudents:
    #print(i)


# Way 2
NameOfStudents = ['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123]
for i in range(len(NameOfStudents)):
    print("index:",i," ", NameOfStudents[i])


# List slicing
# Get first 3 elements and add them to new_list Way 1:

NameOfStudents = ['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123]
new_list =[]
for idx in range(0,3):
    #print("index:",idx," ", NameOfStudents[idx])
    new_list.append(NameOfStudents[idx])
print(new_list)



# Way 2 : using slicing (similar to range(start,stop, step)
NameOfStudents = ['Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123]
print(NameOfStudents[0:3:1])

# club two lists
list1 =['aram','apple','rox']
list2 =['100','200','500']
print(list1+list2) #['aram', 'apple', 'rox', '100', '200', '500']


# Tuple

NameOfStudents = ('Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123)
print(type(NameOfStudents))
print(NameOfStudents.count('Narasimha')) #2
print(len(NameOfStudents))#6
print(NameOfStudents.index('Narasimha'))#0
print(NameOfStudents.index('Srikanth'))#1
print(NameOfStudents[0])# Narasimha
# NameOfStudents[0] ="Abc"  # This operation won't allowed in tuple


# Set

NameOfStudents = {'Narasimha','Srikanth','Nagarjuna','Raju','Narasimha',123}
print(NameOfStudents) #{'Narasimha', 'Srikanth', 123, 'Raju', 'Nagarjuna'}
NameOfStudents.add('Narasimha')
print(NameOfStudents)#{'Nagarjuna', 'Raju', 123, 'Narasimha', 'Srikanth'}
NameOfStudents.add('Narasimha1')
print(NameOfStudents)#{'Narasimha1', 'Nagarjuna', 'Narasimha', 'Raju', 123, 'Srikanth'}
NameOfStudents.remove('Narasimha')
print(NameOfStudents)#{'Raju', 'Srikanth', 'Narasimha1', 123, 'Nagarjuna'}
NameOfStudents.pop()# randomly removes one element
print(NameOfStudents)#{'Nagarjuna', 'Srikanth', 123, 'Raju'}
#NameOfStudents.update('Narasimha')# adds each charactor in the set
print(NameOfStudents)#{'Nagarjuna', 'm', 'Raju', 'N', 'r', 'h', 'i', 's', 'a', 'Narasimha1', 123}
#NameOfStudents[1]="xyz" # this won't work in set
print(NameOfStudents)
NameOfStudents.discard('Narasimha')
print(NameOfStudents)#{'N', 'a', 'Narasimha1', 'Raju', 'i', 'Srikanth', 'r', 'm', 123, 'h', 's'}
NameOfStudents.update(["Pooja", "Ravi"]) #add these 2 elements to set
print(NameOfStudents)#{'Srikanth', 'Pooja', 'Narasimha1', 'Raju', 123, 'Ravi'}


# Union
set1={'Narasimha','Srikanth','Nagarjuna','Raju',123}
set2={'Narasimha','Srikanth','Nagarjuna','Sujatha'}
set_union = set1.union(set2)
print(set_union) #{'Srikanth', 'Raju', 'Nagarjuna', 'Sujatha', 'Narasimha', 123}


#Intersection
set_intersection = set1.intersection(set2)
print(set_intersection) #{'Nagarjuna', 'Srikanth', 'Narasimha'}

#Defference
set_difference = set1.difference(set2) #like set1 minus set2
print(set_difference) #{'Raju', 123}

set_difference = set2.difference(set1)  # like set2 minus set1
print(set_difference) #{'Sujatha'}

# symmetric_difference
set_difference = set1.symmetric_difference(set2) # (set11 - set2) union (set2 -set1)
print("symmetric_difference: ", set_difference) #{'Raju', 'Sujatha', 123}

set_difference = set2.symmetric_difference(set1) # (set11 - set2) union (set2 -set1)
print("symmetric_difference: ", set_difference) # {'Raju', 'Sujatha', 123}
'''

## Dictionary:

#Un ordered
#Mutable
#stores key-value pair
#Keys are unique value can be duplicate

