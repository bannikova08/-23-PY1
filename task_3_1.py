def find_index(products, item):
    if item in products:
        return products.index(item)
    else:
        return None
    
products = ['apple', 'banana', 'orange', 'apple', 'grape']

item = 'apple'
index = find_index(products, item)
print(index)  

item = 'watermelon'
index = find_index(products, item)
print(index)  
