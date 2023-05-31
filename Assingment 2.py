a = [ 2,3,4,55,56,78,75,69,66,101,100 ]
x=0
y=0
for i in a:
    if i%2==0:
        x+=1
    else:
        y+=1
print(f"Even Count: {x}  Odd count: {y}")