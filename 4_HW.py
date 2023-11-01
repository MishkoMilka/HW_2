a=int(input("Ведите число a"))
b=int(input("Ведите число b"))
c=int(input("Ведите число c"))
if a>b>c or c>b>a:
    print("b число це середне число")
if b>a<c or c>a<b:
    print("a число це середне число")
if b>c>a or a>c>b:
    print("c число це середне число")
