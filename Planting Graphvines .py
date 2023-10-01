#!/usr/bin/env python
# coding: utf-8

# # Planting grapevines - question 13 

# ### this problem is asking use to make a code to solve the how many graphvines are need in each row using the 
# ### equation given

# In[1]:


# input from user
row_length = float(input("Enter the length of the row (in feet): "))
end_post_space = float(input("Enter the amount of space used by an end-post assembly (in feet): "))
space_between_vines = float(input("Enter the space between vines (in feet): "))

# equation for number of graphhvines 
vines_per_row = (row_length - 2 * end_post_space) / space_between_vines

# Print function to show function 
print("The number of grapevines that will fit in the row is:", int(vines_per_row))


# #### the code was a sucess and calculated the formula 

# ### my other notebook was having problems so I open a new notebook to restart fresh it wasnt the code but the program wasnt working for some reason. Some problems I faced before the program crashes was the order of oprations the lenght of row wont work in the  equation becasue of the order the code was in. Another problem was not putting an int or float function in the print statment under vines_per_row the answer wasnt working and thats how I found out I needed to add the int function for the equation to work. 

# In[ ]:




