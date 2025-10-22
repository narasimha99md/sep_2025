## Dictionary:

#Un ordered
#Mutable
#stores key-value pair
#Keys are unique value can be duplicate
'''
dict ={3:"Narasimha",1:"Sujju",2:"Nihar",4:"Jayanth"}
print(dict) #{3: 'Narasimha', 1: 'Sujju', 2: 'Nihar', 4: 'Jayanth'}
print(dict.items()) # dict_items([(3, 'Narasimha'), (1, 'Sujju'), (2, 'Nihar'), (4, 'Jayanth')])
# get keys from dict
print(dict.keys()) #dict_keys([3, 1, 2, 4])
# get values from dict
print(dict.values()) #dict_values(['Narasimha', 'Sujju', 'Nihar', 'Jayanth'])
#get employee data
print(dict.get(1))#Sujju
print(dict[2]) #Nihar
x=dict.get(3,0) #return 0 if that key not present else the value will be return for that key
print(x) # Narasimha
print("dict.get(30,0) --> ",dict.get(30,0)) # 0
#add one employee to dict
dict[5]="Krupa"
print("dict.get(5,0) --> ",dict.get(5,0)) #Krupa
print(dict[5])#Krupa
# update value for one employee
dict[5]="Krupendra Reddy"
print(dict[5]) #Krupendra Reddy
# delete record
dict.pop(5)
print("post 5th deletion ",dict) #{3: 'Narasimha', 1: 'Sujju', 2: 'Nihar', 4: 'Jayanth'}

del dict[2]
print("post 1th deletion ",dict) #{3: 'Narasimha', 1: 'Sujju', 4: 'Jayanth'}


# print key and values in the dict
dict ={3:"Narasimha",1:"Sujju",2:"Nihar",4:"Jayanth"}

for key,value in dict.items():
    print("Key & Value :" ,key,value)


# print only keys in the dict
dict ={3:"Narasimha",1:"Sujju",2:"Nihar",4:"Jayanth",5:"Modi"}
for key in dict.keys():
    print("Key  :" ,key)

# print only values in the dict
for Value in dict.values():
    print("Value  :" ,Value)
#find the length of dict
print("len(dict) -->", len(dict)) #5

##remove last item in the dict

print("dict.popitem() -->", dict.popitem()) #(5, 'Modi')

# clear whole dict
dict.clear()
print("after dict.clear() --> ",dict) # {}


######################### Strings  ###################
#strings:

#immutable
#characters of symbols
#array of bytes representing unicode characters
# string in python are surrounded by single or double quote
    # eg: str="narasimga rao"

name = "A"
name1 = "a"
print(name)# A
print(ord(name))#65
print(name1)#a
print(ord(name1))#97

print("chr(65) -->" ,chr(65)) #A
print("chr(97) -->" ,chr(97)) #a

print(name.upper())#A
print(name1.upper())#A


# print all the characters in a sequence

name = "ETL QA Labs"
length = len(name)

for char in name:
    print(char," ")

#print(length) #11
for char in range(length):
    print(name[char])

print("Length of String ==>", length) #11
print("name Data Type-->",type(name))
char_list =[]
for char in range(0,length,1):
    char_list += name[char]
    #print(name[char], "-Count-", name.count(name[char])) # char count
    #print(name[char],"-Index-",name.find(name[char]))# index of char
print("char_list",char_list)
print("".join(char_list))

###join usage in python
words = ["I", "love", "Python"]
result = " ".join(words)
print(result)


# Print string in reverse order using for loop

name = "ETL QA Labs"
length = len(name)
list_rev =[]
for char in range(length-1,-1,-1):
    #print(name[char])
    list_rev += name[char]
    #print(list_rev)

print("".join(list_rev))


# Print string in reverse order using while loop
name = "ETL QA Labs"
length = len(name)

start_idx=length-1
rev_str=[]
while start_idx  >= 0:
    #print(name[start_idx])
    rev_str += name[start_idx]
    start_idx =start_idx-1
print("".join(rev_str))

# Way 2: Print string in reverse order without loop

name = "ETL QA Labs"
length = len(name)
rev_str =""
for char in name:
    rev_str = char + rev_str
print(rev_str)

### using slicing

name = "ETL QA Labs"
rev = name[::-1]
print(rev)



## split string
str = "mandalapurao@gmail.com"
res_split = str.split('@')
print(res_split) #['mandalapurao', 'gmail.com']
print(" ".join(res_split))#mandalapurao gmail.com

str1 = "narasimha rao"
#res_split1 = str1.split()# default value is space for split() function
res_split1 = str1.split(" ")
print(res_split1) #['mandalapurao', 'gmail.com']
print(" ".join(res_split1))#mandalapurao gmail.com


## replace specific character in a string

str = "narasimha rao"
print(str.replace("a","x")) #nxrxsimhx rxo
print(str.replace("na","Y")) #Yrasimha rao
print(str.replace("rao","mandalapu"))#narasimha mandalapu


#  replace first occurence of'a' with 1 and 2nd with 2 ...and so on
#name ="narasimha rao
# result: n1r2simh3 r4o

name ="narasimha rao"
res_name=""
start_num=1
length=len(name)
print(length)

for char in range(length):
    if name[char]=='a':
        res_name =res_name+str(start_num)
        start_num =start_num+1
        print("in if: ",res_name)
    else:
        res_name =res_name+name[char]
        print("in else: ", res_name)

print("final-->",res_name)

'''
##### video 5 completed