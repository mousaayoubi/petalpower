import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory)

#Inspect first ten rows
print(inventory.head(10))

#Choose Staten Island location
staten_island = inventory.head(10)
print(staten_island)

#Choose the product description column for the staten island location
product_request = staten_island['product_description']
print(product_request)

#Choose products that are in Brooklyn and of type seeds
seed_request = (inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')
print(seed_request)

#Check in stock
inventory['in_stock'] = inventory.apply(lambda x: True if x['quantity']>0 else False, axis=1)
print(inventory)

#Add column for total inventory value
inventory['total_value'] = inventory.price * inventory.quantity
print(inventory)
a = sum(inventory['total_value'])
print(a)

#Add combine lambda function
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

#Add full description column usind combine lambda function
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)