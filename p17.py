ones = {0:'',
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"}
teens = {10:"ten",
         11:"eleven",
         12:"twelve",
         13:"thirteen",
         14:"fourteen",
         15:"fifteen",
         16:"sixteen",
         17:"seventeen",
         18:"eighteen",
         19:"nineteen"}
tens = {20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety"}
h = len("hundred")
c = 0
for i in range(1,1001):
    if i == 1000:
        c += 11
        break
    if i % 100 == 0:
        c += len(ones[i/100])+h
    else:
        if i > 100:
            c += len(ones[i/100])+h+3
        rem = i % 100
        if rem < 10:
            c += len(ones[rem])
        elif rem < 20:
            c += len(teens[rem])
        else:
            c += len(tens[10*(rem/10)]) + len(ones[rem%10])
print c
