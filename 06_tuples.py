#tuples are immutable data types in python
#it is started and ended with parentheses ()
a = (1, 2, 3, 4, 5)
print(a)
#tuple can have different data types
my_tuple2 = (1, "hello", 3.5, True)
print(my_tuple2)

#methods of tuple
no=a.count(2) #to count the number of occurrences of an item in the tuple
print(no)
index=a.index(3) #to find the index of an item in the tuple

print(index)


#remember tuples in python are immutable and they are started using ();

#more about tuples:
#A tuple in Python is an ordered, immutable collection of elements. 
#Unlike lists, tuples cannot be modified after creation, which makes them faster and more memory-efficient. 
#They are defined using parentheses, for example: t = (1, 2, 3). 
#Tuples can store different data types such as integers, strings, or even other tuples. 
#They support indexing, slicing, and iteration. 
#Because of their immutability, tuples are commonly used to store fixed data like coordinates, configuration settings, and function return values.
