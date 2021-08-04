l = ['ania', 'tomek']
x = [l[i:i+2] for i in range(len(l))]
x[-1] = [l[-1], l[0]]
print(x)