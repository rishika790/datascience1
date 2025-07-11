# print("hello")
# a = "hello"
# num = 10

# age = 23
# age = 24
# print(age)
# print(age)
# name = "chandni"
# print(name)
# print("my name is",name)
# print("name dtype:-",type(name))
# print("len of name:-",len(name))
# ###indexing
# print(name[0])  
# # print(name[1])
# print(name[len(name)-1])
# name = "rishika"

# ###slicing in python
# name = "rishika"
# print(name[0:3])

# ###operation

# name =" rishika "
# last = " gour "
# upper_case = name.upper()
# print(upper_case)
# lower_last_name = last.lower()
# print(lower_last_name)
# print(name.count("n"))
# name = " rishika "
# last = " gour "
# print(name.title())
# print(name.capitalize())
# print(name+last)


# reversed_name = name[::-1]
# print(reversed_name)

# # for line in reversed(name):
# #     exec(line)

#######>>>>>>>>>>>>List>>>>>>>>>>>>>
# list


#lst = [1,2,3,4,5,6,7,"rohit",2.3]

# 
# mutanble
# duplicated values
# order 
# herto

###array>>>>  lst = [1,2,3,4,5,6,7]
#array
# print("my first list:-",lst)
# print("len of list:-",len(lst))
# print("type of list:-",type(lst))
# print(lst[0])

# print(lst[0:5])
#lst = [1,2,3,4,5,6,7,2.3]
#lst.pop()
#print(lst)
# lst.append(100)
# print(lst)
# lst.insert(0,1000)
# print(lst)
# copy_lst = lst.copy()
# print(copy_list)
# lst.reversed()
# lst.remove(2.3)
# print(lst)
# lst.sort()
#########>>>>>>>>>>>tuple>>>>>>>>>>>>.


#tpl = (1,2,3,4,5,6,"chandni",2.3)
# print("my first tuple:-",tpl)
# print("len of tuple:-",len(tpl))
# print("type of tuple:-",type(tpl))
# print(tpl[0])
# print(tpl[2])
# print(tpl[0:8])
# #build
# a = 1,2,58,5,58,5,5,85,2
# print(a)
# print(len(a))
# print(type(a))

# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)


#lst = [1,2,3,4,[5,6],7]
#print(lst)
#print(lst[4][0])
#print(lst[4][1])

# tpl = (1,2,58,2,8)
# print("max of tuple",(tpl))
# print("min of tuple",tpl)
# sum(tpl)


#>>>>>>>>>dictionary>>>>>>>>>>>>>>>>>>


# my_dict = {
#     "name":"monika",
#     "class":"2nd year",
#     "roll number":"12345",
#     "adderss":"jaipur"##### name item h
# }
# print("my first dict:-",my_dict)
# print("len of dict:-",len(my_dict))
# print("type of dict:-",type(my_dict))

# print(my_dict['name'])
# print(my_dict['class'])
# print(my_dict['roll number'])
# print(my_dict['adderss'])

# my_dict['adderss'] = "beawar"
# print(my_dict)
#  my_dict = {
#     "name":"monika",
#     "class":"2nd year",
#     "roll number":"12345",
#     "adderss":"jaipur"
# }
# my_dict['branch']="it"
# print(my_dic)


# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# copy_dict = my_dict.copy()
# print(copy_dict)
# my_dict.clear()

# a =input("enter a number")
# b =input("enter a second number")
# print(a*b)
# print(type(a))

# # Typecasting
# a =int("enter a number")
# b =int("enter a second number")
# print(a*b)

# # lst=[1,2,3,4,5,,6]
# # print("this is my list:-",lst)
# print("type of list",type(tpl))
# tpl =tuple(lst)
# print("this is my tuple:-",tpl)
# print("type of tuple:-"type(tpl))



# >>>>>>>>>>>>>set>>>>>>>>>>

# my_set=
# tuple =
# list = 
# set =
# dict =

# my_set = {1,2,3,4,5}
# print("this is my first set:-",my_set)
# print("len of my set:-",len(my_set))
# print("type of set:-",type(my_set))

# task >>>>>>>>>>
# my_set.umion()
# my_set.intersection()
# my_set.different()
# lst =lst(my_set)

# lst.append(100)
# print(set(lst))


class BMICalculator:
    def __init__(self , weight, height):
     self.weight = weight
     self.height = height  
    def calculator_bmi(self):
         bmi = self.weight / (self.height **2)
         return bmi
    def get_category(self):
         bmi = self.calculate_bmi()
         if bmi < 18.5:
              return "Underweight"
         elif 18.5 <= bmi < 24.9:
            return "Normal weight"
         elif 25 <= bmi < 29.9:
            return "Overweight"
         else:
            return "Obese"
weight = float(input("Enter weight (in kg):"))
hight = float(input("Enter height (in meters):"))
person = BMICalculator(weight.height)
bmi = person.calculator_bmi()
category = person.get_category()
print(f"\nYour BMI is: {bmi: 2f}")
print(f"Category: {category}")








