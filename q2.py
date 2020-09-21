#Average of Students' Scores

a = "Students scores:"
x,y,z= ("80.0","90.0","66.5")

# Average from list of scores
scores_list = [80.0, 90.0, 66.5 ]
avg = sum(scores_list)/len(scores_list)
  
#Output

print (a)
print (x)
print (y)
print (z)
print ("The average score is: ",round(avg,2))

#Alternative 

degrees = input( "Enter value in degree: ")
radians = float(degrees) * 3.14 / 180

print("Degrees: ", degrees)
print("Radians: ", radians)