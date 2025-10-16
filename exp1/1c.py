import math

r=int(input("Enter the radius:"))
h=int(input("Enter the height:"))

def volume(r,h):
    volume=math.pi*r*r*h
    return volume

def surface_area(r,h):
    surface_area=2*math.pi*r*h
    return surface_area

print("Surface area:",surface_area(r,h))
print("Volume:",volume(r,h))
