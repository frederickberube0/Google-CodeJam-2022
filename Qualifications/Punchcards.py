def draw(x,y):
    for i in range(x):
        line1 = ""
        line2 = ""
        line3 = ""
        if i == 0:
            line1 = "..+"+"-+"*(y-1)
            line2 = "..|"+".|"*(y-1)
            line3 = "+-+"+"-+"*(y-1)
            print(line1)
            print(line2)
            print(line3)
        else:
            line1 = "|"+".|"*y
            line2 = "+"+"-+"*y
            print(line1)
            print(line2)

print(draw(5,4))
