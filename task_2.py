money_capital = 0
salary = 50000  
spend = 60000  
increase = 0.03
month=0

while month < 10:
    money_capital += salary  
    money_capital -= spend
    spend += spend * increase
    month += 1

print('%.2f' %(-money_capital)) 
