n = 19
a = list()
j = 0
while True:
    a.append(n%10)
    n = n//10
    if n < 1:
        for i in a:
            j += i**2
        if j == 1:
            print("yes")
            break
        elif j > 9:
            n = j
            del a[:]
        else:
            print("not")
            break
          yet rs
