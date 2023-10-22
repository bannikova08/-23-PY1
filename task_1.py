money_capital = 50000
salary = 50000  
spend = 60000  
increase = 0.05
months = 0
while money_capital+salary > spend:
    money_capital += salary  
    money_capital -= spend
    spend += spend * increase
    months+=1

print(months)    
    
