# Python has no concept of data declaration. 
# Therefore, Python matrixes cannot be declared; 
# they must be built.

big_list = [0] * 100   # Create a list of 100 elements
                       #  each initialized to 0.
                    
print(len(big_list))


# The inner expression, [0] * 100), creates a list of 100 elements. 
# But the code repeats that data 200 times—not by creating 
# 200 separate rows but instead by creating 200 references to the same row.
mat = [[0] * 100] * 200

print(len(mat))

# So:
mat = [ ]
for i in range(200):
    mat.append([0] * 100)

print(len(mat))    


# So the previous example is a good candidate for a list comp:
mat = [[0]*100 for i in range(200)]

# Syntax:
# matrix_name = [[init] * ncols for var in range(nrows)]

# Because var isn't imporant and will not be reused.
# it can be subbed with "_"
mat2 = [ [0] * 25 for _ in range(30) ]

mat2 = [[ [0] * 25 for _ in range(20) ]
                   for _ in range(30) ]

# adding more levels:

mat2 = [[[ [0] * 10 for _ in range(10) ]
                    for _ in range(10) ]
                    for _ in range(10) ]


