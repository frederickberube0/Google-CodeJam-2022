def calc(printer1, printer2, printer3):

    #CMYB
    minC = min(printer1[0], printer2[0], printer3[0])
    minM = min(printer1[1], printer2[1], printer3[1])
    minY = min(printer1[2], printer2[2], printer3[2])
    minB = min(printer1[3], printer2[3], printer3[3])

    sumColors = minC + minM + minY + minB
    if sumColors < 10**6: return 0
    if sumColors == 10**6: return [minC, minM, minY, minB]

    leftOver = sumColors - 10**6

    lst = [minC, minM, minY, minB]
    
    for i in range(4):
        if leftOver > lst[i]:
            leftOver -= lst[i]
            lst[i] = 0
        else:
            lst[i] -= leftOver
            break
    return lst

print(calc([300000, 200000, 300000, 500000], [300000, 200000, 500000, 300000], [300000, 500000, 300000, 200000]))
print(calc([1000000,1000000, 0, 0], [0, 1000000,1000000, 1000000], [999999, 999999, 999999, 999999])  )
print(calc([768763, 148041, 178147, 984173], [699508, 515362, 534729, 714381], [949704, 625054, 946212, 951187]))
