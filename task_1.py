money_capital = 50000
salary = 50000  
spend = 60000  
increase = 0.05
months = 0
budget=money_capital+salary

while money_capital+salary >= spend:
    budget += salary  
    budget -= spend
    if budget < 0:
        break
    spend += spend * increase
    months+=1

print(months)
