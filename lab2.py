sequence=range(45,210)
for elements in sequence:
    if elements==100:
        continue
    if elements==205:
        break
    print(elements)
       
product="what is the product of 7 * 24 ?"
while input(product)!="168":
    print("You answered this Question wrong, thr correct answer is 168")
else:
    print("your answered this Question correctly")    