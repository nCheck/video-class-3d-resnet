done = open('done.txt', 'r+')
alll = open('alll.txt', 'r+')

ds = []
als = []

for d in done:
    d = d.strip()
    ds.append(d)

for d in alll:
    d = d.strip()
    als.append(d)


done.close()
alll.close()


rem = open('input', 'w+')
    
for a in als:

    if a not in ds:
        rem.write(a + "\n")


rem.close()