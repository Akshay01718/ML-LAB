import matplotlib.pyplot as plt
import pandas as pd
txt=open("./sentence.csv","r")
data=txt.read()
freq={}
for i in data:
    if i==" ": continue
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
df=pd.DataFrame(list(freq.items()),columns=["char","count"])
plt.bar(df["char"],df["count"])
plt.show()
plt.close
print(freq)