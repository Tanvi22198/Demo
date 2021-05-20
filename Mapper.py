import sys
from operator import itemgetter
import os
dim_info = open("test_dim.txt").readlines()[0].split(",")
row_a, col_b = map(int,dim_info)

filec=open("test_matrix.txt","r")
data=filec.read()
#filec.close()
print("----Input File----")
print(data)
lines=data.split("\n")
print ("----Mapper Output----")
for line in lines:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "A":
		for i in range(0,col_b):
			key = row + "," + str(i)
			print ("%s\t%s\t%s"%(key,col,value))
			file1 = open("mat_map_file.txt", "a")  # append mode 
			file1.write("%s\t%s\t%s"%(key,col,value))
			file1.write(";") 
			file1.close() 
	else:
		for j in range(0,row_a):
			key = str(j) + "," + col 
			print ("%s\t%s\t%s"%(key,row,value))
			file1 = open("mat_map_file.txt", "a")  # append mode 
			file1.write("%s\t%s\t%s"%(key,row,value))
			file1.write(";") 
			file1.close()