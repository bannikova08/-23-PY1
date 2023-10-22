money_capital = 0
salary = 50000  
spend = 60000  
increase = 0.03

for month in range(10):
    money_capital += salary  
    money_capital -= spend
    spend += spend * increase

print('%.2f' %(-money_capital))    
