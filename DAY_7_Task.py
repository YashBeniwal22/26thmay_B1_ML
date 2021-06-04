import numpy as np
import pandas as pd

Menu=pd.DataFrame([['Paneer Tikka',350,'Spicy','Indian',4.4],
                   ['Egg Curry',250,'Spicy','Indian',4.8],
                   ['Butter Chicken',550,'Hot Spicy','Indian',4.7],
                   ['Kimchi Noodle',450,'Spicy','Chinese',4.9],
                   ['Pasta',450,'Creamy','Italin',4.4],
                   ['Pizza',550,'Crispy','Italin',4.4],
                   ['Chowmein',350,'Spicy','Chinese',4.4],
                   ['Butter Paneer',250,'Spicy','Indian',4.2],
                   ['Kadhai Paneer',280,'Indian',4.4],
                   ['Dosa',300,'Spicy','South Indian',4.6],
                   ['Daal Bati Churma',750,'Spicy','Indian',4.8],
                   ['Burger',250,'Bitter','Mexican',4.6],
                   ['Stuff Sandwich',350,'Spicy','American',4.7],
                   ['Samosa',150,'Spicy','Indian',4.5],
                   ['Idli Sambar',650,'Creamy','South Indian',4.2],
                   ['Dhokla',450,'Spicy','Indian',4.6],
                   ['Manchurian',250,'Salty','Chinese',4.7]],
                   columns=['Dish Name','Price','Taste','Cuisine','Ratings'])
print(Menu)

# Which Dish is most costliest

print('Which Dish is most costliest:')

for x in Menu.index:
    if Menu.loc[x,'Price']==Menu['Price'].max():
        print('\n\nCostliest Dish Name = ',Menu.loc[x,'Dish Name'],'\nDish Price = ',Menu.loc[x,'Price'])
        
# Which Dish is most Cheapest

print('Which Dish is most Cheapest:')

for x in Menu.index:
    if Menu.loc[x,'Price']==Menu['Price'].min():
        print('\n\nCheapest Dish = ',Menu.loc[x,'Dish Name'],'\nDish Price = ',Menu.loc[x,'Price'])
        
# Which cuisine is most popular

print('Which cuisine is most popular:')
for x in Menu.index:
    if Menu.loc[x,'Ratings']>=4.5:
        print('\n\nMost Popular Cuisine = ',Menu.loc[x,'Cuisine'],'\nDish Price = ',Menu.loc[x,'Price'],'\nDish Rating = ',Menu.loc[x,'Ratings'])
        
        
# Which Dish is most Spicy

print('Which Dish is most Spicy:')
for x in Menu.index:
    if Menu.loc[x,'Taste']=='Spicy':
        print('\n\nMost Spicy Dish = ',Menu.loc[x,'Dish Name'],'\nDish Price = ',Menu.loc[x,'Price'],'\nDish Rating = ',Menu.loc[x,'Ratings'])
        
# Which among them is Indian Dishes

print('Which among them is Indian Dishes:')

for x in Menu.index:
    if Menu.loc[x,'Cuisine']=='Indian':
        print('\n\nIndian Dish = ',Menu.loc[x,'Dish Name'],'\nDish Price = ',Menu.loc[x,'Price'],'\nDish Rating = ',Menu.loc[x,'Ratings'])
        


# Count different types of tastes in Dishes:

print('Count different types of tastes in Dishes:')


print(Menu['Taste'].value_counts(),'\n\n')    

# Types of Taste in Menu:

print('Types of Taste in Menu:')

for x in Menu.index:
 d=set(Menu['Taste'])
print(d)
