def estimatePrice(m):
    m = float(m)
    a = -0.5
    b = 20000
    price = a*m + b 
    print("Estimated car price in function of mileage is: USD {}".format(price))

print("Please enter a mileage, so we can return a theoritical car price:")

mileage = input()

estimatePrice(mileage)




