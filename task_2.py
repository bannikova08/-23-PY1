def find_cp (group1, group2, d):
    p1 = set(group1.split(d))
    p2 = set(group2.split(d))
    cp = p1.intersection(p2)
    return sorted(cp)

group1 = 'John,Anna,Peter,Lisa'
group2 = 'Lisa,Michael,John'

print(find_cp(group1, group2, ","))  
