pythonmarks =78
cprogrammarks = 59.8
mathsmarks = 76
physicsmarks = 79
total=pythonmarks + cprogrammarks + mathsmarks + physicsmarks
aggregate=total/4
print("TOTAL=",total)
print("AGGREGATE=",aggregate)
if(total > 400):
    print(" INVALID MARKS ")
elif(aggregate > 75):
    print("DISTINCTION")
elif(aggregate > 60):
    print("FIRST DIVISION")
elif(aggregate > 50):
    print("SECOND DIVISION")
else:
    print(" FAIL ")
