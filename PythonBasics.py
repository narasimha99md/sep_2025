### Variables
'''
NameOfStudent ="Narasimha"
AgeOfStudent =25
EligibleForVote =True


#Camel case
nameOfStudent ="Narasimha"
ageOfStudent =25
eligibleForVote =True

#Pascal case
NameOfStudent ="Narasimha"
AgeOfStudent =25
EligibleForVote =True

#Snake case
name_of_student ="Narasimha"
age_of_student =25
eligible_for_vote =True

print("NameOfStudent is: ", name_of_student)
print("AgeOfStudent is: ",age_of_student)
print("EligibleForVote :",eligible_for_vote)

# Typecasting (Convert one data type to another)
age ="23"
age1 =90
sal=234.55
print(type(age))
print(type(age1))
print(type(sal))

# convert age type from string to integer
print(type(int(age)))


marks1 ="50"
marks2 ="40"

print(marks1+marks2) #5040
print(int(marks1)+int(marks2)) #90


# Upcasting
price =240
print(float(price)) #240.0

# Down casting
price1 =250.34
print(int(price1)) #250

#Control Statement(if ..else, if..elif)

age=17

if age>=18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")



age =100

if age < 18:
    print("Not Eligible for vote")
elif age >= 18 and age < 95:
    print("Eligible for vote")
else:
    print("Person is Super Senior Citigen ")


# for loop
for i in range (10):# range start with 0 upto 9
    print("Heloo :",i)


for i in range (1,10):
    print("Heloo :",i)

for i in range (0,10,1):
    print("Heloo :",i)
'''

## while loop

x=10
while x>0:
    print("X--> ",x)
    x-=1