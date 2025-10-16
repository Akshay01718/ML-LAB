text=open("./sentence.csv").read().lower()
text=text.strip('&*@#')

words=text.split()

print()
max=0
done=[]


for i in words:

    if i not in done:
        done.append(i)
    else:
        continue
    c=1
    for j in words:
        if i==j:
            c+=1
            
        if c>max:
            max=c
            word=i

print(f"The most frequent word:{word}\n")
print(f"Count:{c}")


    
