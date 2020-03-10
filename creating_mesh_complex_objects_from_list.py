import numpy as np
from stl import mesh

#Bu kod üzerinden ilerleyebiliriz.
#We can proceed through this code

#I created a hexagonal prism with this program
# Define the N vertices of the object (N köşe)
#Yapacağımız iş 3 Boytulu veri bilgisi üzerinden oluşan şeklin köşelerini belirlemek
#What we are going to do is to determine the corners of the shape that consists of 3D data information.
vertices = np.array([\
		[-10, -10, -10],    #0
		[+10, -10, -10],    #1
		[+15, -10, 0],		#2
		[+10, -10, +10],	#3
		[-10, -10, +10],	#4
		[-15, -10, 0],		#5
		[+10, +10, -10],	#6
		[+15, +10, 0],		#7
		[+10, +10, +10],	#8
		[-10, +10, +10],	#9
		[-15, +10, 0],		#10
		[-10, +10, -10]		#11
		])

#Ardından burada bu şekli üçgenlere bölmek
#Then divide this shape into triangles here
# Define the 12 triangles composing the cube
#Burada dilimleme yapılıyor
#Slicing is done here
faces = np.array([\
		[0,1,5],
		[5,4,1],
		[1,4,3],
		[3,1,2],
		[2,7,8],
		[8,2,3],
		[3,8,9],
		[9,3,4],
		[4,5,9],
		[9,5,10],
		[10,5,0],
		[0,10,11],
		[11,0,1],
		[1,11,6],
		[6,1,2],
		[2,6,7],
		[7,8,9],
		[9,7,10],
		[10,7,11],
		[11,6,7]
		])

faces = np.array([\
		[0,1,5],
		[5,4,1],
		[1,4,3],
		[3,1,2],
		[2,7,8],
		[8,2,3],
		[3,8,9],
		[9,3,4],
		[4,5,9],
		[9,5,10],
		[10,5,0],
		[0,10,11],
		[11,0,1],
		[1,11,6],
		[6,1,2],
		[2,6,7],
		[7,8,9],
		[9,7,10],
		[10,7,11],
		[11,6,7]
		])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
	for j in range(3):
		cube.vectors[i][j] = vertices[f[j],:]
# Write the mesh to file "cube.stl"
cube.save('cube.stl')