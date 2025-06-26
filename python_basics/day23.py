# manlo ki hamne agar ek list banayi h and usko koi aur list mai daldiya like l ek list h and maine m = l kardiya to ye ek reference ban jata hai..to m mai changes karo ya l mai dono change honge
# to better ye h ki list ki copy m mai daldo using m  = l.copy() isse dono list ke changes ek dusre se independent honge 
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
# print(k)
# l.extend(m)
print(l)