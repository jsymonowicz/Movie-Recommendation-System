'''
This is a program with:
1) two syntax (compilation) errors (lines 8 and 12)
2) a runtime error (line 11)
3) a logical error (line 12)
'''
#Path length in kilometres:
    path = 60#Syntax error: wrong indentation
#Time in hours:
time = 0
velocity = path / time#Runtime Error: dividing by 0
print f"Velocity is {velocity} m/s." #1) Syntax Error: missing () in print(); 2) Logical Error: units are wrong, should be km/h