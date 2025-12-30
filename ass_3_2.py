import math
def ask_user_no(nub):
    sqq= math.sqrt(nub)
    logg= math.log(nub)
    sinn= math.sin(nub)
    return sqq,logg,sinn

input_no=int(input("enter a number: "))

rs1,rs2,rs3=ask_user_no(input_no)
print(f"Square root: {rs1}\nLogarithm: {rs2}\nSine: {rs3}")