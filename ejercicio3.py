n = 13
h = ''
while n <= 32:
    if n%2 != 0:
        h += ' %i' % n
    n += 1
print (h)
