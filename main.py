# Python program to read binary .plt files.
# 
import pyPLTreader
import numpy as np

# datafile = open("2d_sample_data.plt", "rb")
with open("test_2019.plt", "rb") as datafile:

	mydata = pyPLTreader.read_data(datafile)
	# print('\n========================================\n')
	# print(mydata)  # Prints all information found in the .plt file
	# print('\n========================================\n')

	vars_list = mydata['Var_names']
	indices_list = mydata['Zones'][0]['Indices']
	data_dict = mydata['Zones'][0]

	NX = indices_list[0]
	NY = indices_list[1]
	NZ = indices_list[2]
	num_val = indices_list[0] * indices_list[1] * indices_list[2]

	print("Imax in read Zone: ", NX)
	print("Jmax in read Zone: ", NY)
	print("Kmax in read Zone: ", NZ)
	print("Number of Values Per Variable: ", num_val)

	print("Number of Variables found: ", len(vars_list))
	print("List of variables:", vars_list, "\n")  # Prints lists of variables found in the .plt file

	# var_data = []
	# for i in range(0,len(vars_list)):
	# 	var_name = vars_list[i]
	# 	var_data.append(data_dict[vars_list[i]])
	# 	var_dtype = var_data[i].dtype
	# 	var_data[i] = var_data[i].reshape(NY, NX)  # Convert 1D array to 2D (NY * NX)
	# 	var_data[i] = np.transpose(var_data[i])  # Convert 2D NY * NX to NX * NY
		# print('========================================')
		# print(type(var_data[i]))  # Prints type of data
		# print(var_dtype)  # Prints datatype of array
		# print(var_name, '=', var_data)  # Prints the data corresponding to a variable
		# print('========================================\n')

	# min_rho = np.min(var_data[2])
	# max_rho = np.max(var_data[2])

	# delx = var_data[1][0,0] - var_data[1][1,0]  # In micron
	# dely = var_data[1][0,0] - var_data[1][0,1]  # In micron
	# rho_at_intf = min_rho + (max_rho-min_rho)/2  # In kg/m^3
	# print(rho_at_intf)

	# defly = []
	# for x in range(0,NX):
	# 	for y in range (0,NY):
	# 		# print(var_data[1][x,y])
	# 		if (var_data[2][x,y] > rho_at_intf):
	# 			drho = var_data[2][x,y] - var_data[2][x,y-1]
	# 			dy = (rho_at_intf - var_data[2][x,y-1])/drho
	# 			defly.append(var_data[1][x,y] + (1-dy)*dely)
	# 			print(var_data[0][x,y],'\t',defly[x])
	# 			break

	# max_defly = np.max(np.abs(defly))
	# print(max_defly)
