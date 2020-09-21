# Program angle conversion 
def Convert(Degree):
    pi = 3.14
    return (Degree * (pi / 180));

Degree = 150;
Radians = Convert(Degree);

print("Degrees:",Degree)
print("Radians:",Radians)