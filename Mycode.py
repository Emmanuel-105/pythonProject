def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)
number = int(input('Enter the start number: '))
try:
    countup(number)
except:
       number >= 996
       print('RUNTIME ERROR, RECURRING DEPTH EXCEEDED')
