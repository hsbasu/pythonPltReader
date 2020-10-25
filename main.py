# Python program to read binary .plt files.
# 
import pyPLTreader

datafile = open("2d_sample_data.plt", "rb")

# class read_tecplot_data(datafile):
def read_plt_data(data):
	'''
	This function takes the .plt datafile as input argument.
	It calls two functions: read_header() and read_data().
	It reads the "Header" block by calling read_header()
	and "Data" block by calling read_data().
	It returns all the information found in .plt via argument 'read_datafile'
	'''
	str=data.read()
	data_header = pyPLTreader.read_header(str)
	read_datafile = pyPLTreader.read_data(str, data_header, data)
	return read_datafile

read_data = read_plt_data(datafile)
# print('\n========================================\n')
# print(read_data)  # Prints all information found in the .plt file
# print('\n========================================\n')

vars_list = read_data['Var_names']
indices_list = read_data['Zones'][0]['Indices']
data_dict = read_data['Zones'][0]

print("Imax in read Zone: ", indices_list[0])
print("Jmax in read Zone: ", indices_list[1])
print("Kmax in read Zone: ", indices_list[2])
print("Number of Values Per Variable: ", indices_list[0] * indices_list[1] * indices_list[2])

print("Number of Variables found: ", len(vars_list))
print("List of variables:", vars_list, "\n")  # Prints lists of variables found in the .plt file

for i in range(0,len(vars_list)):
	var_name = vars_list[i]
	var_data = data_dict[vars_list[i]]
	
	print('========================================')
	print(type(var_data))  # Prints type of data
	print(var_name, '=', var_data)  # Prints the data corresponding to a variable
	print('========================================\n')   
