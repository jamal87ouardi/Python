


fin= open(r"C:\Users\DELL\Desktop\inputs.txt", "r")
fout= open(r"C:\Users\DELL\Desktop\out.txt", "a")

a=int(fin.readline())
b=int(fin.readline())
c=int(fin.readline())

print(a)



delta = b*b - (4*a*c)

fout.write(f"{delta}\n")

out2 = 15

fout.write(f"{out2}\n")

fout.close()

fout= open(r"C:\Users\DELL\Desktop\out.txt", "r")

d=int(fout.readline())

print(d+6)


