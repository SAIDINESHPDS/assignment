# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hKNOAAIASywyH7BwWaGIndPnqQnF9GHj
"""

# Question 1
list_1 = ["samsung","apple","oneplus"]
list_2 = ["puma","nike","addidas"]

# Question 2
list1= ["samsung","apple","oneplus"]
list2 = ["puma","nike","addidas"]
list3 = []
for i in list1:
   if i in list2:
      list3.append(i)

print('first list=',list1)
print('second list',list2)
print('the common elements are:',list3)

# Question 3
for i in range(20,40):
 if i%2==0:
   print(i,end=" ")



