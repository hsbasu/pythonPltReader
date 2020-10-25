import tecplotPltReader

datafile = open("phase1000000.plt", "rb")

#class read_tecplot_data(datafile):
def test_read_data(data):
    str=data.read()
    headerr = tecplotPltReader.read_header(str)
    read_datafile = tecplotPltReader.read_data(str, headerr, data)
    print('\n')
    print(read_datafile)
    print('\n')
    return read_datafile

read_data = test_read_data(datafile)
vars_list = read_data['Var_names']
data_dict = read_data['Zones'][0]

print(vars_list)
for i in range(0,len(vars_list)):
    var_name = vars_list[i]
    var_data = data_dict[vars_list[i]]
    print(type(var_data))
    print(var_name, '=', var_data)
