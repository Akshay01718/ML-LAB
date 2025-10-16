import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=x

plt.plot(x,y1,label="y=x")
plt.title('Line PLot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


y2=[]
for i in x:
    y2.append(i**2)
plt.plot(x,y2,label="y=x^2")
plt.title('Curved PLot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

y3=[]
for i in x:
    y3.append(3**i)
plt.plot(x,y3,label="y=3^x")
plt.title('Exponential PLot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()



